# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 12:16:14 2022

@author: KinzCode
"""

import pandas as pd


def drop_columns(mapped_games):
    keeps = ['GAME_DATE_EST', 'HOME_TEAM_ID','VISITOR_TEAM_ID',
             'PTS_home', 'PTS_away', 'HOME_TEAM_WINS', 'SEASON']
    mapped_games = mapped_games[keeps]
    return mapped_games

def rename_columns(mapped_games):
    mapped_games.rename(columns = {'GAME_DATE_EST': 'Date',
                                   'HOME_TEAM_ID':'Home_Team',
                                   'VISITOR_TEAM_ID': 'Away_Team',
                                   'PTS_home':'Home_Score',
                                   'PTS_away': 'Away_Score',
                                   'HOME_TEAM_WINS': 'Home_Team_Winer',
                                   'SEASON': 'Season'}, 
                        inplace = True)
    return mapped_games

def order_data(mapped_games):
    mapped_games.sort_values(by = ['Season', 'Date'], inplace = True)
    return mapped_games

def delete_missing(mapped_games):
    return

def clean_data(mapped_games):
    mapped_games = drop_columns(mapped_games)
    mapped_games = rename_columns(mapped_games)
    mapped_games = order_data(mapped_games)
    return mapped_games


if __name__ == '__main__':
    mapped_games= pd.read_csv('../dat/clean/mapped_games.csv')
    
    # clean data
    cleaned_games = clean_data(mapped_games)
