#!/bin/bash
# Intermediary pipe for fifa-potential analysis 

# Load, clean, and tidy data 
python src/01_load_clean_tidy.py --url=https://sports-statistics.com/database/fifa/fifa_2022_datasets.zip --filename=players_22.csv

# Generate EDA figures
python src/02_eda_figures.py --dataset=data/processed/fifa_train.csv --target=potential

# Preprocess data 


# Complete model selection 


# Complete hyperparameter tuning