import logging
import os
from pprint import pprint

import pytest

import settings
from helper import plot_points, create_ok

log_fmt = r"%(asctime)-15s %(levelname)s %(name)s %(funcName)s:%(lineno)d %(message)s"
logging.basicConfig(format=log_fmt, level=logging.DEBUG)
logging.getLogger('matplotlib').setLevel(logging.INFO)


def test_plot_points():
    plot_points(config=getattr(settings, 'full'))


def test_ok():
    ok = create_ok(config=getattr(settings, 'test'))
    assert (len(ok) == 45)
    _ = None


def test_print_environment_variables():
    for key, value in os.environ.items():
        print(f"{key}: {value}")
