import json
import random
import pandas as pd

INPUT_FILE = "goodreads_reviews_spoiler.json"
OUTPUT_FILE = "goodreads_spoiler_20000.csv"

N_PER_CLASS = 10000
RANDOM_SEED = 42

random.seed(RANDOM_SEED)

spoiler_reviews = []
non_spoiler_reviews = []

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    for line in f:
        review = json.loads(line)

        review_text = " ".join(
            sentence[1]
            for sentence in review["review_sentences"]
        )

        row = {
            "review_text": review_text,
            "is_spoiler": review["has_spoiler"],
            "item_id": review["book_id"]
        }

        if review["has_spoiler"]:
            spoiler_reviews.append(row)
        else:
            non_spoiler_reviews.append(row)

random.shuffle(spoiler_reviews)
random.shuffle(non_spoiler_reviews)

spoiler_sample = spoiler_reviews[:N_PER_CLASS]
non_spoiler_sample = non_spoiler_reviews[:N_PER_CLASS]

df = pd.DataFrame(spoiler_sample + non_spoiler_sample)

df = df.sample(
    frac=1,
    random_state=RANDOM_SEED
).reset_index(drop=True)

df.to_csv(OUTPUT_FILE, index=False)

print("Shape:", df.shape)
print(df["is_spoiler"].value_counts())
