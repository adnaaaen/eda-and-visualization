from matplotlib import pyplot as plt
from numpy import column_stack
from wordcloud import WordCloud

# types
from pandas import Series, DataFrame


def plot_wordcloud(df: DataFrame, columns: list[str]) -> None:
    """
    return wordcloud of its values
    Args:
        data (Series) : data to be create wordcloud

    Return:
        None
    """

    for index, column in enumerate(columns, start=1):
        row_len = len(columns)
        rows = round(row_len/2)
        plt.subplot(rows, 2, index)
        word_cloud = WordCloud(width=800, height=600).generate_from_frequencies(df[column].value_counts()
        plt.title(column, fontsize=28)
        plt.imshow(word_cloud)
        plt.axis("off")



def plot_catagorical(df: DataFrame, columns: list[str]) -> None:
    for index, column in enumerate(columns, start=1):
        row_len = len(columns)
        rows = round(row_len/2)
        plt.subplot(rows, 2, index)
        data = df[column].value_counts().nlargest(n=5)
        plt.title(column)
        plt.bar(x=data.index, height=data.values)
        plt.xticks(rotation=90)

