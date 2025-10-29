import numpy as np
import pandas as pd

def sma(hist_price_df, window_size):
    window_start = 0
    window_end =  window_size
    sma = []

    # For i in range of values that
    # is from 0 to the size of the stock list + 1
    for i in range(len(hist_price_df["Close"])):
        # If i is greater than or equal to the window size
        if i >= window_size-1:
            # Find the average of values within a given window of size defined above 
            sma.append(sum(hist_price_df["Close"][window_start:window_end])/window_size)
            # Increment window start and end by 1 to slide window towards the end of the list   
            window_start += 1
            window_end += 1
        else:
            sma.append(np.nan)
    hist_price_df["sma_of_"+str(window_size)] = sma
    return hist_price_df
