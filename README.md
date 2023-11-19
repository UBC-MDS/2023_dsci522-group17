# Predicting Athletic Potential of Youth Soccer Athletes

## Contributors:
- Jake Barnabe
- Simon Frew
- Merete Lutz
- Waleed Mahmood

## Summary
We attempt to construct a classification model using an RBF SVM classifier algorithm which uses FIFA22 player attribute ratings to classify players' potential with target classes "Low", "Medium", "Good", and "Great". 
The classes are split on the quartiles of the distribution of the FIFA22 potential ratings. 
Our model performed reasonably well on the test data with an accuracy score of 0.84, with hyperparamters C: 100 & Gamma: 0.01. 
However, we believe there is still significant room for improvement before the model is ready to be utilized by soccer clubs and coaching staffs to predict the potential of players on the field instead of on the screen. 

## Usage

If this is your first time running our project,
run the following from the root of this repository:

``` bash
conda env create --file environment.yml
```

To run the analysis, run the following from the root of this repository:

``` bash
conda activate fifa-potential
jupyter lab 
```

Open `high-potential-fifa-prediction-report.ipynb` in Jupyter Lab
and under the "Kernel" menu click "Restart Kernel and Run All Cells...".

## Dependencies

- `conda` (version 23.9.0 or higher)
- `nb_conda_kernels` (version 2.3.1 or higher)
- Python and packages listed in [`environment.yml`](environment.yml)


## Licenses
This report is licensed under a Attribution-NonCommercial-NoDerivs 4.0 International (CC BY-NC-ND 4.0 Deed) License with the repository itself under a MIT License. The underlying dataset is licensed by a CC0 1.0 Universal (Public Domain) license. 



## References
This README file references https://github.com/ttimbers/breast_cancer_predictor_py/tree/main. 

US National Soccer Players. (2023). (rep.). How to evaluate soccer players. Retrieved from https://ussoccerplayers.com/soccer-training-tips/evaluating-players. 

Harris, C.R. et al., 2020. Array programming with NumPy. Nature, 585, pp.357–362.

McKinney, Wes. 2010. “Data Structures for Statistical Computing in Python.” In Proceedings of the 9th Python in Science Conference, edited by Stéfan van der Walt and Jarrod Millman, 51–56.

Pauli Virtanen, et al., and SciPy 1.0 Contributors. (2020) SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. Nature Methods, 17(3), 261-272.

Pedregosa, F. et al., 2011. Scikit-learn: Machine learning in Python. Journal of machine learning research, 12(Oct), pp.2825–2830.

VanderPlas et al., (2018). Altair: Interactive Statistical Visualizations for Python. Journal of Open Source Software, 3(32), 1057, https://doi.org/10.21105/joss.01057

Van Rossum, Guido, and Fred L. Drake. 2009. Python 3 Reference Manual. Scotts Valley, CA: CreateSpace.