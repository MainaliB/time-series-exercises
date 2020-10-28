
import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")


def prep_sales_df(df):
    
    '''Takes in a dataframe, performs necessary date time conversion, sets date as index, creates new 
    columns(months, day, and sales total) and returns the dataframe'''
    
    df.sale_date = pd.to_datetime(df.sale_date, format = '%a, %d %b %Y %H:%M:%S %Z')
    df = df.set_index('sale_date').sort_index()
    df['month'] = df.index.month_name()
    df['day']= df.index.day_name()
    df['sales_total'] = df.sale_amount * df.item_price
    
    return df