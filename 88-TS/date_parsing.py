#python : Topic :.......

#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns

#other
#pip install python-dateutil
from dateutil import tz
from datetime import datetime
indiaTime = datetime.now(tz=tz.gettz("Asia/Kolkatta"))
indiaTime
indiaTime.tzname()

#parset dates
from dateutil import parser
parser.parse('Sunday, August 9th at 8am')

#time differences
from dateutil.relativedelta import relativedelta
from dateutil import parser
start_date = parser.parse('Sunday, Aug 8th, 2020 at 8:15 AM')
start_date
end_date = parser.parse('Aug 15th, 2020 at 13:00')
end_date
relativedelta(start_date, end_date)
relativedelta(end_date, start_date)


#recurring events
from dateutil import rrule
from dateutil import parser
#every Mon & Fri at 10 am
list( 
      rrule.rrule(
          rrule.WEEKLY,
          byweekday = (rrule.MO, rrule.FR),
          dtstart = parser.parse('Aug 8, 2020 at 10 AM'),
          until = parser.parse('Oct 10, 2020'),
          )
      )
