# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:16:42 2022

@author: KinzCode
"""

import numpy as np
import pandas as pd


class ELO(object):
    """
    Class that represents a ELO object. 

    Attributes
    ----------
    elo : DICT
        A dict containing the ELO values for each team.
    home_vals : List
        A list containing all the home elo values.
    away_vals: List
        A list containing all the away elo values.
    preds: List
        A list containing all the calculated predictions for the home teams.
        Note the away team can just be calculated by 1 - home team pred.
    """
    def __init__(self, original_fighters):
        self.elo = {i: 1600 for i in original_fighters}
        self.home_vals = []
        self.away_vals = []
        self.preds = []

    def calculate_pred(self, elo1, elo2):
        """
        Parameters
        ----------
        elo1 : Float
            The home team elo value.
        elo2 : Float
            The away team elo value.
        Returns
        -------
        pred : Float
            The prediction of the home teams probability of winning. Pred is 
            expressed as a decimal between 0.0 - 1.0. E.g. pred of 0.65
            represents the home team has a predicted 65% chance to win.

        """
        elo_difference = (elo2 - elo1) / 400
        pred = 1 / (1 + (10 ** elo_difference))
        return pred
        
    def run_elo(self, row, k):
        """
        Parameters
        ----------
        row : DF
            Each row of the DF represents 1 unique game.
        k : INT
            The K value that determines how small or large a rating can change
            for each game.

        Returns
        -------
        None.

        """
        # get elo rankings
        home_elo = self.elo[row['Home_Team']]
        away_elo = self.elo[row['Away_Team']]
        # calculate predictions
        pred = self.calculate_pred(home_elo, away_elo)
        # calculate elo residual
        elo_residual = k * (row['Home_Team_Winner'] - pred)
        # update elo rankins
        self.elo[row['Home_Team']] += elo_residual
        self.elo[row['Away_Team']] -= elo_residual
        #append elo values to list
        self.home_vals.append(home_elo)
        self.away_vals.append(away_elo)
        # append pred to preds list
        self.preds.append(pred)
        
    
if __name__ == '__main__':
    # read in clean df
    df = pd.read_csv('../dat/clean/cleaned_games.csv')
    # create list of all teams
    original_teams =  list(df['Home_Team'].unique())
    # instantiate elo
    e = ELO(original_teams)
    # apply elo logic to df
    df.apply(e.run_elo, k = 10, axis=1)
    # add preds and elo values to df
    df['eloPred'] = e.preds
    df['elo1'] = e.home_vals
    df['elo2'] = e.away_vals
    # get team rankings
    team_rankings = e.elo
    # save df with predictions to csv
    df.to_csv('../dat/clean/elo_preds.csv', index = False)
    
