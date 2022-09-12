"""
constants.py
This file contains some constants shared across our modules
"""

import datetime as dt

#########
# dates #
#########

TODAY = dt.datetime.today()
CURRENT_YEAR = TODAY.year if TODAY.month < 8 else TODAY.year - 1

##########################
# nflverse url addendums #
##########################

NFLV_BASE_URL = "https://github.com/nflverse/nflverse-data/releases/download/"
NFLV_COMBINE_URL_ADDENDUM = "combine/combine"
NFLV_CONTRACTS_URL_ADDENDUM = "contracts/historical_contracts"
NFLV_DEPTH_CHARTS_URL_ADDENDUM = "depth_charts/depth_charts_"
NFLV_DRAFT_PICKS_URL_ADDENDUM = "draft_picks/draft_picks"
NFLV_INJURIES_URL_ADDENDUM = "injuries/injuries_"
NFLV_NGS_URL_ADDENDUM = "nextgen_stats/ngs_"
NFLV_OFFICIALS_URL_ADDENDUM = "officials/officials"
NFLV_PBP_URL_ADDENDUM = "pbp/play_by_play_"
NFLV_PBP_PARTICIPATION_URL_ADDENDUM = "pbp_participation/pbp_participation_"
NFLV_PFR_URL_ADDENDUM = "pfr_advstats/advstats_week_"
NFLV_PLAYERS_URL_ADDENDUM = "players/players"
NFLV_PLAYER_STATS_URL_ADDENDUM = "player_stats/player_stats_"
NFLV_ROSTERS_URL_ADDENDUM = "rosters/roster_"
NFLV_SNAP_COUNT_URL_ADDENDUM = "snap_counts/snap_counts_"
NFLV_WEEKLY_ROSTER_URL_ADDENDUM = "weekly_rosters/roster_weekly_"

##########################
# nflverse start seasons #
##########################

NFLV_BASE_START_SEASON = 1999
NFLV_DEPTH_CHARTS_START_SEASON = 2001
NFLV_NGS_START_SEASON = 2016
NFLV_PBP_START_SEASON = 1999
NFLV_PBP_PARTICIPATION_START_SEASON = 2016
NFLV_PFR_START_SEASON = 2018
NFLV_PLAYER_STATS_START_SEASON = 1999
NFLV_SNAP_COUNT_START_SEASON = 2012
NFLV_WEEKLY_ROSTER_START_SEASON = 2002

###########################
# reading compressed csvs #
###########################

CSV_EXTENSION = ".csv"
GZIP_EXTENSION = ".csv.gz"

#####################
# nflverse metadata #
#####################

NFLV_BASE_KEY = "base"
NFLV_COMPRESSION_KEY = "compression"
NFLV_SEASON_RANGE_KEY = "season_range"
NLFV_START_SEASON_KEY = "start_season"
NFLV_URL_KEY = "url"

NFLV_TABLE_DEFAULT = "pbp"
NFLV_TABLE_NGS = "nextgen_stats"
NFLV_TABLE_PFR = "pfr_advstats"

NFLV_SUFFIX_DICT = {
	NFLV_TABLE_NGS: "_{stat_type}",
	NFLV_TABLE_PFR: "{stat_type}_"
}

NON_SEASONAL_TABLES = ["combine", "contracts", "draft_picks", "officials", "players"]

SUFFIX_TABLES = ["pfr_advstats"]
URL_STRUCTURE = "{base_url}{url_addendum}{year}{url_suffix}{extension}"

