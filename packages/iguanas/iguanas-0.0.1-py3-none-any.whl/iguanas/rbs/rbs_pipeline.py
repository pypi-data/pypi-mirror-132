"""Defines a Rules-Based System (RBS) pipeline."""
import pandas as pd
import numpy as np
import iguanas.utils as utils
from iguanas.utils.types import PandasDataFrame, PandasSeries
from iguanas.utils.typing import PandasDataFrameType, PandasSeriesType
from typing import List, Tuple


class RBSPipeline:
    """
    A pipeline with each stage giving a decision - either 0 or 1 (corresponding 
    to the binary target). Each stage is configured with a set of rules which, 
    if any of them trigger, mark the relevant records with that decision.

    Parameters
    ----------
    config : List[Tuple(int, list)] 
        The optimised pipeline configuration, where each element aligns to a
        stage in the pipeline. Each element is a tuple with 2 elements: the 
        first element corresponds to the decision made at that stage (either 0
        or 1); the second element is a list of the rules that must trigger to 
        give that decision.
    final_decision : int
        The final decision to apply if no rules are triggered. Must be 
        either 0 or 1.    

    Raises
    ------
    ValueError
        `config` must be a list.
    ValueError
        `final_decision` must be either 0 or 1.

    Attributes
    ----------
    score : float 
        The result of the `metric` function when the pipeline is applied.    
    """

    def __init__(self,
                 config: List[Tuple[int, list]],
                 final_decision: int) -> None:
        if not isinstance(config, list):
            raise ValueError('`config` must be a list')
        if final_decision not in [0, 1]:
            raise ValueError('`final_decision` must be either 0 or 1')
        self.config = config
        self.final_decision = final_decision

    def predict(self,
                X_rules: PandasDataFrameType) -> PandasSeriesType:
        """
        Applies the pipeline to the given dataset and returns its prediction.

        Parameters
        ----------
        X_rules : PandasDataFrameType
            Dataset of each applied rule.

        Returns
        -------
        PandasSeriesType
            The prediction of the pipeline.        
        """

        utils.check_allowed_types(X_rules, 'X_rules', [PandasDataFrame])
        num_rows = len(X_rules)
        stage_level_preds = self._get_stage_level_preds(X_rules, self.config)
        y_pred = self._get_pipeline_pred(stage_level_preds, num_rows)
        return y_pred

    @staticmethod
    def _get_stage_level_preds(X_rules: PandasDataFrameType,
                               config: List[Tuple[int, list]]) -> PandasDataFrameType:
        """Returns the predictions for each stage in the pipeline"""

        rules = X_rules.columns.tolist()
        stage_level_preds = []
        for i, stage in enumerate(config):
            decision = stage[0]
            stage_rules = stage[1]
            stage_rules_present = [
                rule for rule in stage_rules if rule in rules]
            if not stage_rules_present:
                continue
            y_pred_stage = (
                X_rules[stage_rules_present].sum(1) > 0).astype(int)
            if decision == 0:
                y_pred_stage = -y_pred_stage
            y_pred_stage.name = f'Stage={i}, Decision={decision}'
            stage_level_preds.append(y_pred_stage)
        if not stage_level_preds:
            return None
        else:
            stage_level_preds = pd.concat(stage_level_preds, axis=1)
            return stage_level_preds

    def _get_pipeline_pred(self, stage_level_preds: PandasDataFrameType,
                           num_rows: int) -> PandasSeriesType:
        """Returns the predictions of the pipeline"""

        if stage_level_preds is None:
            return np.ones(num_rows) * self.final_decision
        for stage_idx in range(0, len(stage_level_preds.columns)):
            if stage_idx == 0:
                y_pred = stage_level_preds.iloc[:, stage_idx]
            else:
                y_pred = (
                    (y_pred == 0).astype(int) * stage_level_preds.iloc[:, stage_idx]) + y_pred
        y_pred = ((y_pred == 0).astype(int) * self.final_decision) + y_pred
        y_pred = (y_pred > 0).astype(int)
        return y_pred
