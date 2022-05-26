import pandas as pd


IRIS_DATA_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"


def load_data(url):
    return pd.read_csv(url)


def group_sepal_length(df, max_sepal_length):
    # get the maximum sepal lengths per species (group)
    max_sepal_lengths = df.groupby("species").max()[["sepal_length"]].rename(
        columns={"sepal_length": "max_sepal_length"})
    # join on the maximum sepal lengths per species (group) to the original data
    df = df.set_index("species").merge(max_sepal_lengths, how="left", left_index=True, right_index=True)
    # filter for the rows in which the sepal length equals that rows' maximum group sepal length and equals the
    # requested max sepal length
    df = df[(df["sepal_length"] == df["max_sepal_length"]) & (df["max_sepal_length"] == max_sepal_length)]
    # get the count of the species
    df = df.reset_index().groupby("species").count()["sepal_length"]

    return df


def describe(df):
    return df.describe()