NFLV_DIR_DICT = {
	"base": {
		"url": NFLV_BASE_URL,
		"start_season": NFLV_BASE_START_SEASON
	},
	"combine": {
		"url": NFLV_COMBINE_URL_ADDENDUM
	},
	"contracts": {
		"url": NFLV_CONTRACTS_URL_ADDENDUM, 
		"compression": "gzip"
	},
	"depth_charts": {
		"url": NFLV_DEPTH_CHARTS_URL_ADDENDUM, 
		"season_range": range(NFLV_DEPTH_CHARTS_START_SEASON, CURRENT_YEAR+1)
	},
	"draft_picks": {
		"url": NFLV_DRAFT_PICKS_URL_ADDENDUM
	},
	"nextgen_stats": {
		"url": NFLV_NGS_URL_ADDENDUM, 
		"season_range": range(NFLV_NGS_START_SEASON, CURRENT_YEAR+1), 
		"compression": "gzip"
	},
	"pbp": {
		"url": NFLV_PBP_URL_ADDENDUM, 
		"season_range": range(NFLV_PBP_START_SEASON, CURRENT_YEAR+1), 
		"compression": "gzip"
	},
	"pbp_participation": {
		"url": NFLV_PBP_PARTICIPATION_URL_ADDENDUM, 
		"season_range": range(NFLV_PBP_PARTICIPATION_START_SEASON, CURRENT_YEAR+1)
	},
	"pfr_advstats": {
		"url": NFLV_PFR_URL_ADDENDUM, 
		"season_range": range(NFLV_PFR_START_SEASON, CURRENT_YEAR+1)
	},
	"player_stats": {
		"url": NFLV_PLAYER_STATS_URL_ADDENDUM, 
		"season_range": range(NFLV_PLAYER_STATS_START_SEASON, CURRENT_YEAR+1), 
		"compression": "gzip"
	},
	"snap_counts": {
		"url": NFLV_SNAP_COUNT_URL_ADDENDUM, 
		"season_range": range(NFLV_SNAP_COUNT_START_SEASON, CURRENT_YEAR+1)
	},
	"weekly_rosters": {
		"url": NFLV_WEEKLY_ROSTER_URL_ADDENDUM, 
		"season_range": range(NFLV_WEEKLY_ROSTER_START_SEASON, CURRENT_YEAR+1)
	},
}

##################
# renaming dicts #
##################

PBP_RENAME_DICT = {
	"time": "play_time",
	"desc": "play_desc"
}

##################
# subset columns #
##################

PLAYER_COLS = ["player_id", "player_name"]

COMBINE_TBL_COLUMNS = [
	"season",
	"draft_year",
	"draft_team",
	"draft_round",
	"draft_ovr",
	"pfr_id",
	"cfb_id",
	"player_name",
	"pos",
	"school",
	"ht",
	"wt",
	"forty",
	"bench",
	"vertical",
	"broad_jump",
	"cone",
	"shuttle",
]


CONTRACTS_TBL_COLUMNS = [
	"player",
	"position",
	"team",
	"is_active",
	"year_signed",
	"years",
	"value",
	"apy",
	"guaranteed",
	"apy_cap_pct",
	"inflated_value",
	"inflated_apy",
	"inflated_guaranteed",
	"player_page",
	"otc_id",
	"date_of_birth",
	"height",
	"weight",
	"college",
	"draft_year",
	"draft_round",
	"draft_overall",
	"draft_team",
	"season_history",
]


DRAFT_TBL_COLUMNS = [
	"season",
	"club_code",
	"week",
	"game_type",
	"depth_team",
	"last_name",
	"first_name",
	"football_name",
	"formation",
	"gsis_id",
	"jersey_number",
	"position",
	"elias_id",
	"depth_position",
	"full_name",
]


GAME_TBL_COLUMNS = [
	"game_id",
	"game_date",
	"season",
	"season_type",
	"week",
	"start_time",
	"stadium",
	"stadium_id",
	"weather",
	"roof",
	"surface",
	"temp",
	"wind",
	"nfl_api_id",
	"home_team",
	"away_team",
	"home_coach",
	"away_coach",
]


