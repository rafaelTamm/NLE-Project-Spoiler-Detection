# Source Scripts

This directory contains the data preparation and splitting scripts used in the project.

- `prepare_imdb.py`  
  Creates the balanced 20,000-review IMDb dataset used in the experiments.

- `prepare_goodreads.py`  
  Creates the balanced 20,000-review Goodreads dataset and preserves the sentence-level information required for the truncation analysis.

- `split_datasets.py`  
  Creates the item-based train, validation, and test splits for both datasets using seed 42.

For the complete reproduction workflow and required input files, see the main project `README.md` and `data/README.md`.