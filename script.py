"""
script.py
This file contains helper functions for reading nflfastpy data into a
workable pandas dataframe
"""

import logging
import pandas as pd

from typing import Optional

from constants import (
	CSV_EXTENSION,
	CURRENT_YEAR,
	GZIP_EXTENSION,
	NFLV_BASE_KEY,
	NFLV_COMPRESSION_KEY,
	NFLV_DIR_DICT,
	NFLV_URL_KEY,
	NON_SEASONAL_TABLES,
	NFLV_SUFFIX_DICT,
	NFLV_TABLE_DEFAULT,
	SUFFIX_TABLES,
	URL_STRUCTURE,
)


all_tbl_names = list(NFLV_DIR_DICT.keys())
print(all_tbl_names)

table = "weekly_rosters"
year = 2021
stat_type = None
data = _read_nflverse_data_year(table=table, year=year, stat_type=stat_type)


def build_db() -> None:
	"""Function to loop through seasons/tables and write each to the db if data exists"""
	all_table_names = [key for key in NFLV_DIR_DICT.keys() if key != NFLV_BASE_KEY]
	for season in range(NFLV_DIR_DICT[NFLV_BASE_KEY][NLFV_START_SEASON_KEY], CURRENT_YEAR+1):
		for table in all_table_names:
			if season in NFLV_DIR_DICT[table][NFLV_SEASON_RANGE_KEY]:
				_write_table(table=table, season=season)
			else:
				pass


def _construct_table_url(table: str=NFLV_TABLE_DEFAULT, year: int=CURRENT_YEAR, suffix: Optional[str]=None) -> str:
	"""
	Helper function to build nflverse url from table information

	:param table: name of repo subdirectory containing relevant data (default: 'pbp')
	:param year: year to read data (default: current year)
	:param suffix: optional string appended to the end of the url corresponding to 
		stat type (one of 'passing_', 'rushing_', or 'receiving_')
	:param extension: 
	"""
	base_url = NFLV_DIR_DICT[NFLV_BASE_KEY][NFLV_URL_KEY]
	url_addendum = NFLV_DIR_DICT[table][NFLV_URL_KEY]
	compression = NFLV_DIR_DICT[table][NFLV_COMPRESSION_KEY] if NFLV_COMPRESSION_KEY in NFLV_DIR_DICT[table].keys() else None
	extension = GZIP_EXTENSION if compression else CSV_EXTENSION
	url_suffix = suffix if table in SUFFIX_TABLES else ""
	url_year = str(year) if table not in NON_SEASONAL_TABLES else ""
	table_url = URL_STRUCTURE.format(
		base_url=base_url, 
		url_addendum=url_addendum, 
		year=year, 
		url_suffix=url_suffix, 
		extension=extension
	)
	return table_url, compression


def _read_nflverse_data_year(
	table: str=NFLV_TABLE_DEFAULT, 
	year: int=CURRENT_YEAR, 
	stat_type: Optional[str]=None
) -> pd.DataFrame:
	"""
	Helper function to read any table from nflverse repo

	:param table: name of repo subdirectory containing relevant data (default: 'pbp')
	:param year: year to read data (default: current year)
	:param stat_type: optional string indicating stat type
	:return: pandas dataframe of nflverse data
	"""
	suffix = NFLV_SUFFIX_DICT[table].format(stat_type=stat_type) if table in NFLV_SUFFIX_DICT.keys() else ""
	table_url, compression = _construct_table_url(table=table, suffix=suffix, year=year)
	data = pd.read_csv(table_url, compression=compression, low_memory=False)
	return data


def _build_drive_table(pbp_data: pd.DataFrame) -> pd.DataFrame:
	"""
	Helper function to extract drive information from pbp data

	:param pbp_data: play-by-play data for extracting drive info
	:return: dataframe with drive info 
	"""
	drive_data = pbp_data.filter(DRIVE_TBL_COLUMNS, axis=1).drop_duplicates().reset_index(drop=True)
	return drive_data


def _build_games_table(pbp_data: pd.DataFrame) -> pd.DataFrame:
	"""
	Helper function to extract game information from pbp data

	:param pbp_data: play-by-play data for extracting game info
	:return: dataframe with game info 
	"""
	game_data = pbp_data.filter(GAME_TBL_COLUMNS, axis=1).drop_duplicates().reset_index(drop=True)
	return game_data


def _build_pbp_table(pbp_data: pd.DataFrame) -> pd.DataFrame:
	"""
	Helper function to subset pbp data to relevant columns

	:param pbp_data: play-by-play data for extracting game info
	:return: dataframe with pbp info to write to sqlite 
	"""
	pbp_data = pbp_data.filter(PBP_TBL_COLUMNS, axis=1)
	return pbp_data


def _build_pbp_player_table(pbp_data: pd.DataFrame) -> pd.DataFrame:
	"""
	Helper function to extract play-level player involvement information from pbp data

	:param pbp_data: play-by-play data for extracting player involvement info
	:return: dataframe with pbp player info 
	"""
	player_id_columns = [
		pbp_column for pbp_column in pbp_data.columns 
		if any(colname_substring in pbp_column for colname_substring in PLAYER_COLS)
	]
	pbp_player_data = pbp_data.filter(player_id_columns, axis=1)
	return pbp_player_data


def _build_pbp_probabilities_table(pbp_data: pd.DataFrame) -> pd.DataFrame:
	"""
	Helper function to extract outcome probability information from pbp data

	:param pbp_data: play-by-play data for extracting outcome probability info
	:return: dataframe with outcome probability info 
	"""
	pbp_probability_data = pbp_data.filter(PBP_PROBABILITIES_TBL_COLUMNS, axis=1)
	return pbp_probability_data
