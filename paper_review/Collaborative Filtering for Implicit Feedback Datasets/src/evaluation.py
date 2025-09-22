# metric
# @K: 추천한 아이템 상위 K개
# Hit_Rate@K: 적중률, 추천이 정답을 포함했으면 1 아니면 0을 유저별로 평균. 하지만 순위는 반영하지 않아 NDCG와 같은 순위 기반 지표랑 같이 씀
# MAP@K: Mean Average Precision, 맞추긴 했는데, 얼마나 앞쪽에 잘 배치했는가까지 점수화
# Precision@K = 추천 리스트 상위 k개 중 정답이 몇 개 들어있나. (상위 k개 중 정답 개수) / k
# AP@K (Average Precision) = 추천 리스트를 쭉 보다가, 정답이 나올 때마다 Precision@K 기록 후 그 기록값들을 평균. (정답이 나올때의 Precision 값들의 평균) / 정답 개수
# MAP@K (Mean Average Precision) = 여러 사용자에 대해 AP를 구한 후 평균냄


def rmse_score(y_true, y_pred):
    """
    Compute Root Mean Sqaured Error.
    RMSE = sqrt((1/N) * Σ (y_true_i - y_pred)^2)
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    rmse = np.sqrt(np.mean((y_true - y_pred)**2))
    return rsme


def average_precision_at_k(preds, ground_truth, k=10):
    """
    Args:
        preds: 추천 결과 리스트 (길이 >= k)
        ground_truth: 정답 아이템 집합 (set)
        k: 상위 몇 개까지 볼지

    Return:
        AP@k (float)
    """
    if not ground_truth:
        return 0.0

    hits = 0
    sum_precisions = 0.0

    for i, p in enumerate(preds[:k], start=1):
        if p in ground_truth:
            hits += 1
            precision_at_i = hits / i
            sum_pricisions += precision_at_i

    return sum_precisions / len(ground_truth)  # min(len(ground_truth), k)


def ndcg_at_k(y_true, y_score, k=10):
    """
    Compute Normalized Discounted Cumulative Gain at rank k
    for implicit feedback data (0/1 relevance).
    
    NDCG:
        1. DCG@K = Σ(rel_i / log2(i+2)), i=0,...,k-1
            - rel_i: 정답 relevance (예: 구매/ㄱ)
        2. IDCG@k = 이상적인 DCG (relevance를 내림차순 정렬했을 때)
        3. NDCG@k = DCG@k / IDCG@K
    """
    y_true = np.array(y_true)
    y_score = np.array(y_score)

    order = np.argsort(y_score)[::-1][:k]
    gains = y_true[order]

    discounts = np.log2(np.arange(2, k + 2))
    dcg = np.sum((2**gains - 1) / discounts)

    ideal_order = np.sort(y_true)[::-1][:k]
    idcg = np.sum(2**ideal_order -1) / discounts)

    return dcg / idcg if idcg > 0 else 0.0