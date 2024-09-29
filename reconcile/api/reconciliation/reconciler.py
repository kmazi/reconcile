from typing import Dict, List

import pandas


def extract_missing_records(source: pandas.DataFrame,
                            target: pandas.DataFrame) -> pandas.DataFrame:
    """Extract missing records from a normalized dataframe."""
    df = source[~source['ID'].isin(target['ID'])]
    return df


def extract_missing_columns(source_cols: pandas.Index,
                            target_cols: pandas.Index) -> List:
    """Extract missing columns from a normalized dataframe."""
    diff = source_cols.difference(target_cols).to_list()
    return diff


def extract_common_ids(source: pandas.DataFrame,
                       target: pandas.DataFrame) -> List:
    """Extract common ids from two normalized dataframes."""
    common_ids = list(set(source['ID']) & set(target['ID']))
    return common_ids


def extract_common_records(data: pandas.DataFrame,
                           common_ids: List) -> pandas.DataFrame:
    common_records = data[data['ID'].isin(common_ids)]
    common_records = common_records.sort_values(by=['ID'])
    return common_records


def reconcile_files(source: pandas.DataFrame,
                    target: pandas.DataFrame) -> Dict:
    """Reconcile two dataframes."""
    report = {'source_records_missing_in_target': extract_missing_records(
        source=source, target=target).to_html(),
        'target_records_missing_in_source': extract_missing_records(
        source=target, target=source).to_html(),
        'source_columns_missing_in_target': extract_missing_columns(
            source_cols=source.columns, target_cols=target.columns),
        'target_columns_missing_in_source': extract_missing_columns(
            source_cols=target.columns, target_cols=source.columns)}

    # Extract common ids
    common_ids = extract_common_ids(source=source, target=target)
    # Extract common records
    source_common_records = extract_common_records(
        data=source, common_ids=common_ids)
    target_common_records = extract_common_records(
        data=target, common_ids=common_ids)

    # Get common columns
    common_columns = list(set(source_common_records.columns) & set(
        target_common_records.columns))
    # restrict dataframe to common columns
    source_common_records = source_common_records[common_columns]
    target_common_records = target_common_records[common_columns]
    # Compare source and target dataframes
    result = source_common_records.compare(
        target_common_records, result_names=('source', 'target'))
    report['descrepancies'] = result.to_html()
    return report
