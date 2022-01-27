# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:16:42 2022

@author: KinzCode
"""

import numpy as np
import pandas as pd


class ELO(object):
    def __init__(self, original_fighters):
        self.elo = {i: 1600 for i in original_fighters}
        self.elo1_vals = []
        self.elo2_vals = []
        self.preds = []

    def calculate_pred(self, elo1, elo2):
        elo_difference = (elo2 - elo1) / 400
        pred = 1 / (1 + (10 ** elo_difference))
        return pred
        
    def run_elo(self, row, k, n):
        elo1 = self.elo[row['Home_Team']]
        elo2 = self.elo[row['Away_Team']]
        
        pred = self.calculate_pred(elo1, elo2)
        elo_residual = k * (row['Home_Team_Winner'] - pred)
        
        self.elo[row['Home_Team']] += elo_residual
        self.elo[row['Away_Team']] -= elo_residual
        
        self.elo1_vals.append(elo1)
        self.elo2_vals.append(elo2)
        
        self.preds.append(pred)
        
        
if __name__ == '__main__':
    # read in clean df
    df = pd.read_csv('../dat/clean/cleaned_games.csv')
    
    # create list of all teams
    original_teams =  list(df['Home_Team'].unique())
        
    # instantiate elo
    e = ELO(original_teams)
    
    # apply elo logic to df
    df.apply(e.run_elo, args=(10, 1600), axis=1)

    df['eloPred'] = e.preds
    df['elo1'] = e.elo1_vals
    df['elo2'] = e.elo2_vals
    
    team_rankings = e.elo
    
