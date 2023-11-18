#### Analysis write-up

## Predicting FIFA22 player potential from player traits and skill attributes
by Simon Frew, Waleed Mahmood, Merete Lutz & Jake Barnabe
2023/11/15

### Summary

We attempt to construct a classification model using an RBF SVM classifier algorithm which uses FIFA22 player attribute ratings to classify players' potential with target categories "Low", "Medium", "Good", and "Great". The categories are split on the quartiles of the distribution of the FIFA22 potential ratings.

  

### Introduction

One of the most challenging jobs for sports coaches is deciding which players will make a positive addition to the team (US National Soccer Players, 2023). A key step in evaluating which players to add to a team is predicting how their skill level will change over time. We can think of this in terms of their potential. FIFA22 by EA sports is the world's leading soccer video game. For each year's release, they rate players' skill levels in various aspects of the game such as shooting, passing, defending, etc. and give each player an overall rating as well as a rating of each player's potential. 

Here we ask if we can use a machine learning model to classify players by their potential given their attributes. Answering this question is important as developing a model that can accurately predict the potential of players on FIFA22 could then be applied to the evaluation of soccer players in real life and be employed by coaches and scouts to help soccer clubs make good decisions on which players to add to the team and which to let go.     


## Methods
### Data
The data used in this analysis are from the video game FIFA22 by EA Sports. 
The data were downloaded with authentication from [Kaggle](https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset) and without authentication from [Sports-Statistics.com](https://sports-statistics.com/sports-data/fifa-2022-dataset-csvs/). 
Within documentation, these were were scraped from a publically available website (https://sofifa.com/) with a permissive `robots.txt`. 


Each row of the dataset corresponds to a single player, and contains biometric information, ratings for various skills, like shooting accuracy, passing, dribbling, and player wages. 


### Analysis


### Results & Discussion


#### References
https://ussoccerplayers.com/soccer-training-tips/evaluating-players (US National Soccer Players, 2023)

