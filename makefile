

# Downloading, unzipping, extracting and splitting data into test and train datasets
data/raw/players_22.csv : src/01_load_clean_tidy.py
	python src/01_load_clean_tidy.py \
    --url=https://sports-statistics.com/database/fifa/fifa_2022_datasets.zip \
    --filename=players_22.csv





clean:
	rm -f data/raw/players_22.csv
	rm -f data/processed/fifa_train.csv
	rm -f data/processed/fifa_test.csv