def sep(data: list[str]) -> tuple(list[str], list[str]):
    from collections import Counter
    low_car = []
    high_car = []

    counts = Counter(data)

    for values, count in counts:

    


cardinality_level = {}
for each in catagorical_columns:
    unique_vals = df[each].unique()
    status = "High Cardinality" if len(unique_vals) > 10 else "Low Cardinality"
    cardinality_level.update({each : status})
