# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 12:16:14 2022

@author: KinzCode
"""

import pandas as pd


def drop_columns(mapped_games):
    """
    Parameters
    ----------
    mapped_games : DF.

    Returns
    -------
    mapped_games : DF
        Removes unwanted/ unneeded columns for model.

    """
    keeps = ['GAME_DATE_EST', 'HOME_TEAM_ID','VISITOR_TEAM_ID',
             'PTS_home', 'PTS_away', 'HOME_TEAM_WINS', 'SEASON']
    mapped_games = mapped_games[keeps]
    return mapped_games

def rename_columns(mapped_games):
    """
    Parameters
    ----------
    mapped_games : DF.

    Returns
    -------
    mapped_games : DF
        Renames columns in DF to cleaner spelling and more intuitive names.

    """
    mapped_games.rename(columns = {'GAME_DATE_EST': 'Date',
                                   'HOME_TEAM_ID':'Home_Team',
                                   'VISITOR_TEAM_ID': 'Away_Team',
                                   'PTS_home':'Home_Score',
                                   'PTS_away': 'Away_Score',
                                   'HOME_TEAM_WINS': 'Home_Team_Winner',
                                   'SEASON': 'Season'}, 
                        inplace = True)
    return mapped_games

def order_data(mapped_games):
    mapped_games.sort_values(by = ['Season', 'Date'], inplace = True)
    return mapped_games

def delete_missing(mapped_games):
    """
    Parameters
    ----------
    mapped_games : DF

    Returns
    -------
    mapped_games : DF
        Returns DF with no missing values. Any row with NAN is dropped.
    """
    mapped_games.dropna(inplace = True)
    return mapped_games

def clean_data(mapped_games):
    """
    Parameters
    ----------
    mapped_games : DF
        Base DF where each row represnts 1 NBA game. DF contains teams, scores,
        dates etc.

    Returns
    -------
    mapped_games : DF
        The cleaned DF only containing the data needed for the ELO model.
    """
    mapped_games = drop_columns(mapped_games)
    mapped_games = rename_columns(mapped_games)
    mapped_games = delete_missing(mapped_games)
    mapped_games = order_data(mapped_games)
    return mapped_games


if __name__ == '__main__':
    mapped_games= pd.read_csv('../dat/clean/mapped_games.csv')
    
    # clean data
    cleaned_games = clean_data(mapped_games)
    
    # save cleaned data to csv
    cleaned_games.to_csv('../dat/clean/cleaned_games.csv', index = False)