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
