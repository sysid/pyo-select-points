import logging
import random
from typing import Dict, Set

import settings

_log = logging.getLogger(__name__)


def generate_test_data(N, G):
    if N < G:
        raise ValueError("Number of points (N) must be greater than or equal to the number of groups (G)")

    points = {}
    group_membership = []

    for i in range(1, N + 1):
        x = round(random.uniform(0, 100), 3)
        y = round(random.uniform(0, 100), 3)
        points[i] = (x, y)

    # Assign one point to each group
    for i in range(1, G + 1):
        group_membership.append((i, i))

    # Randomly assign the remaining points to the groups
    for i in range(G + 1, N + 1):
        group = random.randint(1, G)
        group_membership.append((i, group))

    test = {
        'N': N,
        'G': G,
        'points': points,
        'group_membership': group_membership
    }

    return test


import matplotlib.pyplot as plt

data = {
    'points': {
        # ... (all the points from the previous dictionary)
    }
}


def plot_points(config: Dict, result: Dict = None):
    data = config
    # Extract x and y coordinates from the data dictionary
    x_coords = [coord[0] for coord in data['points'].values()]
    y_coords = [coord[1] for coord in data['points'].values()]
    fig, ax = plt.subplots(figsize=(12, 8))

    # Create a scatter plot
    ax.scatter(x_coords, y_coords)

    if result is not None:
        # Highlight and increase size of the points with x values in the result dictionary
        x_result = [data['points'][i][0] for i in result['x'].keys() if result['x'][i] == 1]
        y_result = [data['points'][i][1] for i in result['x'].keys() if result['x'][i] == 1]
        ax.scatter(x_result, y_result, color='red', s=100)

    # Label the points
    for i, (x, y) in data['points'].items():
        ax.annotate(f'{i}', (x, y), textcoords="offset points", xytext=(0, 5), ha='center')

    # Set axis labels
    plt.xlabel('x')
    plt.ylabel('y')

    # Show the plot
    plt.show()


def create_ok(config: Dict) -> Set[tuple]:
    points = config['points'].keys()
    ok: Set = set()
    for i in points:
        for j in points:
            if i < j:
                ok.add((i, j))
    return ok


if __name__ == '__main__':
    log_fmt = r'%(asctime)-15s %(levelname)s %(name)s %(funcName)s:%(lineno)d %(message)s'
    logging.basicConfig(format=log_fmt, level=logging.DEBUG)
    logging.getLogger('matplotlib').setLevel(logging.INFO)

    # name = 'test'
    # ok = Ok(config=getattr(settings, name))
    # pprint(ok.ok)
    plot_points(config=getattr(settings, 'test'))
