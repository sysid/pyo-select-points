import logging
from collections import defaultdict
from pprint import pprint
from typing import Dict
import matplotlib.pyplot as plt
import numpy as np

import settings

_log = logging.getLogger(__name__)


class Ok(object):

    def __init__(self, config: Dict) -> None:
        super().__init__()
        self.config = config
        self.group_membership = config['group_membership']

        # self.ok = defaultdict(lambda: 0)
        self.ok = set()
        self.create_ok()

    def create_ok(self) -> None:
        for i, group_i in self.group_membership:
            for j, group_j in self.group_membership:
                if i < j and group_i != group_j:
                    self.ok.add((i, j))


def plot_points(config, result=None):
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(12, 8))

    # Get unique group IDs
    unique_groups = set(group for _, group in config['group_membership'])

    # Generate colors for each group
    color_map = plt.cm.rainbow(np.linspace(0, 1, len(unique_groups)))
    group_colors = {group: color for group, color in zip(unique_groups, color_map)}

    # Create a dictionary to store legend handles
    legend_handles = {}

    # Plot the points with different colors per group and add point names
    for point, group in config['group_membership']:
        x, y = config['points'][point]
        color = group_colors[group]
        scatter = ax.scatter(x, y, color=color)
        ax.annotate(f'{point}', (x, y), textcoords="offset points", xytext=(0, 5), ha='center')

        # Add the scatter object to legend_handles if not already present
        if group not in legend_handles:
            legend_handles[group] = scatter

    if result is not None:
        for pair, value in result["pair"].items():
            if value == 1:
                point1, point2 = pair
                x1, y1 = config['points'][point1]
                x2, y2 = config['points'][point2]
                ax.plot([x1, x2], [y1, y2], linestyle='-', linewidth=1, color='gray')

    # Add labels and legend
    # ax.set_xlabel('X-axis')
    # ax.set_ylabel('Y-axis')
    ax.legend(legend_handles.values(), [f'Group {group}' for group in legend_handles.keys()],
              title='Groups', loc='upper left', bbox_to_anchor=(1.05, 1))

    # Show the plot
    plt.tight_layout()
    plt.show()


def group(config: Dict) -> Dict:
    memberships = config['group_membership']
    groups = defaultdict(lambda: list())
    for point, group in memberships:
        groups[group].append(point)
    return groups


if __name__ == '__main__':
    log_fmt = r'%(asctime)-15s %(levelname)s %(name)s %(funcName)s:%(lineno)d %(message)s'
    logging.basicConfig(format=log_fmt, level=logging.DEBUG)
    logging.getLogger('matplotlib').setLevel(logging.INFO)

    name = 'test'
    ok = Ok(config=getattr(settings, name))
    pprint(ok.ok)
