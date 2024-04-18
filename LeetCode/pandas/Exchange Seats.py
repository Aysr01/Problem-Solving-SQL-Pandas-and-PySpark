import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    if seat.size == 0:
        return seat    
    ret_df = seat.copy()
    ret_df.loc[seat.id % 2 != 0, "student"] = seat.shift(-1).loc[seat.id % 2 != 0, "student"]
    ret_df.loc[seat.id % 2 == 0, "student"] = seat.shift(1).loc[seat.id % 2 == 0, "student"]
    ret_df.fillna(seat.iloc[-1, 1], inplace=True)
    return ret_df