from matplotlib import pyplot as plt
from seaborn import countplot
from wordcloud import WordCloud

# types
# from typing import Any
# from matplotlib.axis import Axis
# from matplotlib.figure import Figure
from pandas import Series


def plot_wordcloud(data: Series) -> None:
    word_cloud = WordCloud(width=800, height=600).generate_from_frequencies(data.value_counts())
    plt.title(data.name, fontsize=28)
    plt.imshow(word_cloud)
    plt.axis("off")


# ---------------------------------------------------------------------------------


# TODO: catagorical distribution
