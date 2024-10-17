from pandas import DataFrame, Series
from numpy import number


def get_iqr(data: Series)-> tuple[float, float]:
    """
    Return the lower limit and upper limit using IQR

    Args:
        data (Series) : numerical data points

    Returns:
        tuple(lower_limit, upper_limit) [float, float] : the IQR range
    """

    threshold = 1.5
    Q1, Q3 = data.quantile([.25, .75])
    IQR = Q3 - Q1
    lower_limit = Q1 - (IQR * threshold)
    upper_limit = Q3 + (IQR * threshold)
    return (lower_limit, upper_limit)


# -----------------------------------------------------------------------


def get_outliers(df: DataFrame) -> DataFrame:
    """
        return outliers using IQR in given df

        Args:
            df (DataFrame) : dataframe object to perform operation

        Returns:
            DataFrame object
    """

    data = {}
    df_copy = df.copy()
    numerical_columns = df_copy.select_dtypes(number)

    for each in numerical_columns:
        lower_limit, upper_limit = get_iqr(data=df_copy[each])

        total_count = df_copy.shape[0]      # count of the dataframe
        outliers = df_copy[~df_copy[each].between(lower_limit, upper_limit)]
        outlier_count = outliers.shape[0]
        percentage = round((outlier_count / total_count) * 100, 2) if outlier_count != 0 else 0      # how much outliers that have in DF
        values = outliers[each] if len(outliers[each]) > 0 else "Empty"    # outlier values

        data[each] = {"df_count" : total_count, "outlier_count" : outlier_count,
                      "percentage" : percentage, "outlier_values" : values}

    return DataFrame(data).T        # Transposed DF


# -----------------------------------------------------------------------


def handle_outliers(df: DataFrame, columns: list[str]) -> DataFrame:
    """
        remove outliers

        Args:
            df (DataFrame) : dataframe object to perform operation
            columns (list[str]) : specific columns

        Returns:
            new outlier removed dataframe 
    """

    df_copy = df.copy()
    for each in columns:
        lower_limit, upper_limit = get_iqr(data=df[each])
        df_copy = df_copy[df_copy[each].between(lower_limit, upper_limit)]

    return df_copy
