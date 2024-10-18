from matplotlib import pyplot as plt
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



