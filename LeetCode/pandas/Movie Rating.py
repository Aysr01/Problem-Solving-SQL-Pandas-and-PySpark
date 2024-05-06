# Join, GROUP BY, COUNT, SORT VALUES, Query, MEAN
import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    # User with highest number of rates
    user_with_high_rates = users.merge(movie_rating, on="user_id") \
                                .groupby(["user_id", "name"])["rating"] \
                                .count() \
                                .rename("count")\
                                .reset_index() \
                                .sort_values(["count", "name"], ascending=[False, True]) \
                                .head(1)
    # Movie with the highest average rate
    highest_rated_movie = movies.merge(movie_rating, on="movie_id") \
                            .query(" '2020-03-01' > `created_at` >= '2020-02-01'") \
                            .groupby(["movie_id", "title"])["rating"] \
                            .mean() \
                            .rename("avg_rate")\
                            .reset_index() \
                            .sort_values(["avg_rate", "title"], ascending=[False, True]) \
                            .head(1)

    output = {
        "results": [
            user_with_high_rates["name"].values[0],
            highest_rated_movie["title"].values[0]
        ]}
    
    return pd.DataFrame(output)