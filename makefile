# Makefile to rerun analyses for fifa-potential
# rerun analyses using `make all` in the root directory

# run all analyses
all : report/_build/html/index.html

# Downloading, unzipping, extracting and splitting data into test and train datasets
data/processed/fifa_test.csv data/processed/fifa_train.csv data/raw/players_22.csv : scripts/01_load_clean_tidy.py
		python scripts/01_load_clean_tidy.py \
			--url=https://sports-statistics.com/database/fifa/fifa_2022_datasets.zip \
			--filename=players_22.csv

# Creating EDA plot
results/figures/eda_plots.png : scripts/02_eda_figures.py data/processed/fifa_train.csv
		python scripts/02_eda_figures.py \
			--dataset=data/processed/fifa_train.csv \
			--target=potential

# Preprocessing the data
data/processed/scaled_fifa_train.csv data/processed/scaled_fifa_test.csv : scripts/03_preprocessing.py data/processed/fifa_train.csv data/processed/fifa_test.csv
		python scripts/03_preprocessing.py \
			--train=data/processed/fifa_train.csv \
			--test=data/processed/fifa_test.csv

# Cross-Validation on multiple machine learning models
results/tables/model_cross_val_scores.csv:	scripts/04_model_selection.py data/processed/scaled_fifa_train.csv
		python scripts/04_model_selection.py \
			--scaled_train=data/processed/scaled_fifa_train.csv

# Hyperparameter Optimization and Testing model on test data
results/tables/hyperparameter_rankings.csv results/tables/test_score.csv results/models/best_model.pickle : scripts/05_hyperparameter_scoring.py data/processed/scaled_fifa_train.csv data/processed/scaled_fifa_test.csv
		python scripts/05_hyperparameter_scoring.py \
			--scaled_train=data/processed/scaled_fifa_train.csv \
			--scaled_test=data/processed/scaled_fifa_test.csv

# Render the html report 
report/_build/html/index.html : report/high-potential-fifa-prediction-report.ipynb results/tables/model_cross_val_scores.csv results/tables/hyperparameter_rankings.csv results/tables/test_score.csv results/figures/eda_plots.png
		jupyter-book build --all report
		cp -rf report/_build/html/* docs
		if [ ! -f ".nojekyll" ]; then touch docs/.nojekyll; fi 
		# above line referenced from https://github.com/ttimbers/breast_cancer_predictor_py/blob/main/Makefile

# clean repository
clean:
		rm -rf report/_build docs/*
		rm -f data/processed/fifa_train.csv \
			data/processed/fifa_test.csv \
			data/processed/scaled_fifa_train.csv \
			data/processed/scaled_fifa_test.csv
		rm -f results/figures/eda_plots.png
		rm -f results/models/best_model.pickle
		rm -f results/tables/model_cross_val_scores.csv \
			results/tables/hyperparameter_rankings.csv \
			results/tables/test_score.csv

