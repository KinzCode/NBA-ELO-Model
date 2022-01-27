# :basketball: **NBA ELO MODEL** :basketball:

## **Contributors** :black_nib:
:star: Ben McKinnon
:star: Daniel Braun

## **Table Of Contents** :books:
* [General info](#general-info)
* [Technologies](#technologies)
* [Data sources](#data-sources)
* [Use](#use)

## **General** :page_with_curl:
### Overview :speech_balloon:

This repository holds the codebase for an ELO model applied to the National Basketball Association (NBA). This is a predictive model that can be made by someone with no to very little knowledge of more advanced statistical/ machine learning modelling practices. Further, it is essential to note that the predictions generated by this model **must not be used for gambling purposes**. Market setters of NBA odds use more advanced modelling techniques that capture more variance of the game, which this basic technique fails to do. Anyone who fails to adhere to this advice does so at their own risk.

### Logic :sunglasses:
All teams are assigned an initial score of 1500, which is the convention of what score new players receive within the traditional chess ELO system. Then, a prediction is made for the home team using the formula: 

<img src="https://latex.codecogs.com/svg.image?&space;E_{A}&space;=&space;&space;\frac{1}{\&space;1&space;&plus;&space;10&space;^&space;\frac{(R_{B}&space;-&space;R_{A})}{400}&space;" title=" E_{A} = \frac{1}{\ 1 + 10 ^ \frac{(R_{B} - R_{A})}{400} " />

Where :
* <img src="https://latex.codecogs.com/svg.image?&space;R_{A}" title=" R_{A}" /> = The home team's current rating.
* <img src="https://latex.codecogs.com/svg.image?&space;R_{B}" title=" R_{B}" /> = The away team's current rating.

Ratings are then adjusted using the formula:

<img src="https://latex.codecogs.com/svg.image?&space;R'&space;_{A}&space;=&space;&space;R_{A}&space;&plus;&space;K&space;(S_{A}&space;-&space;E_{A})" title=" R' _{A} = R_{A} + K (S_{A} - E_{A})" />

Where :
* <img src="https://latex.codecogs.com/svg.image?&space;R_{A}" title=" R_{A}" /> = The home team's current rating.
* <img src="https://latex.codecogs.com/svg.image?&space;{K}" title="K}" /> = The rate to which elo ratings change to new game results. This value is interchangable and can be changed in elo.py but has been set as 10 as a default. Making this value to large means the ratings will jump around to much where as making it to small will mean the elo will take to long to account for important changes.
* <img src="https://latex.codecogs.com/svg.image?&space;S_{A}" title=" S_{A}" /> = The match result. Will either be 1 representing win or 0 representing a loss.
* <img src="https://latex.codecogs.com/svg.image?&space;E_{A}" title=" E_{A}" /> = The pre game prediction.

## **Technologies** :computer: 
Project is created with:
  * Python 3.7.8
  * Pandas 1.0.3
  * Numpy 1.19.4

## **Data sources** :open_file_folder:
The data used in this repository was kindly provided by https://www.kaggle.com/nathanlauga/nba-games

## Use :shipit:
1. Clone this repository
2. Execute merge.py
3. Execute clean.py
4. Execute elo.py
5. View elo_preds.csv in dat/clean

## Structure :microscope:
    ├── dat   		       <- Folder containing raw and clean folders.
        ├── raw		      <- Folder containing the raw origonal csv files.
        ├── clean    	 <- Folder containing the cleaned csv files generated by merge.py & clean.py.
    ├── src    		      <- The folder containing scripts that merge, clean, and turn the raw data into predictions.
        ├── merge.py   <- The script that merges the appropriate csv files.
        ├── clean.py 	 <- The script that cleans the df in prepartion for ELO by removing unneccesary rows, handling missing data etc.
        ├── elo.py  		 <- The script that holds the ELO logic and creates the predictions.
    └── README.md      <- The file providing an overview of the repository and codebase.

