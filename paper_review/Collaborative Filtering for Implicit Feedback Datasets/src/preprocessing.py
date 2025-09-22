from scipy.sparse import csr_matrix


def preprocessing(df):
    # p_ui : 영화에 평점을 매긴 경우, 보았다고 가정
    # c_ui : 영화에 매긴 평점이 시청 빈도로 가정
    df["preference"] = 1
    df["confidence"] = 1 + df["rating"]
    df.head()

    # sparse matrix
    df["user_idx"] = df["userId"].astype("category").cat.codes
    df["item_idx"] = df["movieId"].astype("category").cat.codes

    n_users = df["user_idx"].nunique()
    n_items = df["item_idx"].nunique()

    # csr_matrix(Compressed Sparse Row) : 행(row) 중심 압축 저장

    # confidence matrix (CSR)
    C = csr_matrix(
        (df["confidence"], (df["user_idx"], df["item_idx"])),  # (data, (row, col))
        shape=(n_users, n_items)
    )

    # preference matrix (CSR)
    P = csr_matrix(
        (df["preference"], (df["user_idx"], df["item_idx"])),  # (data, (row, col))
        shape=(n_users, n_items)
    )

    print("CSR shape:", C.shape)
    print("Non-zero entries:", C.nnz)