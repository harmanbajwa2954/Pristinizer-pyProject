import pandas as pd

def analyze(df):

    summary = {
        'column':[col for col in df.columns],
        'datatype':[],
        'missing_count':[],
        'missing_%':[],
        'unique_count':[]
        
    }
    total_rows = len(df)

    for col in df.columns:
        summary['datatype'].append(df[col].dtype)
        summary['missing_count'].append(df[col].isNull().sum())
        summary['missing_%'].append((df[col].isNull().sum()/total_rows)*100)
        summary['unique_count'].append(df[col].nunique())
        
    

    return df

