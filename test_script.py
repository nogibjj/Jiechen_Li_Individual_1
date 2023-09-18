"""
Test for script.py goes here
"""

from lib import (
    readfile,
    lib_describe,
    lib_get_sum,
    plt_show,
    plt_sns_show,
)

# import pandas as pd


def test_main():
    # df = "spotify_2023_1.csv"
    data = readfile("spotify_2023_1.csv")
    lib_describe(data)
    lib_get_sum(data.isnull())
    plt_show(data)
    plt_sns_show(data)


if __name__ == "__main__":
    test_main()
