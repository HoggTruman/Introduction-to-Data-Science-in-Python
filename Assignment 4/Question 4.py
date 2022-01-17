import pandas as pd
import numpy as np
import scipy.stats as stats
import re

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

def nfl_correlation():
    # read in
    nfl_df = pd.read_csv("nfl.csv")
    cities = pd.read_html("wikipedia_data.html")[1]
    cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]

    # keep necessary columns
    cities = cities[['Metropolitan area', 'Population (2016 est.)[8]', 'NFL']]
    nfl_df = nfl_df[nfl_df['year'] == 2018]
    nfl_df = nfl_df[['team', 'W', 'L']]
    nfl_df = nfl_df[~nfl_df['W'].str.contains('AFC|NFC', regex=True)]

    # clean out garbage from team names
    nfl_df['team'] = nfl_df['team'].str.replace(r'[*+]', '', regex=True)
    cities['NFL'] = cities['NFL'].str.replace(r'\[.*\]', '', regex=True)

    # create a column for just team names
    nfl_df['team_only'] = nfl_df['team'].apply(lambda x: x.split()[-1])
    nfl_df['team_only'].replace({'Giants': 'GiantsJets', 'Jets': 'GiantsJets',
                                 'Rams': 'RamsChargers', 'Chargers': 'RamsChargers',
                                 '49ers': '49ersRaiders', 'Raiders': '49ersRaiders',
                                 }, inplace=True)

    # rename cities columns
    cities.rename(columns={'Metropolitan area': 'city', 'Population (2016 est.)[8]': 'population', 'NFL': 'team_only'},
                  inplace=True)

    # convert W/L + population to float
    nfl_df['W'] = nfl_df['W'].apply(lambda x: float(x))
    nfl_df['L'] = nfl_df['L'].apply(lambda x: float(x))
    cities['population'] = cities['population'].apply(lambda x: float(x))

    # group by team_only
    nfl_df = nfl_df.groupby(by='team_only')['W', 'L'].mean()
    nfl_df.reset_index(inplace=True)


    # merge the two
    mdf = pd.merge(nfl_df, cities, how="inner", on="team_only")

    # create win loss column
    mdf['win/loss'] = mdf['W']/(mdf['W']+mdf['L'])


    # carry out analysis
    population_by_region = [x for x in mdf['population']]  # pass in metropolitan area population from cities
    win_loss_by_region = [x for x in mdf['win/loss']]  # pass in win/loss ratio from nhl_df in the same order as cities["Metropolitan area"]
    assert len(population_by_region) == len(win_loss_by_region), "Q4: Your lists must be the same length"
    assert len(population_by_region) == 29, "Q4: There should be 29 teams being analysed for NFL"
    return stats.pearsonr(population_by_region, win_loss_by_region)[0]


if __name__ == "__main__":
    print(nfl_correlation())
