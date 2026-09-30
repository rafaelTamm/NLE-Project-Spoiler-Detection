# Cross-Domain Spoiler Detection

This repository contains the implementation and evaluation of a cross-domain spoiler detection project using movie reviews from IMDb and book reviews from Goodreads.

The main research question is:

> How well do text-based spoiler classifiers transfer between the IMDb movie-review and Goodreads book-review datasets?

Two approaches are compared:

- TF-IDF + Logistic Regression
- ModernBERT (`answerdotai/ModernBERT-base`)

Both approaches are evaluated in four settings:

1. IMDb → IMDb
2. Goodreads → Goodreads
3. IMDb → Goodreads
4. Goodreads → IMDb

The first two settings measure in-domain performance, while the latter two evaluate cross-domain transfer.

## Repository Structure

```text
.
├── data/
│   ├── README.md
│   ├── imdb_spoiler_20000.csv
│   ├── goodreads_spoiler_20000.csv
│   ├── imdb_train.csv
│   ├── imdb_val.csv
│   ├── imdb_test.csv
│   ├── goodreads_train.csv
│   ├── goodreads_val.csv
│   ├── goodreads_test.csv
│   └── goodreads_20000_with_sentence_labels.jsonl
├── notebooks/
│   ├── README.md
│   ├── 01_tfidf_baseline.ipynb
│   ├── 02_modernbert.ipynb
│   └── 03_results_analysis.ipynb
├── results/
│   ├── README.md
│   ├── tfidf_results.csv
│   ├── modernbert_multiseed_results.csv
│   ├── modernbert_multiseed_summary.csv
│   ├── modernbert_confidence.csv
│   ├── modernbert_length_analysis.csv
│   ├── modernbert_cross_domain_error_sample.csv
│   └── goodreads_truncation_analysis.csv
├── src/
│   ├── prepare_imdb.py
│   ├── prepare_goodreads.py
│   └── split_datasets.py
├── requirements.txt
└── README.md
```

## Installation

Python 3 is required.

Install the required dependencies with:

```bash
pip install -r requirements.txt
```

The main dependencies are pandas, NumPy, scikit-learn, Matplotlib, PyTorch, Transformers, Datasets, and Accelerate.

## Data

The project uses two spoiler detection datasets:

- IMDb movie reviews
- Goodreads book reviews

For each domain, a balanced sample of 20,000 reviews is used:

- 10,000 spoiler reviews
- 10,000 non-spoiler reviews

The data is split by movie or book identifier rather than individual review. This prevents reviews of the same item from occurring in multiple dataset partitions.

The intended split ratio is approximately 70% training, 15% validation, and 15% test. Sampling and dataset splitting use random seed `42`.

The processed datasets required for the experiments are included in `data/`. The original source datasets are not included.

See `data/README.md` for details about the datasets and data preparation.

## Experiments

### 1. TF-IDF + Logistic Regression

Notebook:

`notebooks/01_tfidf_baseline.ipynb`

The baseline uses TF-IDF features with Logistic Regression. The regularization parameter is selected from `C ∈ {0.1, 1, 10}` using validation Macro-F1 on the source domain.

Results are saved to:

`results/tfidf_results.csv`

### 2. ModernBERT

Notebook:

`notebooks/02_modernbert.ipynb`

The transformer experiments use `answerdotai/ModernBERT-base`.

Main training configuration:

- maximum sequence length: 1,024 tokens
- epochs: 3
- learning rate: 2e-5
- training batch size: 2
- evaluation batch size: 4
- gradient accumulation steps: 4
- model selection based on validation Macro-F1

Fine-tuning is repeated with three random seeds:

- 42
- 123
- 456

The dataset splits remain fixed across these runs. Main ModernBERT results are reported as mean and sample standard deviation across the three fine-tuning seeds.

### 3. Final Results and Analysis

Notebook:

`notebooks/03_results_analysis.ipynb`

The final notebook combines the experiment results and performs:

- in-domain and cross-domain comparison
- cross-domain transfer analysis
- confidence analysis
- review-length analysis
- qualitative cross-domain error analysis
- Goodreads 1,024-token truncation analysis

The main ModernBERT results use all three fine-tuning seeds. Detailed prediction-level analyses use the seed-42 models.

## Evaluation

The reported classification metrics are:

- Accuracy
- Precision
- Recall
- F1
- Macro-F1

Macro-F1 is used as the primary metric for model selection and comparison.

## Reproducing the Experiments

Run the notebooks from the repository root so that the relative `data/` and `results/` paths resolve correctly.

Execute the notebooks in the following order:

1. `notebooks/01_tfidf_baseline.ipynb`
2. `notebooks/02_modernbert.ipynb`
3. `notebooks/03_results_analysis.ipynb`

The TF-IDF baseline and final analysis do not require a GPU.

ModernBERT fine-tuning is computationally more expensive and is intended to be run with GPU acceleration. The ModernBERT notebook supports Google Colab and uses Google Drive for persistent model checkpoints.

The exported result files are already included in `results/`, so the final analyses can be inspected without retraining ModernBERT.

## Reproducing the Data Preparation

If the processed datasets in `data/` are already available, the preparation step can be skipped.

To recreate them from the original datasets, download the source files described in `data/README.md` and place them in `data/`.

Then run:

```bash
python src/prepare_imdb.py
python src/prepare_goodreads.py
python src/split_datasets.py
```

The preparation scripts create the balanced datasets and the item-based train, validation, and test partitions.

## Results

All exported experiment results are stored in `results/`.

See `results/README.md` for a description of the individual result files.