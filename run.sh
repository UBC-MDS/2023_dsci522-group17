#!/bin/bash
# Intermediary pipe for fifa-potential analysis scripts

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