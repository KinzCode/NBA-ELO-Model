# **NBA ELO MODEL**

## **Contributors**
Ben McKinnon & Daniel Braun

## **Table of contents**
* [General info](#general-info)
* [Technologies](#technologies)
* [Data sources](#data-sources)
* [Use](#use)

## **General**
This repository holds the codebase for an ELO model applied to the National Basketball Association(NBA). This is a predictive model that can be made by someone with no to very little knowledge of more advanced statistical/ machine learning modelling practices. Further, it is essential to note that the predictions generated by this model ** must not be used for gambling purposes** . Market setters of NBA odds use more advanced modelling techniques that capture more variance of the game, which this basic technique does. Anyone who fails to adhere to this advice does so at their own risk.

ELO is calculated by 

![img]http://www.sciweavers.org/tex2img.php?eq=%20E_%7BA%7D%20%3D%20%20%5Cfrac%7B1%7D%7B%5C%201%20%2B%2010%20%5E%20%5Cfrac%7B%28R_%7BA%7D%20-%20R_%7BB%7D%29%7D%7B400%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0[/img]

## **Technologies**
Project is created with:
  * Python 3.7.8
  * Pandas 1.0.3
  * Numpy 1.19.4

## **Data sources**
The data used in this repository was kindly provided by https://www.kaggle.com/nathanlauga/nba-games

## Use

## Structure
    ├── dat   		<- Folder containing raw and clean folders.
        ├── raw		<- Folder containing the raw origonal csv files.
        ├── clean    		<- Folder containing the cleaned csv files generated by merge.py & clean.py.
    ├── src    		<- The folder containing scripts that merge, clean, and turn the raw data into predictions.
        ├── merge.py    	<- The script that merges the appropriate csv files.
        ├── clean.py 		<- The script that cleans the df in prepartion for ELO by removing unneccesary rows, handling missing data etc.
        ├── elo.py  		<- The script that holds the ELO logic and creates the predictions.
    └── README.md     	<- The file providing an overview of the repository and codebase.

