# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 14:02:18 2022

@author: KinzCode
"""

import pandas as pd

def map_team_names(games, teams):
    teams['TEAM_NAME'] = teams['CITY'] + " " + teams['NICKNAME']
    team_id_dict = dict(zip(teams['TEAM_ID'], teams['TEAM_NAME']))
    games['HOME_TEAM_ID'] = games['HOME_TEAM_ID'].map(team_id_dict)
    games['VISITOR_TEAM_ID'] = games['VISITOR_TEAM_ID'].map(team_id_dict)
    return games

def merge_data(games, teams):
    mapped_games = map_team_names(games, teams)
    return mapped_games


if __name__ == '__main__':
    teams = pd.read_csv('../dat/raw/teams.csv')
    #rankings = pd.read_csv('../dat/ranking.csv')
    #players = pd.read_csv('../dat/players.csv')
    #games_details = pd.read_csv('../dat/games_details.csv')
    games = pd.read_csv('../dat/raw/games.csv')
    
    # start merging
    mapped_games = merge_data(games, teams)
    
    # save merged csv
    mapped_games.to_csv('../dat/clean/mapped_games.csv', index = False)