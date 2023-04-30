import sys
from pathlib import Path

import numpy as np
import pandas as pd

from select_points import SelectPoints

# if len(sys.argv) != 2:
#     print(f"\n-E- Usage: ipy.py 'model.dill'")
#     sys.exit(1)
#
# name = sys.argv[1]
name = 'xxx.dill'
p = Path(name)

m = SelectPoints.load_dill(name)
print(f"\n -M- model {name} available in variable: m")

# df.to_pickle(p.with_suffix('.pbz2'))
