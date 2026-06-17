import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Program that loads a dataset, print its dimensions and plot a country's
    time series. 
    Returns the dimensions tuple on sucess or None on any error.
    """
    try:
        df = load("./life_expectancy_years.csv")
        if df is None:
            return None
        
        country = "Germany"
        if country not in df.index:
            return None

        years = df.columns.astype(int)
        values = df.loc[country]

        plt.figure(figsize=(12, 6))
        plt.plot(years, values, marker='.', linestyle='-')
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.title(f"{country} Life Expectancy Projections")
        plt.grid(True)
        plt.show()

        return df.shape

    except Exception as e:
        return None


if __name__ == "__main__":
    main()
