"""
script.py
This file contains helper functions for reading nflfastpy data into a
workable pandas dataframe
"""

import logging
import pandas as pd

from typing import List, Optional, Tuple
import constants as c


def build_db() -> None:
    """Function to loop through seasons/tables and write each to the db if data exists.

    Parameters
    ----------
    None.

    Returns
    -------
    None.
    """

    for table in c.ALL_TABLE_NAMES:
        if table in c.SEASONAL_TABLES:
            for season in range(
                c.NFLV_DIR_DICT[table][c.NLFV_START_SEASON_KEY], c.CURRENT_YEAR + 1
            ):
                if season in c.NFLV_DIR_DICT[table][c.NFLV_SEASON_RANGE_KEY]:
                    write_table(table=table, season=season)
                else:
                    logging.info(c.MISSING_SEASON_MESSAGE, season, table)
        else:
            write_table(table=table)


def construct_table_url(
    table: str = c.NFLV_TABLE_DEFAULT,
    year: int = c.CURRENT_YEAR,
    suffix: Optional[str] = None,
) -> Tuple[str, str]:
    """Helper function to build nflverse url from table information.

    Parameters
    ----------
    table : str
        Name of repo subdirectory containing relevant data (default: 'pbp').
    year : int
        Year to read data (default: current year).
    suffix :
        Optional string appended to the end of the url corresponding to
        stat type (one of 'passing_', 'rushing_', or 'receiving_').

    Returns
    -------
    table_url, compression : Tuple[str, str]
        Tuple of the url to read NFLV data from and the compression used to store it.
    """
    base_url = c.NFLV_DIR_DICT[c.NFLV_BASE_KEY][c.NFLV_URL_KEY]
    url_addendum = c.NFLV_DIR_DICT[table][c.NFLV_URL_KEY]
    compression = (
        c.NFLV_DIR_DICT[table][c.NFLV_COMPRESSION_KEY]
        if c.NFLV_COMPRESSION_KEY in c.NFLV_DIR_DICT[table].keys()
        else None
    )
    extension = c.GZIP_EXTENSION if compression else c.CSV_EXTENSION
    url_suffix = suffix if table in c.SUFFIX_TABLES else ""
    url_year = str(year) if table not in c.NON_SEASONAL_TABLES else ""
    table_url = c.URL_STRUCTURE.format(
        base_url=base_url,
        url_addendum=url_addendum,
        year=url_year,
        url_suffix=url_suffix,
        extension=extension,
    )
    return table_url, compression


def read_nflverse_data_year(
    table: str = c.NFLV_TABLE_DEFAULT,
    year: int = c.CURRENT_YEAR,
    stat_type: Optional[str] = None,
) -> pd.DataFrame:
    """Helper function to read any table from nflverse repo.

    Parameters
    ----------
    table : str
        Name of repo subdirectory containing relevant data (default: 'pbp').
    year : int
        Year to read data (default: current year).
    stat_type : Optional[str]
        Optional string indicating stat type.

    Returns
    -------
    data : pd.DataFrame
        Pandas DataFrame of nflverse data.
    """
    suffix = (
        c.NFLV_SUFFIX_DICT[table].format(stat_type=stat_type)
        if table in c.NFLV_SUFFIX_DICT.keys()
        else ""
    )
    table_url, compression = construct_table_url(table=table, suffix=suffix, year=year)
    data = pd.read_csv(table_url, compression=compression, low_memory=False)
    return data


def return_column_names(nflv_data: pd.DataFrame, table_name: str) -> List[str]:
    """Helper function to return column names for each table.

    Parameters
    ----------
    nflv_data : pd.DataFrame
        Pandas DataFrame of NFLVerse information to write to the database.
    table_name : str
        Name of table to write to the database. Options available
        in ff_projections.constants.NFLV_TABLE_DICT.keys().

    Returns
    -------
    column_list : List[str]
        List of columns for writing to the NFLVerse database.
    """
    if table_name == "pbp_player":
        column_list = [
            pbp_column
            for pbp_column in nflv_data.columns
            if any(
                colname_substring in pbp_column for colname_substring in c.PLAYER_COLS
            )
        ]
    elif table_name not in c.NFLV_TABLE_DICT.keys():
        raise KeyError(c.MISSING_TABLE_MESSAGE)
    else:
        column_list = c.NFLV_TABLE_DICT[table_name]
    return column_list


def build_table(nflv_data: pd.DataFrame, table_name: str) -> pd.DataFrame:
    """Helper function to extract table-specific information from pbp data.

    Parameters
    ----------
    nflv_data : pd.DataFrame
        NFLVerse data for database upload.
    table_name :
        Name of table to write to the database. Options available
        in ff_projections.constants.NFLV_TABLE_DICT.keys().

    Returns
    -------
    filtered_data : pd.DataFrame
        Re-indexed pandas DataFrame with only the relevant columns available and
        duplicate rows removed. Ready to be written to the database.
    """
    column_list = return_column_names(nflv_data=nflv_data, table_name=table_name)
    filtered_data = (
        nflv_data.filter(column_list, axis=1).drop_duplicates().reset_index(drop=True)
    )
    return filtered_data


def write_table(table: str, season: Optional[int] = None) -> None:
    return table, season
