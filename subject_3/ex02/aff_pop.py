from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    This program loads a csv file and displays the life expectancy infos
    for two chosen countries, for the years between 1800 to 2050.
    It displays a graph image with the result on the screen.
    """
    try:
        df = load("./population_total.csv")
        if df is None:
            return None

        countries_plot = ["Germany", "France"]
        plt.figure(figsize=(12, 6))

        years = df.columns.astype(int)
        mask = (years >= 1800) & (years <= 2050)
        years_filtered = years[mask]

        for country in countries_plot:
            if country in df.index:
                plt.plot(years_filtered, df.loc[country][mask], marker='.', linestyle='-',
                         label=country)

        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.title("Population Projections")
        plt.legend()
        plt.grid(True)
        plt.show()

        return df.shape

    except Exception as e:
        return None


if __name__ == "__main__":
    main()
