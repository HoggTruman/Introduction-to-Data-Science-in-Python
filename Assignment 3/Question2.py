import numpy as np
import pandas as pd
import re


def answer_two():
    # Energy
    Energy = pd.read_excel('Energy Indicators.xls', usecols=[2, 3, 4, 5])
    Energy = Energy[17:244].rename(columns={'Unnamed: 2': 'Country',
                                            'Unnamed: 3': 'Energy Supply',
                                            'Unnamed: 4': 'Energy Supply per Capita',
                                            'Unnamed: 5': '% Renewable'
                                            })
    Energy = Energy.replace('...', np.NAN)
    Energy['Country'] = Energy['Country'].apply(lambda x: re.findall(r"^[^(0-9]*[a-z]", x)[0])
    Energy = Energy.replace({"Republic of Korea": "South Korea",
                             "United States of America": "United States",
                             "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                             "China, Hong Kong Special Administrative Region": "Hong Kong"
                             })
    Energy['Energy Supply'] *= 1000000

    # GDP
    GDP = pd.read_csv('world_bank.csv', skiprows=range(4)).rename(columns={'Country Name': 'Country'})
    GDP['Country'] = GDP['Country'].replace({"Korea, Rep.": "South Korea",
                                             "Iran, Islamic Rep.": "Iran",
                                             "Hong Kong SAR, China": "Hong Kong"})
    GDP = GDP[['Country'] + [str(x) for x in range(2006, 2016)]]

    # ScimEn
    ScimEn = pd.read_excel('scimagojr-3.xlsx')

    # Merge Data Frames
    df_intersect = ScimEn.merge(Energy, on='Country').merge(GDP, on='Country')
    df_union = ScimEn.merge(Energy, left_on='Country', right_on='Country', how='outer').merge(GDP, left_on='Country',
                                                                                              right_on='Country',
                                                                                              how='outer')

    return len(df_union) - len(df_intersect)


if __name__ == "__main__":
    df = answer_two()
