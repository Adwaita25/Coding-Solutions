import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    rows = players.shape[0]
    cols = players.shape[1]
    return [rows, cols]
