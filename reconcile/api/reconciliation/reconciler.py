from typing import List

import pandas
from rest_framework.exceptions import APIException


def extract_missing_records(source: pandas.DataFrame,
                            target: pandas.DataFrame) -> pandas.DataFrame:
    try:
        df = source[~source['ID'].isin(target['ID'])]
    except KeyError as e:
        raise APIException(f'{str(e)} column not found or is not ID column.')
    return df


def extract_common_ids(source: pandas.DataFrame, target: pandas.DataFrame) -> List:
    try:
        common_ids = list(set(source['ID']) & set(target['ID']))
    except KeyError as e:
        raise APIException(f'{str(e)} column not found or is not ID column.')
    return common_ids


def extract_common_records(data: pandas.DataFrame, common_ids: List) -> pandas.DataFrame:
    common_records = data[data['ID'].isin(common_ids)]
    common_records = common_records.sort_values(by=['ID'])
    return common_records


def reconcile_files(source: pandas.DataFrame, target: pandas.DataFrame):
    """Reconcile two dataframes."""
    report = {'source_records_missing_in_target': extract_missing_records(
        source=source, target=target),
        'target_records_missing_in_source': extract_missing_records(
        source=target, target=source), }

    # Extract common ids
    common_ids = extract_common_ids(source=source, target=target)
    # Extract common records
    source_common_records = extract_common_records(
        data=source, common_ids=common_ids)
    target_common_records = extract_common_records(
        data=target, common_ids=common_ids)

    # Compare source and target dataframes
    result = source_common_records.compare(target_common_records)
    report['descrepancies'] = result.to_dict(orient='split')
    return report
