#!/usr/bin/env python
import sys
import logging
from dataclasses import dataclass
from math import sqrt
from pprint import pprint
import numpy as np

import pyomo.environ as pyo

import settings
from common.BaseModel import BaseModel
from helper import Ok, group, plot_points

_log = logging.getLogger(__name__)


@dataclass
class Point:
    x: float
    y: float


class SelectPoints(BaseModel):

    def __init__(self, name: str, config: dict) -> None:
        super().__init__(name)

        self.config = config
        m = self.instance  # from BaseModel
        self.points = config['points']
        self.group_membership = config['group_membership']

        ################################################################################
        # Sets
        ################################################################################
        m.I = pyo.RangeSet(config['N'])
        m.G = pyo.RangeSet(config['G'])
        m.Ok = pyo.Set(initialize=Ok(config).ok)

        ################################################################################
        # Params put at model
        ################################################################################
        m.Points = pyo.Set(initialize=self.points.values())

        @m.Param(m.Ok)
        def distance(model, i, j):
            p = Point(*self.points[i])
            q = Point(*self.points[j])
            return sqrt((p.x - q.x) ** 2 + (p.y - q.y) ** 2)

        m.groups = pyo.Param(m.G, initialize=group(config))

        ################################################################################
        # Var
        ################################################################################
        m.x = pyo.Var(m.I, domain=pyo.Binary, initialize=0)
        m.pair = pyo.Var(m.Ok, domain=pyo.Binary, initialize=0)

        ################################################################################
        # Constraints
        ################################################################################
        @m.Constraint(m.G)
        def one_point_per_group(m, g):
            return sum(m.x[i] for i in m.groups[g]) == 1

        @m.Constraint(m.Ok)
        def both_selected(m, i, j):
            return m.pair[i, j] >= m.x[i] + m.x[j] - 1

        ################################################################################
        # Objective
        ################################################################################
        def total_distance_rule(m):
            return sum(
                m.pair[i, j] * m.distance[i, j] for (i, j) in m.Ok)

        m.objective = pyo.Objective(rule=total_distance_rule, sense=pyo.minimize)

    def show(self):
        if self.is_solved:
            pprint(self.result)
            plot_points(config, m.result)
        else:
            _log.warning(f"Model not solved optimally.")


if __name__ == "__main__":
    log_fmt = r"%(asctime)-15s %(levelname)s %(name)s %(funcName)s:%(lineno)d %(message)s"
    logging.basicConfig(format=log_fmt, level=logging.DEBUG)
    logging.getLogger('matplotlib').setLevel(logging.INFO)
    print(f"{'select-points':.^80}")

    name = 'full'
    config = getattr(settings, name)

    m = SelectPoints(name=name, config=config)
    m.save_model()
    m.solve(tee=False, keepfiles=False)
    m.save_model()

    if m.is_solved:
        m.save_dill()
        m.show()
