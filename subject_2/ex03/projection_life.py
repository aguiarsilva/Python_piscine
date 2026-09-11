from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    """
    This program loads the files (income_per_person_gdppercapita_ppp_inflation
    _adjusted.csv and life_expectancy_years.csv) and displays a graph with the
    projection of life expectancy in relation to the gdp of the year 1900 for
    each country.
    """
    try:
        life_df = load("./life_expectancy_years.csv")
        gdp_df = load(
                "./income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
                )

        if life_df is None or gdp_df is None:
            return None

        for col in gdp_df.columns:
            gdp_df[col] = pd.to_numeric(
                    gdp_df[col].astype(str).str.replace('k', ''),
                    errors='coerce'
            )

        year = "1900"
        life_1900 = life_df[year]
        gdp_1900 = gdp_df[year]

        combined_data = pd.DataFrame({
            'Life Expectancy': life_1900,
            'GDP': gdp_1900
            })

        combined_clean = combined_data.dropna()

        plt.figure(figsize=(12, 6))
        plt.scatter(combined_clean['GDP'], combined_clean['Life Expectancy'])
        plt.ylabel("Life Expectancy (years)")
        plt.xlabel("GDP per capita")
        plt.title("Life Expectancy vs GDP per capita (1900)")
        plt.grid(True, alpha=0.3)

        def thousands_formatter(y, pos):
            return f'{int(y/1000)}k'

        plt.gca().xaxis.set_major_formatter(
                plt.FuncFormatter(thousands_formatter)
                )
        plt.show()

        return combined_clean.shape

    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    main()
