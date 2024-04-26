# SORT VALUES, DENSE RANK
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    sorted_scores = scores.sort_values(by="score", ascending=False)
    sorted_scores["rank"] = sorted_scores["score"].rank(
        method="dense",
        ascending=False
    )
    return sorted_scores[["score", "rank"]]