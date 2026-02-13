import pandas as pd
import numpy as np

def summarize(df):

    summary = {
        'column':[col for col in df.columns],
        'datatype':[],
        'missing_count':[],
        'missing_%':[],
        'unique_count':[]
        
    }
    total_rows = len(df)

    for col in df.columns:
        summary['datatype'].append(str(df[col].dtype))
        summary['missing_count'].append(df[col].isnull().sum())
        per = ((df[col].isnull().sum()/total_rows)*100).round(2)
        summary['missing_%'].append(per)
        summary['unique_count'].append(df[col].nunique())
        
    
    fd = pd.DataFrame(summary)

    return fd

