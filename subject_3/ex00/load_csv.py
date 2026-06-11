import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Function to load the Dataset from a file path
    Args: path where the file is located
    Returns the dimension of the loaded dataset.
    """
    if path is None:
        raise AssertionError("Error: wrong or inexistent path")

    if not path.endswith('.csv'):
        raise ValueError(f"Expected .csv file, got {path}")

    df = pd.read_csv(path)
    
    return df
