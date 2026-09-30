# Notebooks

The final experiment notebooks are located in this directory.

Run them in the following order:

1. `01_tfidf_baseline.ipynb`  
   Trains and evaluates the TF-IDF + Logistic Regression baseline.

2. `02_modernbert.ipynb`  
   Fine-tunes and evaluates ModernBERT using the training seeds 42, 123, and 456.

3. `03_results_analysis.ipynb`  
   Combines the experiment results and performs the final cross-domain and error analyses.

The notebooks should be executed from the repository root so that relative paths to `data/` and `results/` resolve correctly.

ModernBERT fine-tuning requires substantially more computational resources than the other experiments and is intended to be run with GPU acceleration.

The exported result files are already available in `results/`, so the final analysis can be inspected without retraining ModernBERT.