import pandas as pd 
import numpy as np 
import os 


DATA_FILE = os.path.join("./data/")

# first column is the time step.
# each row corresponds to specific time point. 
# each column is a measurement of a variable for a specific ecoli, formatted as var_n.
data_df = pd.read_csv()