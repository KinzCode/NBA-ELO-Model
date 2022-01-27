# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 14:02:18 2022

@author: KinzCode
"""

import pandas as pd

def map_team_names(games, teams):
    """
    Parameters
    ----------
    games : DF
        The df where each row represents a unique NBA game. DF contains attributes
        such as date, home/visitor team ID, scores etc.
    teams : DF
        The df containing the team ID and the respetive information associated to
        that ID. This includes : city, mascot etc.
    Returns
    -------
    mapped_games : DF
        The games df with the respective team names mapped to the team ID.

    """
    teams['TEAM_NAME'] = teams['CITY'] + " " + teams['NICKNAME']
    team_id_dict = dict(zip(teams['TEAM_ID'], teams['TEAM_NAME']))
    games['HOME_TEAM_ID'] = games['HOME_TEAM_ID'].map(team_id_dict)
    games['VISITOR_TEAM_ID'] = games['VISITOR_TEAM_ID'].map(team_id_dict)
    return games

def merge_data(games, teams):
    """
    Parameters
    ----------
    games : DF
        The df where each row represents a unique NBA game. DF contains attributes
        such as date, home/visitor team ID, scores etc.
    teams : DF
        The df containing the team ID and the respetive information associated to
        that ID. This includes : city, mascot etc.

    Returns
    -------
    mapped_games : DF
        The games df with the respective team names mapped to the team ID.

    """
    mapped_games = map_team_names(games, teams)
    return mapped_games


if __name__ == '__main__':
    teams = pd.read_csv('../dat/raw/teams.csv')
    games = pd.read_csv('../dat/raw/games.csv')
    
    # start merging
    mapped_games = merge_data(games, teams)
    
    # save merged csv
    mapped_games.to_csv('../dat/clean/mapped_games.csv', index = False)