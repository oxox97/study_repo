import kagglehub
import pandas as pd
import os


def parse_netflix_file(file_path):
    data = []
    current_movie = None
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if line.endswith(":"):
                current_movie = int(line[:-1])
                if current_movie == 101:  # movieId sampling
                    break
            else:
                user, rating, date = line.split(",")
                if int(user) < 10000:  # userId sampling
                    data.append([int(user), current_movie, int(rating), date])
                else:
                    continue
    return pd.DataFrame(data, columns=["userId", "movieId", "rating", "timestamp"])


if __name__ == "__main__":
    path = kagglehub.dataset_download("netflix-inc/netflix-prize-data")
    file_path = os.path.join(path, "combined_data_1.txt")
    df = parse_netflix_file(file_path)
    print(df.shape)
    print(df.head())
    