#!/usr/bin/env python
import sys
import logging
from pprint import pprint
import numpy as np

from pyomo.environ import *
from twimage import add2canvas, Point, heatmap

# sys.path.insert(0, './common')

import settings
from common.BaseModel import BaseModel

_log = logging.getLogger(__name__)


class select-points(BaseModel):

    def __init__(self, name: str, config: dict) -> None:
        super().__init__(name)

        self.config = config
        model = self.instance  # from BaseModel

        ################################################################################
        # Sets
        ################################################################################

        ################################################################################
        # Params put at model
        ################################################################################

        ################################################################################
        # Var
        ################################################################################

        ################################################################################
        # Constraints
        ################################################################################

        ################################################################################
        # Objective
        ################################################################################
        def obj_profit(model):
            cost = 0
            profit = 0
            return profit - cost

        model.objective = Objective(rule=obj_profit, sense=maximize)

    def show(self):
        if self.is_solved:
            pprint(self.result)
            # df = self.populate_df(('x',))  # must have same dimension
        else:
            _log.warning(f"Model not solved optimally.")

    def plot(self, debug: bool = False):
        if not self.is_solved:
            _log.warning(f"Cannot plot, model not solved properly.")
            return
        x = [k for (k, v) in self.result['x'].items() if v > 0.9]
        height = len(x)
        width = self.N
        canvas = np.zeros((height, width))

        for l, (i, j) in enumerate(x):
            m = np.ones((1, j - i + 1)) * (j - i + 1)
            canvas = add2canvas(canvas, m, Point(l, i - 1), debug=debug, merge=False)

        figsize = (width / 2, height / 2)
        _log.info(f"Creating heatmap plot: {figsize}.")
        heatmap(
            canvas,
            origin='lower',
            show_data=True,
            # figsize=figsize,
            vmin=0.1, vmax=999,
            extend='both',
            outlier_color_max='grey',
            outlier_color_min='white',
            hide_data_map=[0, 1000],
            title='Task Scheduling',
            xlabel='time slot',
            ylabel='task',
        )


if __name__ == "__main__":
    log_fmt = r"%(asctime)-15s %(levelname)s %(name)s %(funcName)s:%(lineno)d %(message)s"
    logging.basicConfig(format=log_fmt, level=logging.DEBUG)
    logging.getLogger('matplotlib').setLevel(logging.INFO)
    print(f"{'select-points':.^80}")

    name = 'test'
    config = getattr(settings, name)

    m = select-points(name=name, config=config)
    m.save_model()
    m.solve(tee=False, keepfiles=False)
    m.save_model()

    if m.is_solved:
        m.save_dill()
        # df = m.populate_df(('x',))
        m.show()
