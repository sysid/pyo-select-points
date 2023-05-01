import logging
import os
from pprint import pprint

import pytest

import settings
from helper import Ok, plot_points, group, generate_test_data

log_fmt = r"%(asctime)-15s %(levelname)s %(name)s %(funcName)s:%(lineno)d %(message)s"
logging.basicConfig(format=log_fmt, level=logging.DEBUG)
logging.getLogger('matplotlib').setLevel(logging.INFO)


def test_ok():
    expected = {(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10),
                (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (4, 8), (4, 9), (4, 10), (5, 8), (5, 9),
                (5, 10), (6, 8), (6, 9), (6, 10), (7, 8), (7, 9), (7, 10)}
    ok = Ok(config=getattr(settings, 'test'))
    assert ok.ok == expected


def test_plot_points():
    plot_points(config=getattr(settings, 'full2'))


def test_group():
    groups = group(config=getattr(settings, 'test'))
    assert groups.get(3) == [2, 3]
    _ = None


def test_generate_test_data():
    # Example usage:
    N = 100
    G = 10
    test = generate_test_data(N, G)
    pprint(test)
    _ = None


def test_print_environment_variables():
    for key, value in os.environ.items():
        print(f"{key}: {value}")
