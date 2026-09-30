# Data

This directory contains the processed datasets used for the spoiler detection experiments.

## Original Datasets

The original datasets are not included in this repository due to their size.

### IMDb Spoiler Dataset

Source:

**IMDb Spoiler Dataset by Rishabh Misra**

Original file used:

`IMDB_reviews.json`

The preparation script creates a balanced subset containing:

- 10,000 spoiler reviews
- 10,000 non-spoiler reviews

### Goodreads Spoiler Dataset

Source:

**Goodreads Spoiler Dataset by Wan et al.**

Original file used:

`goodreads_reviews_spoiler.json`

The preparation script creates a balanced subset containing:

- 10,000 spoiler reviews
- 10,000 non-spoiler reviews

The original datasets must be downloaded separately before running the preparation scripts.

## Processed Data

The processed datasets used for the experiments are included in this repository.

### IMDb

- `imdb_spoiler_20000.csv` — balanced 20,000-review IMDb sample
- `imdb_train.csv` — training split
- `imdb_val.csv` — validation split
- `imdb_test.csv` — test split

### Goodreads

- `goodreads_spoiler_20000.csv` — balanced 20,000-review Goodreads sample
- `goodreads_train.csv` — training split
- `goodreads_val.csv` — validation split
- `goodreads_test.csv` — test split
- `goodreads_20000_with_sentence_labels.jsonl` — the sampled Goodreads reviews with the original sentence-level spoiler annotations preserved for the truncation analysis

## Dataset Splits

The datasets are split by item identifier rather than individual review. This prevents reviews of the same movie or book from appearing in multiple partitions.

The intended split is approximately:

- 70% training
- 15% validation
- 15% test

A fixed random seed of `42` is used for sampling and splitting.

The resulting split sizes are:

| Dataset | Train | Validation | Test |
| --- | ---: | ---: | ---: |
| IMDb | 13,913 | 2,821 | 3,266 |
| Goodreads | 13,982 | 2,934 | 3,084 |

## Data Preparation

The preprocessing scripts are located in `src/`:

- `prepare_imdb.py`
- `prepare_goodreads.py`
- `split_datasets.py`

`prepare_imdb.py` and `prepare_goodreads.py` create the balanced 20,000-review datasets from the original data.

`split_datasets.py` creates the item-based training, validation, and test partitions.

The processed CSV files required to run the classification experiments are already included in this repository.

## Sentence-Level Goodreads Data

The file `goodreads_20000_with_sentence_labels.jsonl` preserves the sentence-level spoiler annotations for the 20,000 Goodreads reviews used in this project.

It is used for the 1,024-token truncation analysis in `notebooks/03_results_analysis.ipynb`. The main classification experiments use the CSV train, validation, and test splits.

IMDb provides review-level spoiler labels but not equivalent sentence-level spoiler annotations, so the fine-grained spoiler-evidence truncation analysis is performed only for Goodreads.