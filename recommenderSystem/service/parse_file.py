import pandas as pd
from collections import defaultdict

path = 'recommenderSystem/file/'

def get_sport_weight_table() -> 'pd.dataframe':
	filename = 'sport_weight.csv'

	return pd.read_csv(path + filename, usecols=['SportCode', 'SportCategoryCode', 'SportTournamentCode', 'BetLimitFactor'])

def get_sport_weight_dict() -> 'dict':
	df = get_sport_weight_table()
	info = defaultdict(dict)
	for i in df.itertuples():
		info[i.SportCode][i.SportTournamentCode] = i.BetLimitFactor

	return info