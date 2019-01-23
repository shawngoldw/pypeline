def drop_column(data, col):
    return data.drop(col, axis=1)


def replace_value(data, col, find, replace):
    data[col] = data[col].replace(find, replace)
    return data