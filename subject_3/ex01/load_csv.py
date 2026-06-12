import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Function to load the Dataset from a file path
    Args: path where the file is located
    Writes the dimensions of the dataset and returns it.
    """
    try:
        df = pd.read_csv(path)

        dimensions = df.shape
        print(f"Loading dataset of dimensions ({dimensions[0]} x {dimensions[1]})")

        return dimensions
    except Exception:
        return None
        
