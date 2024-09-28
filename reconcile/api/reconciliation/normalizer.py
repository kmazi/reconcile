import pandas
from django.core.files.uploadedfile import UploadedFile


def normalize_date(col: pandas.Series) -> pandas.Series:
    """convert string date to python date object."""
    return pandas.to_datetime(col, format='%Y-%m-%d').dt.date


def normalize_name(col: pandas.Series) -> pandas.Series:
    """convert name to title case stripping whitespaces."""
    col = col.str.strip().str.title()
    return col


def normalize_amount(col: pandas.Series) -> pandas.Series:
    return col


def normalize(data: UploadedFile) -> pandas.DataFrame:
    """Normalize incoming data."""
    df = pandas.read_csv(data)
    # normalize columns
    for col in df.columns:
        match col:
            case 'Name':
                df[col] = normalize_name(df[col])
            case 'Date':
                df[col] = normalize_date(df[col])
            case 'Amount':
                df[col] = normalize_amount(df[col])
            case _:
                continue
    # Sort dataframe by ID column
    df = df.sort_values(by='ID')
    return df
