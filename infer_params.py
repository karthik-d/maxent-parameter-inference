import pandas as pd
import numpy as np
import maxent
import os


DATA_FILE = os.path.join("./data/")


data_df = pd.read_csv(DATA_FILE)