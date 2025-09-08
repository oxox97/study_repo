import numpy as np

def precision_at_k(recommended_items, ground_truth, k=10):
    """
    Precision@K
    recommended_items: list of item ids recommended (길이 >= k)
    ground_truth: set of items that are actually relevant
    """
    recommended_k = recommended_items[:k]
    hits = len(set(recommended_k) & set(ground_truth))
    return hits / k


def recall_at_k(recommended_items, ground_truth, k=10):
    """
    Recall@K
    """
    recommended_k = recommended_items[:k]
    hits = len(set(recommended_k) & set(ground_truth))
    return hits / len(ground_truth) if ground_truth else 0.0


def average_precision(recommended_items, ground_truth, k=10):
    """
    MAP 계산에 쓰이는 AP@K
    """
    score = 0.0
    hits = 0
    for i, item in enumerate(recommended_items[:k], start=1):
        if item in ground_truth:
            hits += 1
            score += hits / i
    return score / min(len(ground_truth), k) if ground_truth else 0.0


def ndcg_at_k(recommended_items, ground_truth, k=10):
    """
    NDCG@K
    """
    dcg = 0.0
    for i, item in enumerate(recommended_items[:k], start=1):
        if item in ground_truth:
            dcg += 1 / np.log2(i + 1)
    # ideal DCG
    idcg = sum(1 / np.log2(i + 1) for i in range(1, min(len(ground_truth), k) + 1))
    return dcg / idcg if idcg > 0 else 0.0


def evaluate_model(model, test_interactions, train_interactions, k=10):
    """
    모델 전체 평가
    model: 학습된 ALS 모델 (user_vecs, item_vecs 속성 보유)
    test_interactions: dict {user: set(items)} 테스트 데이터
    train_interactions: dict {user: set(items)} 학습 데이터 (이미 본 아이템 제외 목적)
    """
    precisions, recalls, maps, ndcgs = [], [], [], []

    for user, true_items in test_interactions.items():
        if not true_items:
            continue

        # 모든 아이템에 대해 점수 예측
        scores = model.user_vecs[user] @ model.item_vecs.T
        # 학습에서 이미 본 아이템은 제외
        seen = train_interactions.get(user, set())
        scores[list(seen)] = -np.inf

        # 추천 상위 k개
        recommended = np.argsort(-scores)[:k]

        # 각 지표 계산
        precisions.append(precision_at_k(recommended, true_items, k))
        recalls.append(recall_at_k(recommended, true_items, k))
        maps.append(average_precision(recommended, true_items, k))
        ndcgs.append(ndcg_at_k(recommended, true_items, k))

    return {
        "precision": np.mean(precisions) if precisions else 0.0,
        "recall": np.mean(recalls) if recalls else 0.0,
        "map": np.mean(maps) if maps else 0.0,
        "ndcg": np.mean(ndcgs) if ndcgs else 0.0
    }
