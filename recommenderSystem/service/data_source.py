import numpy as np
from datetime import datetime
from recommenderSystem.service import parse_file


_Weight_Dict = parse_file.get_sport_weight_dict()


def tournament_prematch(sportid: list, sportTournamentcode: list, date: list) -> 'ndarray':
	sec_list = _date_transform(date)
	weight_list = _weight_transform(sportid, sportTournamentcode)
	return np.column_stack([sec_list, weight_list])  # (n, 2)


def tournament_live(sportid: list, sportTournamentcode: list, duration: list) -> 'ndarray':
	sec_list = [float(i) for i in duration]
	weight_list = _weight_transform(sportid, sportTournamentcode)
	return np.column_stack([sec_list, weight_list])  # (n, 2)


def _date_transform(date_list: list):
	sec_list = []
	for date in date_list:
		timedelta = datetime.strptime(date, "%Y-%m-%d %H:%M:%S") - datetime.now()
		sec_list.append(timedelta.total_seconds())

	return sec_list


def _weight_transform(sportid_list: list, sportTournamentcode_list: list)->int:

	weight_list = []
	for sportid, sportTournamentcode in zip(sportid_list, sportTournamentcode_list):

		weight = 1
		if sportid in _Weight_Dict and sportTournamentcode in _Weight_Dict[sportid]:
			weight = _Weight_Dict[sportid][sportTournamentcode]

		weight_list.append(weight)
	return weight_list
