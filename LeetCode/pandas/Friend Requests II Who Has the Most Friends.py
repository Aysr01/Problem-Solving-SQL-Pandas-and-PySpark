import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    # Users that have sent a friend request and got accepted
    accepted_friends = request_accepted[["requester_id"]] \
                            .rename(columns={
                                "requester_id": "id"
                            })
    #Users that have accepted a friend request
    accepters = request_accepted[["accepter_id"]] \
                            .rename(columns={
                                "accepter_id": "id"
                            })
    
    
    result = pd.concat([accepted_friends, accepters]) \
      .groupby("id")["id"] \
      .count() \
      .rename("num") \
      .reset_index() \
      .sort_values(by="num", ascending=False) \
      .head(1)
    
    return result