import pandas as pd
import numpy as np
import scipy.stats as stats
import re

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

def nba_correlation():
    # read in
    nba_df = pd.read_csv("nba.csv")
    cities = pd.read_html("wikipedia_data.html")[1]
    cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]

    # keep necessary columns
    cities = cities[['Metropolitan area', 'Population (2016 est.)[8]', 'NBA']]
    nba_df = nba_df[nba_df['year'] == 2018]
    nba_df = nba_df[['team', 'W', 'L']]

    # clean out garbage from team names
    nba_df['team'] = nba_df['team'].str.replace(r'[^a-z]*$', '', regex=True)
    cities['NBA'] = cities['NBA'].str.replace(r'\[.*\]', '', regex=True)

    # create a column for just team names
    nba_df['team_only'] = nba_df['team'].apply(lambda x: x.split()[-1])
    nba_df['team_only'].replace({'Blazers': 'Trail Blazers',
                                 'Knicks': 'KnicksNets', 'Nets': 'KnicksNets',
                                 'Lakers': 'LakersClippers', 'Clippers': 'LakersClippers',
                                 }, inplace=True)

    # rename cities columns
    cities.rename(columns={'Metropolitan area': 'city', 'Population (2016 est.)[8]': 'population', 'NBA': 'team_only'},
                  inplace=True)

    # remove unnecessary rows and convert W/L + population to float
    # nba_df = nba_df[~nba_df['W'].str.contains('Division')]
    nba_df['W'] = nba_df['W'].apply(lambda x: float(x))
    nba_df['L'] = nba_df['L'].apply(lambda x: float(x))
    cities['population'] = cities['population'].apply(lambda x: float(x))

    # group by team_only
    nba_df = nba_df.groupby(by='team_only')['W', 'L'].mean()
    nba_df.reset_index(inplace=True)


    # merge the two
    mdf = pd.merge(nba_df, cities, how="inner", on="team_only")

    # create win loss column
    mdf['win/loss'] = mdf['W']/(mdf['W']+mdf['L'])


    # carry out analysis
    population_by_region = [x for x in mdf['population']]  # pass in metropolitan area population from cities
    win_loss_by_region = [x for x in mdf['win/loss']]  # pass in win/loss ratio from nhl_df in the same order as cities["Metropolitan area"]
    assert len(population_by_region) == len(win_loss_by_region), "Q2: Your lists must be the same length"
    assert len(population_by_region) == 28, "Q2: There should be 28 teams being analysed for NBA"
    return stats.pearsonr(population_by_region, win_loss_by_region)[0]


if __name__ == "__main__":
    print(nba_correlation())
