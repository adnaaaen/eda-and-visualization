from pandas import DataFrame
from numpy import percentile, number


def get_iqr(data: list[int | float]) -> tuple[float, float]:
    """
    Return the lower limit and upper limit using IQR

    Args:
        data (list[int | float]) : numerical data points

    Returns:
        tuple(lower_limit, upper_limit) [float, float] : the IQR range
    """

    threshold = 1.5
    Q1, Q3 = percentile(data, [.25, .75])
    IQR = Q3 - Q1
    upper_limit, lower_limit = Q1 - (IQR * threshold), Q3 + (IQR * threshold)
    return (lower_limit, upper_limit)


# -----------------------------------------------------------------------


def get_outliers(df: DataFrame, columns: list[str] | None = None) -> DataFrame:
    """
        return outliers using IQR in given df

        Args:
            df (DataFrame) : dataframe object to perform operation
            columns (list[str]) [optional] : specific columns
            threshold (float) = 1.5 : dataframe object to perform operation

        Returns:
            DataFrame object
    """

    data = {}
    df_copy = df.copy()
    numerical_columns = df_copy.select_dtypes(number)

    for each in columns if columns else numerical_columns:
        lower_limit, upper_limit = get_iqr(data=df[each].to_list())

        total_count = df_copy.shape[0]      # count of the dataframe
        outliers = df_copy[~df_copy[each].between(lower_limit, upper_limit)]
        outlier_count = outliers.shape[0]
        percentage = round((outlier_count / total_count) * 100, 2)      # how much outliers that have in DF
        values = outliers[each]     # outlier values

        data[each] = {"df_count" : total_count, "outlier_count" : outlier_count,
                      "percentage" : percentage, "outlier_values" : values}

    return DataFrame(data).T        # Transposed DF


# -----------------------------------------------------------------------


def handle_outliers(df: DataFrame, columns: list[str]) -> DataFrame:
    """
        remove outliers

        Args:
            df (DataFrame) : dataframe object to perform operation
            columns (list[str]) [optional] : specific columns

        Returns:
            new outlier removed dataframe 
    """

    df_copy = df.copy()
    for each in columns:
        lower_limit, upper_limit = get_iqr(data=df[each].to_list())
        df_copy = df_copy[~df_copy[each].between(lower_limit, upper_limit)]

    return df_copy
