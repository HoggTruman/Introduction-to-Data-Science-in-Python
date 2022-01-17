import pandas as pd


def proportion_of_education():
    df = pd.read_csv('NISPUF17.csv')
    mat_edu = {"less than high school": len(df[df['EDUC1'] == 1]) / len(df),
               "high school": len(df[df['EDUC1'] == 2]) / len(df),
               "more than high school but not college": len(df[df['EDUC1'] == 3]) / len(df),
               "college": len(df[df['EDUC1'] == 4]) / len(df)
               }
    return mat_edu


print(proportion_of_education())
