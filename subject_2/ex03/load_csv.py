import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """
    Function to load the Dataset from a file path
    Args: path where the file is located
    Writes the dimensions of the dataset and returns it.
    """
    try:
        df = pd.read_csv(path, index_col=0)

        dimensions = df.shape
        print(f"Loading dataset of dimensions ( \
              {dimensions[0]} x {dimensions[1]})"
              )
        return df

    except Exception:
        return None
