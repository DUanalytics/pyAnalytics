# -*- coding: utf-8 -*-
#not working due library issues

#Plots using ggplot
#pip install ggplot
#pip install tslib  #additional
#pip install plotnine
#pip install 'plotnin[all]'

#ggplot is python implmentation of grammar of graphics.
#trying to match the features of ggplot on R

import pandas as pd
import numpy as np
from plotnine import *

from pydataset import data
mtcars = data('mtcars')
mtcars.head()

from pandas import Timestamp
#from pandas.lib import Timestamp
from tslib import *
import pandas as pd
from ggplot import *
#error tslib


ggplot(mtcars, aes(x=wt, y=mpg)) + geom_point()
