import pandas
from django.core.files.uploadedfile import UploadedFile
from rest_framework.exceptions import APIException


def normalize_date(col: pandas.Series) -> pandas.Series:
    """convert string date to python date object."""
    return pandas.to_datetime(col, format='%Y-%m-%d').dt.date


def normalize_name(col: pandas.Series) -> pandas.Series:
    """convert name to title case stripping whitespaces."""
    col = col.str.strip().str.title()
    return col


def normalize_amount(col: pandas.Series) -> pandas.Series:
    return col


def normalize(data: UploadedFile, name='') -> pandas.DataFrame:
    """Normalize incoming data."""
    try:
        df = pandas.read_csv(data)
    except (pandas.errors.ParserError, UnicodeDecodeError):
        raise APIException(f'Invalid {name} file format: Please upload csv files.')

    # normalize columns
    for col in df.columns:
        match col:
            case 'Name':
                df[col] = normalize_name(df[col])
            case 'Date':
                try:
                    df[col] = normalize_date(df[col])
                except ValueError as e:
                    raise APIException(
                        f'Invalid date format present in Date column of {name} file')
            case 'Amount':
                df[col] = normalize_amount(df[col])
            case _:
                continue
    # Sort dataframe by ID column
    try:
        df = df.sort_values(by='ID')
    except KeyError as e:
        raise APIException(f'{str(e)} column not found or is not ID column.')
    return df
