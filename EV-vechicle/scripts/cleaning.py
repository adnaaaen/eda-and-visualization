from pandas import DataFrame, Series
from typing import Any


def imputer(obj: Any, data: Series) -> Series:
    trans_data = data.to_numpy().reshape(-1, 1)
    imputed_data = Series(obj.fit_transform(trans_data).flatten())
    return imputed_data