DRAFT_PICKS_TBL_COLUMNS = [
	"season", 
	"round",
	"pick",
	"team", 
	"gsis_id",
	"pfr_player_id",
	"cfb_player_id",
	"pfr_player_name",
	"hof",
	"position",
	"category",
	"side",
	"college",
	"age",
	"to",
	"allpro",
	"probowls",
	"seasons_started",
	"w_av",
	"car_av",
	"dr_av",
	"games",
	"pass_completions",
	"pass_attempts",
	"pass_yards",
	"pass_tds",
	"pass_ints",
	"rush_atts",
	"rush_yards",
	"rush_tds",
	"receptions",
	"rec_yards",
	"rec_tds",
	"def_solo_tackles",
	"def_ints",
	"def_sacks",
]


DRIVE_TBL_COLUMNS = [
	"game_id",
	"fixed_drive",
	"fixed_drive_result",
	"drive_real_start_time",
	"drive_play_count",
	"drive_time_of_possession",
	"drive_first_downs",
	"drive_inside20",
	"drive_ended_with_score",
	"drive_quarter_start",
	"drive_quarter_end",
	"drive_yards_penalized",
	"drive_start_transition",
	"drive_end_transition",
	"drive_game_clock_start",
	"drive_game_clock_end",
	"drive_start_yard_line",
	"drive_end_yard_line",
	"drive_play_id_started",
	"drive_play_id_ended",
]


NGS_PASSING_TBL_COLUMNS = [
	"season",
	"season_type",
	"week" ,
	"player_display_name",
	"player_position",
	"team_abbr",
	"avg_time_to_throw",
	"avg_completed_air_yards",
	"avg_intended_air_yards",
	"avg_air_yards_differential",
	"aggressiveness",
	"max_completed_air_distance",
	"avg_air_yards_to_sticks",
	"attempts",
	"pass_yards",
	"pass_touchdowns",
	"interceptions",
	"passer_rating",
	"completions",
	"completion_percentage",
	"expected_completion_percentage",
	"completion_percentage_above_expectation",
	"avg_air_distance",
	"max_air_distance",
	"player_gsis_id",
	"player_first_name",
	"player_last_name",
	"player_jersey_number",
	"player_short_name",
]


NGS_RECEIVING_TBL_COLUMNS = [
	"season",
	"season_type",
	"week",
	"player_display_name",
	"player_position",
	"team_abbr",
	"avg_cushion",
	"avg_separation",
	"avg_intended_air_yards",
	"percent_share_of_intended_air_yards",
	"receptions",
	"targets",
	"catch_percentage",
	"yards",
	"rec_touchdowns",
	"avg_yac",
	"avg_expected_yac",
	"avg_yac_above_expectation",
	"player_gsis_id",
	"player_first_name",
	"player_last_name",
	"player_jersey_number",
	"player_short_name",
]


NGS_RUSHING_TBL_COLUMNS = [
	"season",
	"season_type",
	"week",
	"player_display_name",
	"player_position",
	"team_abbr",
	"efficiency",
	"percent_attempts_gte_eight_defenders",
	"avg_time_to_los",
	"rush_attempts",
	"rush_yards",
	"expected_rush_yards",
	"rush_yards_over_expected",
	"avg_rush_yards",
	"rush_yards_over_expected_per_att",
	"rush_pct_over_expected",
	"rush_touchdowns",
	"player_gsis_id",
	"player_first_name",
	"player_last_name",
	"player_jersey_number",
	"player_short_name",
]


