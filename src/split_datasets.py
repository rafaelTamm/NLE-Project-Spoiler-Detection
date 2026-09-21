import pandas as pd
from sklearn.model_selection import GroupShuffleSplit


def split_dataset(input_file, output_prefix):
    df = pd.read_csv(input_file)

    #  split in training validation und test
    splitter = GroupShuffleSplit(
        n_splits=1,
        train_size=0.7,
        random_state=42
    )

    train_idx, temp_idx = next(
        splitter.split(
            df,
            groups=df["item_id"]
        )
    )

    train_df = df.iloc[train_idx].copy()
    temp_df = df.iloc[temp_idx].copy()

    # Die restlichen 30 % halbieren
    splitter_temp = GroupShuffleSplit(
        n_splits=1,
        train_size=0.5,
        random_state=42
    )

    val_idx, test_idx = next(
        splitter_temp.split(
            temp_df,
            groups=temp_df["item_id"]
        )
    )

    val_df = temp_df.iloc[val_idx].copy()
    test_df = temp_df.iloc[test_idx].copy()

    train_df.to_csv(f"{output_prefix}_train.csv", index=False)
    val_df.to_csv(f"{output_prefix}_val.csv", index=False)
    test_df.to_csv(f"{output_prefix}_test.csv", index=False)

    print(f"\n{output_prefix.upper()}")

    for name, split in [
        ("Train", train_df),
        ("Validation", val_df),
        ("Test", test_df)
    ]:
        print(f"\n{name}")
        print("Reviews:", len(split))
        print("Items:", split["item_id"].nunique())
        print(split["is_spoiler"].value_counts())
        print(
            (
                split["is_spoiler"]
                .value_counts(normalize=True)
                * 100
            ).round(2)
        )

    train_items = set(train_df["item_id"])
    val_items = set(val_df["item_id"])
    test_items = set(test_df["item_id"])

    print("\nOverlaps")
    print("Train / Validation:", len(train_items & val_items))
    print("Train / Test:", len(train_items & test_items))
    print("Validation / Test:", len(val_items & test_items))


split_dataset(
    "data/imdb_spoiler_20000.csv",
    "data/imdb"
)

split_dataset(
    "data/goodreads_spoiler_20000.csv",
    "data/goodreads"
)
