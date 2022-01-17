import pandas as pd
import numpy as np
import scipy.stats as stats
import re

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

def nhl_correlation():
    # read in
    nhl_df = pd.read_csv("nhl.csv")
    cities = pd.read_html("wikipedia_data.html")[1]
    cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]

    # keep necessary columns
    cities = cities[['Metropolitan area', 'Population (2016 est.)[8]', 'NHL']]
    nhl_df = nhl_df[nhl_df['year'] == 2018]
    nhl_df = nhl_df[['team', 'W', 'L']]

    # clean out garbage from team names
    nhl_df['team'] = nhl_df['team'].apply(lambda x: x if x[-1] != '*' else x[:-1])
    cities['NHL'] = cities['NHL'].str.replace(r'\[.*\]', '', regex=True)

    # create a column for just team names
    nhl_df['team_only'] = nhl_df['team'].apply(lambda x: x.split()[-1])
    nhl_df['team_only'].replace({'Leafs': 'Maple Leafs', 'Wings': 'Red Wings', 'Jackets': 'Blue Jackets', 'Knights': 'Golden Knights',
                                 'Rangers': 'RangersIslandersDevils', 'Islanders': 'RangersIslandersDevils', 'Devils': 'RangersIslandersDevils',
                                 'Kings': 'KingsDucks', 'Ducks': 'KingsDucks'
                                 }, inplace=True)

    # rename cities columns
    cities.rename(columns={'Metropolitan area': 'city', 'Population (2016 est.)[8]': 'population', 'NHL': 'team_only'},
                  inplace=True)

    # remove unnecessary rows and convert W/L to float
    nhl_df = nhl_df[~nhl_df['W'].str.contains('Division')]
    nhl_df['W'] = nhl_df['W'].apply(lambda x: float(x))
    nhl_df['L'] = nhl_df['L'].apply(lambda x: float(x))
    cities['population'] = cities['population'].apply(lambda x: float(x))

    # group by team_only
    nhl_df = nhl_df.groupby(by='team_only')['W', 'L'].mean()
    nhl_df.reset_index(inplace=True)


    # merge the two
    mdf = pd.merge(nhl_df, cities, how="inner", on="team_only")

    # create win loss column
    mdf['win/loss'] = mdf['W']/(mdf['W']+mdf['L'])


    population_by_region = [x for x in mdf['population']]  # pass in metropolitan area population from cities
    win_loss_by_region = [x for x in mdf['win/loss']]  # pass in win/loss ratio from nhl_df in the same order as cities["Metropolitan area"]
    # assert len(population_by_region) == len(win_loss_by_region), "Q1: Your lists must be the same length"
    # assert len(population_by_region) == 28, "Q1: There should be 28 teams being analysed for NHL"
    return stats.pearsonr(population_by_region, win_loss_by_region)[0]


if __name__ == "__main__":
    print(nhl_correlation())
