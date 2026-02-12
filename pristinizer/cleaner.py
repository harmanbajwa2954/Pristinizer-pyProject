import pandas as pd

def clean(df):
    """This function will clean the DataFrame
    standardizing column names
    by removing duplicate values
    handling missing values
    fixing datatypes
    removing empty columns
    """

    df = df.copy()

    # removing duplicate values
    df = df.drop_duplicates()

    # standardizing columns names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')   
    #the strip() method removes any leading and trainling whitespaces
    
    '''handling missing values'''

    #checking for empty columns and fully empty rows
    empty_cols = [cols for cols in df.columns if df[cols].isnull().all()]
    df.drop(empty_cols,axis =1, inplace =True)
    df.dropna(how='all', inplace=True)

    #replacing empty values according to the column type
    for cols in df.columns:
        if df[cols].dtype == 'str' or df[cols].dtype == 'object' or df[cols].dtype == 'string' :
            df[cols] = df[cols].fillna('unknown')          # fills empty categorical values with 'unknown' keyword
        else:
            df[cols] = df[cols].fillna(df[cols].mean())     #fills empty numerical values with 'mean' of column 

    return df





    