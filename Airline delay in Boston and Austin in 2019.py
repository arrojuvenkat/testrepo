Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 20 2015, 20:20:57) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # installing plotly
! pip3 install plotly

# Standard plotly imports
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)

import pandas as pd

# Prepare data frames
airlineDelay = pd.read_csv("data/2019_airline_delay_causes.csv")

aus_df = airlineDelay[airlineDelay.airport == 'AUS'
bos_df = airlineDelay[airlineDelay.airport == 'BOS']

aus_month=aus_df.arr_del15.groupby(aus_df.month).sum()
bos_month=bos_df.arr_del15.groupby(bos_df.month).sum()

aus_month=aus_month.reset_index()
bos_month=bos_month.reset_index()

aus_df=aus_month[['month','arr_del15']]
bos_df=bos_month[['month','arr_del15']]

# create aus_ad
aus_ad = go.Scatter(  
                  x = aus_df.month,
                  y = aus_df.arr_del15.groupby(aus_df.month).sum(),
                  mode = "lines+markers", line={'dash':'dot'},
                  text = aus_df.month, 
                  name='Aus')

# create bos_ad
bos_ad = go.Scatter(  
                  x = bos_df.month,
                  y = bos_df.arr_del15.groupby(bos_df.month).sum(),
                  mode = "lines+markers", line={'dash':'dot'},
                  text = bos_df.month, 
                  name='Boston')

data = [aus_ad,bos_ad]

layout = dict(title = 'Airline delay in Boston & Austin, in 2019',
              xaxis= dict(title= 'Months',ticklen= 5,showgrid=True),
              yaxis = dict(title= 'No of filghts delayed'), 
              showlegend=True
             )

fig = dict(data = data, layout = layout)

iplot(fig)

#Result: In Austin & Boston, more flights delayed in JUN and very less delayed in September in 2019.
