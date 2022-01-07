from recommenderSystem.service import data_source
from recommenderSystem.model.non_personalize import tournament_prematch as t_prematch_model
from recommenderSystem.model.non_personalize import tournament_live as t_live_model


def tournament_prematch(data: 'tournamet domain model') -> list:

	x = data_source.tournament_prematch(data.sportid_list, data.tournamentid_list, data.date_list)
	model = t_prematch_model()
	y = model.predict(x)
	return list(y)


def tournament_live(data: 'tournamet domain model') -> list:

	x = data_source.tournament_live(data.sportid_list, data.tournamentid_list, data.date_list)
	model = t_live_model()
	y = model.predict(x)
	return list(y)
