# Source Scripts

This directory contains the data preparation and splitting scripts used in the project.

- `prepare_imdb.py`  
  Creates the balanced 20,000-review IMDb dataset used in the experiments.

- `prepare_goodreads.py`
  Creates the balanced 20,000-review Goodreads dataset used in the experiments.

The file `data/goodreads_20000_with_sentence_labels.jsonl` contains the sampled Goodreads reviews with the original sentence-level annotations used for the truncation analysis. This exported file from the original data-preparation workflow is included in the repository.

- `split_datasets.py`  
  Creates the item-based train, validation, and test splits for both datasets using seed 42.

For the complete reproduction workflow and required input files, see the main project `README.md` and `data/README.md`.