PBP_TBL_COLUMNS = [
	"play_id",
	"game_id",
	"game_date",
	"season",
	"posteam",
	"defteam",
	"side_of_field",
	"yardline_100",
	"quarter_seconds_remaining",
	"half_seconds_remaining",
	"game_seconds_remaining",
	"game_half",
	"quarter_end",
	"sp",
	"qtr",
	"series",
	"fixed_drive",
	"down",
	"goal_to_go",
	"yrdln",
	"ydstogo",
	"ydsneg",
	"play_time",
	"play_desc",
	"play_type",
	"pass",
	"rush",
	"first_down",
	"special",
	"play",
	"yards_gained",
	"out_of_bounds",
	"shotgun",
	"no_huddle",
	"qb_dropback",
	"qb_kneel",
	"qb_spike",
	"qb_scramble",
	"pass_length",
	"pass_location",
	"air_yards",
	"yards_after_catch",
	"run_location",
	"run_gap",
	"field_goal_result",
	"kick_distance",
	"extra_point_result",
	"two_point_conv_result",
	"home_timeouts_remaining",
	"away_timeouts_remaining",
	"timeout",
	"timeout_team",
	"td_team",
	"td_player_name",
	"td_player_id",
	"total_home_score",
	"total_away_score",
	"score_differential",
	"posteam_score_post",
	"defteam_score_post",
	"score_differential_post",
	"punt_blocked",
	"first_down_rush",
	"first_down_pass",
	"first_down_penalty",
	"third_down_converted",
	"third_down_failed",
	"fourth_down_converted",
	"fourth_down_failed",
	"incomplete_pass",
	"touchback",
	"interception",
	"punt_inside_twenty",
	"punt_in_endzone",
	"punt_out_of_bounds",
	"punt_downed",
	"punt_fair_catch",
	"kickoff_inside_twenty",
	"kickoff_in_endzone",
	"kickoff_out_of_bounds",
	"kickoff_downed",
	"kickoff_fair_catch",
	"fumble_forced",
	"fumble_not_forced",
	"fumble_out_of_bounds",
	"solo_tackle",
	"safety",
	"penalty",
	"tackled_for_loss",
	"fumble_lost",
	"own_kickoff_recovery",
	"own_kickoff_recovery_td",
	"qb_hit",
	"rush_attempt",
	"pass_attempt",
	"sack", 
	"touchdown", 
	"pass_touchdown",
	"rush_touchdown",
	"return_touchdown",
	"extra_point_attempt",
	"two_point_attempt",
	"field_goal_attempt",
	"kickoff_attempt", 
	"punt_attempt", 
	"fumble", 
	"complete_pass",
	"assist_tackle", 
	"lateral_reception", 
	"lateral_receiving_yards",
	"lateral_rush", 
	"lateral_return",
	"lateral_recovery",
	"passing_yards",
	"receiving_yards",
	"rushing_yards",
	"tackle_with_assist",
	"return_team",
	"return_yards", 
	"penalty_team",
	"replay_or_challenge_result", 
	"penalty_type",
	"defensive_two_point_attempt",
	"defensive_two_point_conv",
	"defensive_extra_point_attempt",
	"defensive_extra_point_conv",
	"home_opening_kickoff",
]


PBP_PARTICIPATION_TBL_COLUMNS = [
	"old_game_id",
	"play_id",
	"possession_team",
	"offense_formation",
	"offense_personnel",
	"defenders_in_box",
	"defense_personnel",
	"number_of_pass_rushers",
	"offense_players",
	"n_offense",
	"defense_players",
	"n_defense",
]


PBP_PLAYER_TBL_COLUMNS = [
	"play_id",
	"game_id",
	"safety_player_id",
	"passer_player_id",
	"receiver_player_id",
	"rusher_player_id",
	"lateral_receiver_player_id",
	"lateral_rusher_player_id",
	"lateral_rushing_yards",
	"lateral_sack_player_id",
	"interception_player_id",
	"lateral_interception_player_id",
	"punt_returner_player_id",
	"lateral_punt_returner_player_id",
	"kickoff_returner_player_id",
	"lateral_kickoff_returner_player_id",
	"punter_player_id",
	"kicker_player_id",
	"own_kickoff_recovery_player_id",
	"blocked_player_id",
	"tackle_for_loss_1_player_id",
	"tackle_for_loss_2_player_id",
	"qb_hit_1_player_id",
	"qb_hit_2_player_id",
	"forced_fumble_player_1_team",
	"forced_fumble_player_1_player_id",
	"forced_fumble_player_2_team",
	"forced_fumble_player_2_player_id",
	"solo_tackle_1_team",
	"solo_tackle_2_team",
	"solo_tackle_1_player_id",
	"solo_tackle_2_player_id", 
	"assist_tackle_1_player_id", 
	"assist_tackle_1_team", 
	"assist_tackle_2_player_id", 
	"assist_tackle_2_team", 
	"assist_tackle_3_player_id", 
	"assist_tackle_3_team", 
	"assist_tackle_4_player_id", 
	"assist_tackle_4_team",  
	"tackle_with_assist_1_player_id", 
	"tackle_with_assist_1_team", 
	"tackle_with_assist_2_player_id",  
	"tackle_with_assist_2_team",
	"pass_defense_1_player_id", 
	"pass_defense_2_player_id",  
	"fumbled_1_team",
	"fumbled_1_player_id",  
	"fumbled_2_player_id", 
	"fumbled_2_team", 
	"fumble_recovery_1_team",
	"fumble_recovery_1_yards", 
	"fumble_recovery_1_player_id", 
	"fumble_recovery_2_team",
	"fumble_recovery_2_yards", 
	"fumble_recovery_2_player_id", 
	"sack_player_id", 
	"half_sack_1_player_id",  
	"half_sack_2_player_id", 
	"penalty_player_id", 
]


