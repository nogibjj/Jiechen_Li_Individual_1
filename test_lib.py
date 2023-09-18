"""
Test for library goes here

"""
from lib import (
    # readfile,
    lib_describe,
    lib_get_sum,
    plt_show,
    plt_sns_show,
)
import pandas as pd


csv_file = "spotify_2023_1.csv"
df = pd.read_csv(csv_file)


def test_descirbe():
    # data = pd.read_csv(file)
    data = pd.read_csv(csv_file)
    # result = lib_describe(file)
    result = lib_describe(data)
    assert result.loc["mean", "artist_count"] == 1.5561385099685205
    assert result.loc["min", "artist_count"] == 1.000000
    assert result.loc["std", "artist_count"] == 0.8930441928452748
    assert result.loc["max", "artist_count"] == 8.000000


# df = df.isnull()
def test_sum():
    lib_get_sum(df.isnull())


def test_plot_a():
    plt_show(df)


def test_plot_b():
    plt_sns_show(df)
