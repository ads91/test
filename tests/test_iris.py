import pandas as pd

from iris import IRIS_DATA_URL, load_data, group_sepal_length, describe


# TODO: mock out upstream data dependency to load a static local version of the data
IRIS_DATA = load_data(IRIS_DATA_URL)


def test_group_sepal_length():
    assert group_sepal_length(IRIS_DATA, 5.8).to_dict() == {"setosa": 1}
    assert group_sepal_length(IRIS_DATA, 7.9).to_dict() == {"virginica": 1}


def test_describe():
    expected = {
        "sepal_length": {"count": 150.0, "mean": 5.8433333333, "std": 0.828066128, "min": 4.3, "25%": 5.1, "50%": 5.8,
                         "75%": 6.4, "max": 7.9},
        "sepal_width": {"count": 150.0, "mean": 3.0573333333, "std": 0.4358662849, "min": 2.0, "25%": 2.8, "50%": 3.0,
                        "75%": 3.3, "max": 4.4},
        "petal_length": {"count": 150.0, "mean": 3.758, "std": 1.7652982333, "min": 1.0, "25%": 1.6, "50%": 4.35,
                         "75%": 5.1, "max": 6.9},
        "petal_width": {"count": 150.0, "mean": 1.1993333333, "std": 0.762237669, "min": 0.1, "25%": 0.3, "50%": 1.3,
                        "75%": 1.8, "max": 2.5}}
    df_1, df_2 = describe(IRIS_DATA), pd.DataFrame.from_dict(expected)
    pd.testing.assert_frame_equal(df_1, df_2)


if __name__ == "__main__":
    test_group_sepal_length()
    test_describe()
