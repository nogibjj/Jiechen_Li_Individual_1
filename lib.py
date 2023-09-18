"""
Python Descriptive Statistics Script Library

"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read the Dataframe spotify_2023.csv.


def readfile(file):
    df = pd.read_csv(file)
    return df


def lib_describe(df):
    return df.describe()


# check for missing values


def lib_get_sum(df):
    # df = df.isnull()
    return df.sum()


# Danceability, Valence, and Energy Distribution


def plt_show(df):
    plt.figure(figsize=(8, 8))
    labels = ["Danceability", "Valence", "Energy"]
    sizes = [
        df["danceability_%"].iloc[0],
        df["valence_%"].iloc[0],
        df["energy_%"].iloc[0],
    ]
    colors = ["lightcoral", "lightgreen", "skyblue"]
    # explode the 1st slice (Danceability)
    explode = (0.1, 0.1, 0.1)
    plt.pie(
        sizes,
        explode=explode,
        labels=labels,
        colors=colors,
        autopct="%1.1f%%",
        shadow=True,
        startangle=140,
    )
    plt.title("Danceability, Valence, and Energy Distribution")
    # equal aspect ratio ensures that pie is drawn as a circle.
    plt.axis("equal")
    plt.show()


def plt_sns_show(df):
    sns.set(style="whitegrid")
    columns_to_plot = [
        "danceability_%",
        "valence_%",
        "energy_%",
        "acousticness_%",
        "instrumentalness_%",
    ]
    sns.pairplot(df[columns_to_plot], palette="coolwarm")
    plt.suptitle("Pairplot of Audio Attributes", y=1.02)
    plt.show()
