#Topic ----Segment - incomplete
#https://plotnine.readthedocs.io/en/latest/generated/plotnine.geoms.geom_segment.html#ranges-of-similar-variables

import numpy as np
import pandas as pd
import pandas as pd
import pandas.api.types as pdtypes
import numpy as np

from plotnine import *
from plydata import *
from plotnine.data import mtcars
#%%%

mtcars >> sample_n(10, random_state=123)


#%%%
geom_segment(mapping=None, data=None, stat='identity', position='identity',
             na_rm=False, inherit_aes=True, show_legend=None, arrow=None,
             lineend='butt', **kwargs)


#%%%

