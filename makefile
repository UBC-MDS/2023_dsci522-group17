

# Downloading, unzipping, extracting and splitting data into test and train datasets
data/raw/players_22.csv : src/01_load_clean_tidy.py
	python src/01_load_clean_tidy.py \
    --url=https://sports-statistics.com/database/fifa/fifa_2022_datasets.zip \
    --filename=players_22.csv

# Creating EDA plot
results/eda_plots.png : src/02_eda_figures.py data/processed/fifa_train.csv
	python src/02_eda_figures.py \
	--dataset=data/processed/fifa_train.csv \
	--target=potential

# Preprocessing the data
scaled:	src/03_preprocessing.py data/processed/fifa_train.csv data/processed/fifa_test.csv
	python src/03_preprocessing.py \
    --train=data/processed/fifa_train.csv \
    --test=data/processed/fifa_test.csv

# Cross-Validation on multiple machine learning models
results/model_cross_val_scores.csv:	src/04_model_selection.py data/processed/scaled_fifa_train.csv
	python src/04_model_selection.py \
    --scaled_train=data/processed/scaled_fifa_train.csv

# Hyperparameter Optimization and Testing model on test data
outputs : src/05_hyperparameter_scoring.py data/processed/scaled_fifa_train.csv data/processed/scaled_fifa_test.csv
	python src/05_hyperparameter_scoring.py \
    --scaled_train=data/processed/scaled_fifa_train.csv \
    --scaled_test=data/processed/scaled_fifa_test.csv


clean:
	rm -f data/raw/players_22.csv
	rm -f data/processed/fifa_train.csv
	rm -f data/processed/fifa_test.csv
	rm -f results/eda_plots.png
	rm -f data/processed/scaled_fifa_train.csv
	rm -f data/processed/scaled_fifa_test.csv
	rm -f results/model_cross_val_scores.csv
	rm -f results/hyperparameter_rankings.csv
	rm -f results/test_score.csv
	rm -f results/best_model.pickle