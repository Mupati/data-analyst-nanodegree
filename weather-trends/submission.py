import pandas as pd

# fill empty csv data


def fill_empty(csv_file):
    df = pd.read_csv(csv_file)
    return df.fillna(method='ffill')


def find_moving_average(dataFrame):
    pass


if __name__ == "__main__":
    accra_data = './accra_city_data.csv'
    global_data = './global_data.csv'
