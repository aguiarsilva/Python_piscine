from load_csv import load
from matplotlib.pyplot import plt
import pandas as pd


def main():
    """
    This program loads the files (income_per_person_gdppercapita_ppp_inflation
    _adjusted.csv and life_expectancy_years.csv) and displays a graph with the
    projection of life expectancy in relation to the gdp of the year 1900 for
    each country.
    """
    try:
        df = load("./population_total.csv")
        df2 = load(
                "./income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
                )

        if df is None or df2 is None:
            return None

        for col in df2.columns:
            df2[col] = pd.to_numeric(df2[col].astype(str).str.replace('k', ''),
                                     errors='coerce')

        year = "1900"
        df_1900 = df[year]
        df2_1900 = df2[year]

        combined_data = pd.DataFrame({
            'Life Expectancy': df_1900,
            'GDP': df2_1900
            })

        combined_clean = combined_data.dropna()

        plt.figure(figsize=(12,6))
        plt.scatter(combined_clean['Life Expectancy'], combined_clean['GDP'])
        plt.xlabel("Life Expectancy (years)")
        plt.ylabel("GDP per capita")
        plt.title("Life Expectancy vs GDP per capita (1900)")
        plt.grid(True, alpha=0.3)
        plt.show()

        return combined_clean.shape

    except Exception as e:
        print(f"Error: {e}")
        return None



if __name__ == "__main__":
    main()
