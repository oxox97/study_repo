import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """
    Netflix Prize Data 불러기
    """
    df = pd.read_csv(
        path,
        header=None,
        names=["movie_id", "year", "title", "tmp", "tmp2", "tmp3"],
        encoding="latin-1",
        )  # names
    return df.head(10)


if __name__ == "__main__":
    path = "dataset/movie_titles.csv"
    print(f"[INFO] Loading dataset from {path} ...")
    df = load_data(path)
    print(df.head())