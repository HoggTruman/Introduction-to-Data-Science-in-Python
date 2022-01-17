import pandas as pd
import numpy as np
import scipy.stats as stats
import re

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)


def nhl_():
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

    return mdf


def nba_():
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

    return mdf


def mlb_():
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

    return mdf


def nfl_():
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

    return mdf


def sports_team_performance():
    dfs = [nfl_(), nba_(), nhl_(), mlb_()]

    sports = ['NFL', 'NBA', 'NHL', 'MLB']
    p_values = pd.DataFrame({k: np.nan for k in sports}, index=sports)

    for x in range(len(dfs)):
        for y in range(len(dfs)):
            temp_df = pd.merge(dfs[x], dfs[y], on="city", how="inner")
            p_values.iat[x, y] = stats.ttest_rel(temp_df['win/loss_x'], temp_df['win/loss_y'])[1]

    assert abs(p_values.loc["NBA", "NHL"] - 0.02) <= 1e-2, "The NBA-NHL p-value should be around 0.02"
    assert abs(p_values.loc["MLB", "NFL"] - 0.80) <= 1e-2, "The MLB-NFL p-value should be around 0.80"
    return p_values


if __name__ == "__main__":
    print(sports_team_performance())