PBP_PROBABILITIES_TBL_COLUMNS = [
	"play_id",
	"game_id",
	"no_score_prob",
	"opp_fg_prob",
	"opp_safety_prob",
	"opp_td_prob",
	"fg_prob",
	"safety_prob",
	"td_prob",
	"extra_point_prob",
	"two_point_conversion_prob",
	"ep",
	"epa",
	"total_home_epa",
	"total_away_epa",
	"total_home_rush_epa",
	"total_away_rush_epa",
	"total_home_pass_epa",
	"total_away_pass_epa",
	"air_epa",
	"yac_epa",
	"comp_air_epa",
	"comp_yac_epa",
	"total_home_comp_air_epa",
	"total_away_comp_air_epa",
	"total_home_comp_yac_epa",
	"total_away_comp_yac_epa",
	"total_home_raw_air_epa",
	"total_away_raw_air_epa",
	"total_home_raw_yac_epa",
	"total_away_raw_yac_epa",
	"wp",
	"def_wp",
	"home_wp",
	"away_wp",
	"wpa",
	"vegas_wpa",
	"vegas_home_wpa",
	"home_wp_post",
	"away_wp_post",
	"vegas_wp",
	"vegas_home_wp",
	"total_home_rush_wpa",
	"total_away_rush_wpa",
	"total_home_pass_wpa",
	"total_away_pass_wpa",
	"air_wpa",
	"yac_wpa",
	"comp_air_wpa",
	"comp_yac_wpa",
	"total_home_comp_air_wpa",
	"total_away_comp_air_wpa",
	"total_home_comp_yac_wpa",
	"total_away_comp_yac_wpa",
	"total_home_raw_air_wpa",
	"total_away_raw_air_wpa",
	"total_home_raw_yac_wpa",
	"total_away_raw_yac_wpa",
	"qb_epa",
	"xyac_epa",
	"xyac_mean_yardage",
	"xyac_median_yardage",
	"xyac_success",
	"xyac_fd",
	"xpass",
	"pass_oe",
]


PFR_DEFENSE_TBL_COLUMNS = [
	"game_id",
	"pfr_game_id",
	"season",
	"week",
	"game_type",
	"team",
	"opponent",
	"pfr_player_name",
	"pfr_player_id",
	"def_ints",
	"def_targets",
	"def_completions_allowed",
	"def_completion_pct",
	"def_yards_allowed",
	"def_yards_allowed_per_cmp",
	"def_yards_allowed_per_tgt",
	"def_receiving_td_allowed",
	"def_passer_rating_allowed",
	"def_adot",
	"def_air_yards_completed",
	"def_yards_after_catch",
	"def_times_blitzed",
	"def_times_hurried",
	"def_times_hitqb",
	"def_sacks",
	"def_pressures",
	"def_tackles_combined",
	"def_missed_tackles",
	"def_missed_tackle_pct",
]


