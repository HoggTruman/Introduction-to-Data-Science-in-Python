import pandas as pd
import numpy as np
import scipy.stats as stats
import re

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

def mlb_correlation():
    # read in
    mlb_df = pd.read_csv("mlb.csv")
    cities = pd.read_html("wikipedia_data.html")[1]
    cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]

    # keep necessary columns
    cities = cities[['Metropolitan area', 'Population (2016 est.)[8]', 'MLB']]
    mlb_df = mlb_df[mlb_df['year'] == 2018]
    mlb_df = mlb_df[['team', 'W', 'L']]

    # clean out garbage from team names
    # mlb_df['team'] = mlb_df['team'].str.replace(r'[^a-z]*$', '', regex=True)
    cities['MLB'] = cities['MLB'].str.replace(r'\[.*\]', '', regex=True)

    # create a column for just team names
    mlb_df['team'].replace({'Chicago White Sox': 'wSox'}, inplace=True)
    mlb_df['team_only'] = mlb_df['team'].apply(lambda x: x.split()[-1])
    mlb_df['team_only'].replace({'Jays': 'Blue Jays', 'Sox': 'Red Sox',
                                 'Yankees': 'YankeesMets', 'Mets': 'YankeesMets',
                                 'Dodgers': 'DodgersAngels', 'Angels': 'DodgersAngels',
                                 'Giants': 'GiantsAthletics', 'Athletics': 'GiantsAthletics',
                                 'Cubs': 'CubsWhite Sox', 'wSox': 'CubsWhite Sox'
                                 }, inplace=True)

    # rename cities columns
    cities.rename(columns={'Metropolitan area': 'city', 'Population (2016 est.)[8]': 'population', 'MLB': 'team_only'},
                  inplace=True)

    # remove unnecessary rows and convert W/L + population to float
    # nba_df = nba_df[~nba_df['W'].str.contains('Division')]
    mlb_df['W'] = mlb_df['W'].apply(lambda x: float(x))
    mlb_df['L'] = mlb_df['L'].apply(lambda x: float(x))
    cities['population'] = cities['population'].apply(lambda x: float(x))

    # group by team_only
    mlb_df = mlb_df.groupby(by='team_only')['W', 'L'].mean()
    mlb_df.reset_index(inplace=True)


    # merge the two
    mdf = pd.merge(mlb_df, cities, how="inner", on="team_only")

    # create win loss column
    mdf['win/loss'] = mdf['W']/(mdf['W']+mdf['L'])


    # carry out analysis
    population_by_region = [x for x in mdf['population']]  # pass in metropolitan area population from cities
    win_loss_by_region = [x for x in mdf['win/loss']]  # pass in win/loss ratio from nhl_df in the same order as cities["Metropolitan area"]
    assert len(population_by_region) == len(win_loss_by_region), "Q3: Your lists must be the same length"
    assert len(population_by_region) == 26, "Q3: There should be 26 teams being analysed for MLB"
    return stats.pearsonr(population_by_region, win_loss_by_region)[0]


if __name__ == "__main__":
    print(mlb_correlation())
