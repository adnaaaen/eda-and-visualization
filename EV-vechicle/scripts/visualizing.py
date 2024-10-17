from matplotlib import pyplot as plt
from seaborn import histplot
from wordcloud import WordCloud

# types
from pandas import Series


def plot_wordcloud(data: Series) -> None:
    """
    return wordcloud of its values
    Args:
        data (Series) : data to be create wordcloud

    Return:
        None
    """

    word_cloud = WordCloud(width=800, height=600).generate_from_frequencies(data.value_counts())
    plt.title(data.name, fontsize=28)
    plt.imshow(word_cloud)
    plt.axis("off")


# ---------------------------------------------------------------------------------


def plot_catagorical(data: Series) -> None:

    """
    plot catagorical about the top 10 value counts in the data
    Args:
        data (Series) : data to be create wordcloud

    Return:
        None
    """
    
    highest_data = data.value_counts().nlargest(n=10)
    plt.title(f"TOP 10 {data.name}", fontsize=24)
    plt.bar(x=highest_data.index, height=highest_data.values)
    plt.xticks(rotation=90)
    plt.show()


# ---------------------------------------------------------------------------------


def plot_numerical(data: Series) -> None:
    """
"
    plot numerical variable with histogram to find the distribution
    Args:
        data (Series) : data to be create wordcloud

    Return:
        None
    "
    """

    plt.title(f"DISTRIBUTION OF {data.name}", fontsize=20)
    histplot(data, bins=20, kde=True)
    plt.show()




    
