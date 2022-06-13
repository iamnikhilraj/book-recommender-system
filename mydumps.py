from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd
pd.set_option('display.max_columns',10)
popular_df = pickle.load(open('popular.pkl','rb'))
print(popular_df["Image-URL-M"].head(1))