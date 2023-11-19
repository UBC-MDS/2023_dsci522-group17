#### Analysis write-up

## Predicting FIFA22 player potential from player traits and skill attributes
by Simon Frew, Waleed Mahmood, Merete Lutz & Jake Barnabe
2023/11/15

### Summary

We attempt to construct a classification model using an RBF SVM classifier algorithm which uses FIFA22 player attribute ratings to classify players' potential with target classes "Low", "Medium", "Good", and "Great". The classes are split on the quartiles of the distribution of the FIFA22 potential ratings. Our model performed reasonably well on the test data with an accuracy score of 0.84, with hyperparamters C: 100 & Gamma: 0.01. However, we believe there is still significant room for improvement before the model is ready to be utilized by soccer clubs and coaching staffs to predict the potential of players on the field instead of on the screen. 

  

### Introduction

One of the most challenging jobs for sports coaches is deciding which players will make a positive addition to the team (US National Soccer Players, 2023). A key step in evaluating which players to add to a team is predicting how their skill level will change over time. We can think of this in terms of their potential. FIFA22 by EA sports is the world's leading soccer video game. For each year's release, they rate players' skill levels in various aspects of the game such as shooting, passing, defending, etc. and give each player an overall rating as well as a rating of each player's potential. 

Here we ask if we can use a machine learning model to classify players by their potential given their attribute ratings. Answering this question is important as developing a model that can accurately predict the potential of players on FIFA22 could then be applied to the evaluation of soccer players in real life and be employed by coaches and scouts to help soccer clubs make good decisions on which players to add to the team and which to let go.     


## Methods
### Data
The data used in this analysis are from the video game FIFA22 by EA Sports. 
The data were downloaded with authentication from [Kaggle](https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset) and without authentication from [Sports-Statistics.com](https://sports-statistics.com/sports-data/fifa-2022-dataset-csvs/). 
Within documentation, these were were scraped from a publicly available website (https://sofifa.com/) with a permissive `robots.txt`. 


Each row of the dataset corresponds to a single player, and contains biometric information, ratings for various skills, like shooting accuracy, passing, dribbling, and player wages. 


### Analysis
The Radial Basis Function (RBF) Support Vector Machine (SVM) RBF SVM model was used to build a classification model to predict whether a player has high potential or not (found in the potential column of the data set). The variables included in our model were selected from the list of different player statistics that are part of the dataset, including the statistics on their `speed`, `dribbling`, `shooting` etc. These are the variables that were used as features to fit the model. The hyperparameters `gamma` and `C` were chosen through the use of the automated optimization method from `scikit-learn` called `RandomizedSearchCV`. The Python programming language (Van Rossum and Drake 2009) was used and the following Python packages were used to perform the analysis: Numpy (Harris et al. 2020), Pandas (McKinney 2010), altair (VanderPlas et al., 2018), SkLearn (Pedregosa et al. 2011) and SciPy (Pauli Virtanen, et al., 2020). The code used to perform the analysis and create this report can be found here: <https://github.com/UBC-MDS/2023_dsci522-group17/>.

### Results and Discussion
To look at whether each of the predictors might be useful to predict the class of the target variable `potential`, we plotted the distributions of each predictor from the training data set and coloured the distribution by class (Low: blue, medium: orange, Good: red, Great: green). These distributions are drawn up after we have scaled all of the features in the training dataset. In doing this, we can see that most of the distributions, for the features we have filtered to keep, have overlap but their spreads and centers are different, except for `height_cm` and `weight_kg` - which overlap almost completely across the different classes of `potential` - and `value_eur` - which has no distribution for classes other than `great` for `potential` - so we omit them from our model.

Through our model selection process, we were able to determine that the best model in our case would be an RBF SVM model. To determine the values for the hyperparameters that would give us the best estimator, we used the hyperparameter optimization method `RandomizedSearchCV` to perform a 5-fold cross validation, so that we are able to get the most suitable hyperparamters to obtain the best possible model to estimate and predict the class for `potential`. 

We observe that the optimal hyperparameter values are `C: 100` and `Gamma: 0.01`. The training accuracy obtained with these `hyperparameters` is 0.786. And the accuracy of our model is 0.84, i.e. it predicted quite well when run on the test data. 

### Further Improvements
To improve our model further in the future, with the hopes of better predicting the potential of a player, there are a few improvements that can be made. First of all, we could include the growth of a player over the years, based on their performance in games. This would somewhat lead to us having a time-series dataset which we can use to create a feature that captures the growth of a player over the years. Second, we would include the effort that the player puts into their training. This can be a beneficial improvement that could lead to better predictive power in our model. Finally, we could include the reporting of the probability estimates of the prediction of the classes in for the `potential` of a player, so that a player scout knows with how much certainty a player might be classified as a `Great` player (for example).




#### References
https://ussoccerplayers.com/soccer-training-tips/evaluating-players (US National Soccer Players, 2023)

Harris, C.R. et al., 2020. Array programming with NumPy. Nature, 585, pp.357–362.

McKinney, Wes. 2010. “Data Structures for Statistical Computing in Python.” In Proceedings of the 9th Python in Science Conference, edited by Stéfan van der Walt and Jarrod Millman, 51–56.

Pauli Virtanen, et al., and SciPy 1.0 Contributors. (2020) SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. Nature Methods, 17(3), 261-272.

Pedregosa, F. et al., 2011. Scikit-learn: Machine learning in Python. Journal of machine learning research, 12(Oct), pp.2825–2830.

VanderPlas et al., (2018). Altair: Interactive Statistical Visualizations for Python. Journal of Open Source Software, 3(32), 1057, https://doi.org/10.21105/joss.01057

Van Rossum, Guido, and Fred L. Drake. 2009. Python 3 Reference Manual. Scotts Valley, CA: CreateSpace.

