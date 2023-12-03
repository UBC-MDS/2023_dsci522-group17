# Predicting Athletic Potential of FIFA Athletes

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

## Report
The final report can be found
[here](https://ubc-mds.github.io/fifa-potential/high-potential-fifa-prediction-report.html)

## Dependencies

- [Docker](https://www.docker.com/) is a container used 
to manage the software dependencies for this project.
The Docker image used for this project is based on the
`quay.io/jupyter/minimal-notebook` image.
Additional dependencies are specified in the [Dockerfile](Dockerfile).
- Pythonic dependencies are described in the [environment.yaml](environment.yaml)

## Usage

### Setup

1. [Install](https://www.docker.com/get-started/) 
and launch Docker on your computer.

2. Clone this GitHub repository.

### Running the analysis using Docker Compose

1. Navigate to the root of this project on your computer using the
   command line and enter the following command:

``` 
docker compose up
```

2. In the terminal, look for a URL that starts with 
`http://127.0.0.1:8888/lab?token=` 
Copy and paste that URL into your browser.

3. To replicate the analysis, open a terminal window within Jupyter Lab and run: 

```bash
conda activate fifa-potential
bash run.sh
```

3. To view the analysis, run the following in the root directory to rebuild the report and copy it to the `docs/` directory.
```
jupyter-book build --all report
yes | cp -r -f report/_build/html/* docs
```


#### Clean up

1. To shut down the container and clean up the resources, 
press `Ctrl` + `C` in the terminal
where you launched the container, and then type 
```
docker compose rm
```

### Running the analysis locally 

1. Install local dependencies
2. To replicate the analysis, navigate to the root of this project on your computer using the command line and enter the following commands:

```bash
conda activate fifa-potential
bash run.sh
```

3. To view the analysis, run the following in the root directory to rebuild the report and copy it to the `docs/` directory.
```
jupyter-book build --all report
yes |  cp -r -f report/_build/html/* docs
```


#### Clean up
1. To remove all modified files, execute `git restore .` at the root of the repository to revert all local changes to the repository

## Developer notes

### Adding a new dependency

1. Add the dependency to the `Dockerfile` file on a new branch.

2. Re-build the Docker image locally to ensure it builds and runs properly.

3. Push the changes to GitHub. A new Docker
   image will be built and pushed to Docker Hub automatically.
   It will be tagged with the SHA for the commit that changed the file.

4. Update the `docker-compose.yml` file on your branch to use the new
   container image (make sure to update the tag specifically).

5. Send a pull request to merge the changes into the `main` branch. 

### Running the tests
Tests are run using the `pytest` command in the root of the project.
More details about the test suite can be found in the 
[`tests`](tests) directory.

### Building the report
Run the following in the root directory to build the report and copy it to the `docs/` directory.
```
jupyter-book build --all report
y |  cp -r -f report/_build/html/* docs
```
Note that this will not rerun the analysis itself, simply update the rendered report. 

### Calling individual scripts
Refer to [run.sh](run.sh) for execution order. Commands and recommended parameters are listed below as required for Milestone 3: 

```bash
# Load, clean, and tidy data 
python src/01_load_clean_tidy.py \
    --url=https://sports-statistics.com/database/fifa/fifa_2022_datasets.zip \
    --filename=players_22.csv

# Generate EDA figures
python src/02_eda_figures.py \
    --dataset=data/processed/fifa_train.csv \
    --target=potential

# Preprocess data 
python src/03_preprocessing.py \
    --train=data/processed/fifa_train.csv \
    --test=data/processed/fifa_test.csv

# Complete model selection 
python src/04_model_selection.py \
    --scaled_train=data/processed/scaled_fifa_train.csv

# Complete hyperparameter tuning
python src/05_hyperparameter_scoring.py \
    --scaled_train=data/processed/scaled_fifa_train.csv \
    --scaled_test=data/processed/scaled_fifa_test.csv
```

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
