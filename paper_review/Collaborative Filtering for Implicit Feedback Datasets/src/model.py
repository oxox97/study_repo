# $
# \min_{X, Y} \; 
# \sum_{u,i} c_{ui}\,(p_{ui} - x_u^\top y_i)^2 
# \;+\; \lambda \big( \lVert X \rVert^2 + \lVert Y \rVert^2 \big)
# $

# # 변수 X와 Y 둘 다 있어, 식이 비선형이라 한 번에 닫힌 해(Closed form) 못 구함

# $
# y_i = 
# \left( X^{\top}X + X^{\top}(C_i - I)X + \lambda I \right)^{-1} 
# X^{\top} C_i p_i
# $

# $
# x_u = 
# \left( Y^{\top}Y + Y^{\top}(C_u - I)Y + \lambda I \right)^{-1} 
# Y^{\top} C_u p_u
# $

# where,
# - X: user latent factor matrix (n_users x k)
# - Y : item latent factor matrix (n_items x k)
# - C : confidence matrix (n_users x n_items)
#     - C_u = diag(c_u) (n_items x n_items) (for simple matrix calculation)
# - P : preference matrix (n_users x n_items)
#     - p_u (n_items,)


from numpy.linalg import solve

def update_user_latent_matrix(X, Y, C, P, lambda_reg):
    """
    Update user latent factors (X) given item vectors (Y),
    confidence matrix (C), and preference matrix (P)

    This function implements the ALS update step for users:
        x_u = (Y^T Y + Y^T (C_u - I) Y + λI)^(-1) Y^T C_u p_u

    Args:
        X: User latent matrix of shape (n_users, k)
        Y: Item latent matrix of shape (n_items, k)
        C: Confidence matrix of shape (n_users, n_items)
            For user u, c_u = C[u] (vector), C_u = diag(c_u)
        P: Preference matrix of shape (n_users, n_items)
        lambda_reg: Regularization parameter λ

    Returns:
        Updated user latent matrix X of shape (n_users, k)
    """
    n_users, k = X.shape
    n_items = Y.shape[0]
    YtY = np.matmul(Y.T, Y)  # (k x k)
    I_k = np.identity(k)  # (k x k)
    for u in range(n_users):
        c_u = C[u].toarray().flatten()  # (n_items,)
        p_u = P[u].toarray().flatten()  # (n_items,)
        C_u = np.diag(c_u)  # (n_items, n_items)

        A = YtY + np.matmul(Y.T, np.matmul(C_u - np.identity(n_items), Y)) + lambda_reg * I_k

        b = np.matmul(Y.T, np.matmul(C_u, p_u))

        X[u] = solve(A, b)  # LU Decomposition

    return X


def update_item_latent_matrix(X, Y, C, P, lambda_reg):
    n_users, k = X.shape
    n_items = Y.shape[0]
    XtX = np.matmul(X.T, X)  # (k x k)
    I_k = np.identity(k)  # (k x k)
    for i in range(n_items):
        c_i = C[:, i].toarray().flatten()  # (n_users,)
        p_i = P[:, i].toarray().flatten()  # (n_users,)
        C_i = np.diag(c_i)  # (n_users, n_users)

        A = XtX + np.matmul(X.T, np.matmul(C_i - np.identity(n_users), X)) + lambda_reg * I_k

        b = np.matmul(X.T, np.matmul(C_i, p_i))

        Y[i] = solve(A, b)

    return Y

    from tqdm import tqdm

def als_train(X, Y, C, P, lambda_reg=0.1, n_iters=10):
    """
    Alternating Least Sqaures(ALS) training loop for n_iters.

    Returns:
        X: Trained user latent matrix
        Y: Trained item latent matrix
    """
    for it in tqdm(range(n_iters), desc="ALS training", unit="iter"):
        # print(f"Iteration {it+1}/{n_iters} ...")
        X = update_user_latent_matrix(X, Y, C, P, lambda_reg)
        Y = update_item_latent_matrix(X, Y, C, P, lambda_reg)

    return X, Y


    %%time

k = 20  # latent factor dimension
lambda_reg = 0.1

X = np.random.normal(size=(n_users, k))
Y = np.random.normal(size=(n_items, k))
X, Y = als_train(X, Y, C, P)
X