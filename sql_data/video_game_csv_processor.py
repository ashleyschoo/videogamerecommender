import chardet
import logging
import os
import pandas as pd
import sys as sys


def main(argv=None):
	"""
	Utilize Pandas library to read in video_game.csv file
	(comma delimited). Filter out duplicate values and NaN values and sort the
	series in alphabetical order. Write out each series to a .csv file for inspection.
	"""
	if argv is None:
		argv = sys.argv
	
	msg = [
		'Source file read {0}',	#0
		'Video Game file processed' #1
		'AgeRating {0}', #2
		'GenreCategory {0}', #3
		'NumberofPlayers {0}', #4
		'PopularityRating {0}', #5
		'Videogames written to file {0}' #6
	]

	# Setting logging format and default level
	logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

	# Read Video Game Information data (check encoding)
	video_game_csv = "C:/Users/ashle/OneDrive/Documents/Software Engineering/videogamerecommender/sql_data/input/video_game.csv"
	#'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/input/video_game.csv'

	encoding = find_encoding(video_game_csv)
	video_game_data_frame_untrimmed = read_csv(video_game_csv, encoding, ',')
	logging.info(msg[0].format(os.path.abspath(video_game_csv)))

	video_game_data_frame = trim_columns(video_game_data_frame_untrimmed)
	csv = "C:/Users/ashle/OneDrive/Documents/Software Engineering/videogamerecommender/sql_data/output/video_game_csv_trimmed.csv"
	#'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/output/video_game_csv_trimmed.csv'
	write_series_to_csv(video_game_data_frame, csv, ',', False)
	logging.info(msg[1].format(os.path.abspath(video_game_csv)))	

	# Write AgeRating name to a .csv file
	AgeRating = extract_filtered_series(video_game_data_frame, ['AgeRating'])
	AgeRatingTrimmed = trim_columns(AgeRating)
	AgeRtingStripped = AgeRatingTrimmed.replace({r'\\r\n': ''}, regex=True)
	AgeRating_csv = 'C:/Users/ashle/OneDrive/Documents/Software Engineering/videogamerecommender/sql_data/output/AgeRating.csv'
	write_series_to_csv(AgeRtingStripped, AgeRating_csv, ',', False)
	logging.info(msg[2].format(os.path.abspath(AgeRating_csv)))

	# Write GenreCategory name to a .csv file
	GenreCategory = extract_filtered_series(video_game_data_frame, ['GenreCategory'])
	GenreCategory_csv = 'C:/Users/ashle/OneDrive/Documents/Software Engineering/videogamerecommender/sql_data/output/GenreCategory.csv'
	write_series_to_csv(GenreCategory, GenreCategory_csv, ',', False)
	logging.info(msg[3].format(os.path.abspath(GenreCategory_csv)))

	# Write NumberofPlayers name to a .csv file
	NumberofPlayers = extract_filtered_series(video_game_data_frame, ['NumberofPlayers'])
	#NumberofPlayers_csv = 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/output/NumberofPlayers.csv'
	NumberofPlayers_csv = 'C:/Users/ashle/OneDrive/Documents/Software Engineering/videogamerecommender/sql_data/output/NumberofPlayers.csv'	
	write_series_to_csv(NumberofPlayers, NumberofPlayers_csv, ',', False)
	logging.info(msg[4].format(os.path.abspath(NumberofPlayers_csv)))

	# Write PopularityRating name to a .csv file
	PopularityRating = extract_filtered_series(video_game_data_frame, ['PopularityRating'])
	PopularityRating_csv = 'C:/Users/ashle/OneDrive/Documents/Software Engineering/videogamerecommender/sql_data/output/PopularityRating.csv'
	write_series_to_csv(PopularityRating, PopularityRating_csv, ',', False)
	logging.info(msg[5].format(os.path.abspath(PopularityRating_csv)))	


# 	# Write VideoGameName name to a .csv file
# 	VideoGameName = extract_filtered_series(video_game_data_frame, ['VideoGameName','PC_Windows','PC_MAC','Playstation','NintendoSwitch','Xbox','Phone_Android','Phone_iPhone','Description','YoutubeTrailerLink'
# ])
# 	VideoGameName_csv = 'C:/Users/ashle/OneDrive/Documents/Software Engineering/videogamerecommender/sql_data/output/VideoGameName.csv'
# 	write_series_to_csv(VideoGameName, VideoGameName_csv, ',', False)
# 	logging.info(msg[6].format(os.path.abspath(VideoGameName_csv)))	



def find_encoding(fname):
	r_file = open(fname, 'rb').read()
	result = chardet.detect(r_file)
	charenc = result['encoding']
	return charenc


def read_csv(path, encoding, delimiter=','):
	"""
    Utilize Pandas to read in *.csv file.
    :param path: file path
    :param delimiter: field delimiter
    :return: Pandas DataFrame
    """

	# UnicodeDecodeError: 'utf-8' codec can't decode byte 0x96 in position 450: invalid start byte
	# return pd.read_csv(path, sep=delimiter, encoding='utf-8', engine='python')

	return pd.read_csv(path, sep=delimiter, encoding=encoding, engine='python')
    # return pd.read_csv(path, sep=delimiter, engine='python')


def trim_columns(data_frame):
	"""
	:param data_frame:
	:return: trimmed data frame
	"""
	trim = lambda x: x.strip() if type(x) is str else x
	return data_frame.map(trim)


def write_series_to_csv(series, path, delimiter=',', row_name=True):
	"""
	Write Pandas DataFrame to a *.csv file.
	:param series: Pandas one dimensional ndarray
	:param path: file path
	:param delimiter: field delimiter
	:param row_name: include row name boolean
	"""
	series.to_csv(path, sep=delimiter, index=row_name)



def extract_filtered_series(data_frame, column_list):
	"""
	Returns a filtered Panda Series one-dimensional ndarray from a targeted column.
	Duplicate values and NaN or blank values are dropped from the result set which is
	returned sorted (ascending).
	:param data_frame: Pandas DataFrame
	:param column_list: list of columns
	:return: Panda Series one-dimensional ndarray
	"""

	return data_frame[column_list].drop_duplicates().dropna(axis=0, how='all').sort_values(
		column_list)
	# return data_frame[column_list].str.strip().drop_duplicates().dropna().sort_values()


if __name__ == '__main__':
	sys.exit(main())
