import pandas as pd
from ydata_profiling import ProfileReport

filepath = r'../data/week/Week-Data-Network.csv'
title = 'Week-Data-Network'
df = pd.read_csv(filepath)

report_filepath = filepath.replace('.csv', '_report.html')
profile = ProfileReport(df, title=title, minimal=True)
profile.to_file(report_filepath)
