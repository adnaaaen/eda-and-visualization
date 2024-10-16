from pandas import DataFrame, Series


def drop(df: DataFrame, col_to_ignore: list[str]) -> DataFrame:
    return df.drop(columns=col_to_ignore)


# -----------------------------------------------------------------------------------------------------

# TODO: complete
def clean(df: DataFrame) -> DataFrame:
    """
    clean dataset

    Args:
        df (DataFrame) : the dataframe object

    Returns:
        DataFrame : a cleaned dataframe object
    
    """
    pass


# -------------------------------------------------------------------------------------------


def impute(simpleimputer: object) -> Series:
    pass 