PFR_PASSING_TBL_COLUMNS = [
	"game_id", 
	"pfr_game_id", 
	"season", 
	"week", 
	"game_type", 
	"team",
	"opponent", 
	"pfr_player_name", 
	"pfr_player_id", 
	"passing_drops",
	"passing_drop_pct", 
	"receiving_drop", 
	"receiving_drop_pct",
	"passing_bad_throws", 
	"passing_bad_throw_pct", 
	"times_sacked",
	"times_blitzed", 
	"times_hurried", 
	"times_hit", 
	"times_pressured",
	"times_pressured_pct", 
	"def_times_blitzed", 
	"def_times_hurried",
	"def_times_hitqb",
]


PFR_RECEIVING_TBL_COLUMNS = [
	"game_id",
	"pfr_game_id",
	"season",
	"week",
	"game_type",
	"team",
	"opponent",
	"pfr_player_name",
	"pfr_player_id",
	"rushing_broken_tackles",
	"receiving_broken_tackles",
	"passing_drops",
	"passing_drop_pct",
	"receiving_drop",
	"receiving_drop_pct",
	"receiving_int",
	"receiving_rat",
]


PLAYER_STATS_TBL_COLUMNS = [
	"player_id",
	"player_name",
	"recent_team",
	"season",
	"week",
	"season_type",
	"completions",
	"attempts",
	"passing_yards",
	"passing_tds",
	"interceptions",
	"sacks",
	"sack_yards",
	"sack_fumbles",
	"sack_fumbles_lost",
	"passing_air_yards",
	"passing_yards_after_catch",
	"passing_first_downs",
	"passing_epa",
	"passing_2pt_conversions",
	"pacr",
	"dakota",
	"carries",
	"rushing_yards",
	"rushing_tds",
	"rushing_fumbles",
	"rushing_fumbles_lost",
	"rushing_first_downs",
	"rushing_epa",
	"rushing_2pt_conversions",
	"receptions",
	"targets",
	"receiving_yards",
	"receiving_tds",
	"receiving_fumbles",
	"receiving_fumbles_lost",
	"receiving_air_yards",
	"receiving_yards_after_catch",
	"receiving_first_downs",
	"receiving_epa",
	"receiving_2pt_conversions",
	"racr",
	"target_share",
	"air_yards_share",
	"wopr",
	"special_teams_tds",
	"fantasy_points",
	"fantasy_points_ppr",
]


RUSHING_TBL_COLUMNS = [
	"game_id",
	"pfr_game_id", 
	"season", 
	"week", 
	"game_type", 
	"team",
	"opponent", 
	"pfr_player_name", 
	"pfr_player_id", 
	"carries",
	"rushing_yards_before_contact", 
	"rushing_yards_before_contact_avg",
	"rushing_yards_after_contact", 
	"rushing_yards_after_contact_avg",
	"rushing_broken_tackles", 
	"receiving_broken_tackles",
]

WEEKLY_ROSTERS_TBL_COLUMNS = [
	"season",
	"team",
	"position",
	"depth_chart_position",
	"jersey_number",
	"status",
	"full_name",
	"first_name",
	"last_name",
	"birth_date",
	"height",
	"weight",
	"college",
	"gsis_id",
	"espn_id",
	"sportradar_id",
	"yahoo_id",
	"rotowire_id",
	"pff_id",
	"pfr_id",
	"fantasy_data_id",
	"sleeper_id",
	"years_exp",
	"headshot_url",
	"ngs_position",
	"week",
	"game_type",
	"status_description_abbr",
	"football_name",
	"esb_id",
	"gsis_it_id",
	"smart_id",
	"entry_year",
	"rookie_year",
	"draft_club",
	"draft_number",
]


######################
# table column dicts #
######################

NFLV_TABLE_DICT = {
	"drive": DRIVE_TBL_COLUMNS,
	"game": GAME_TBL_COLUMNS,
	"pbp": PBP_TBL_COLUMNS,
	"pbp_player": PBP_PLAYER_TBL_COLUMNS,
	"pbp_probabilities": PBP_PROBABILITIES_TBL_COLUMNS,
}