from fastapi import APIRouter
from fastapi import Request
from recommenderSystem.viewmodel.tournament import tournament_data, tournament_rank
from recommenderSystem.domainmodel.tournament import tournament
from recommenderSystem.service import data_pipe


router = APIRouter()


@router.post("/predict/tournament_prematch/", tags=["non personalized"])
def get_tournament_prematch(inputs: tournament_data):
    if not inputs:
        return {'error': 'contain at least one data'}

    converted = _convert_tournament_input(inputs.dict())
    rank_list = data_pipe.tournament_prematch(converted)
    return tournament_rank(data=rank_list)


@router.post("/predict/tournament_live", tags=["non personalized"])
def get_tournament_live(inputs: tournament_data):
    if not inputs:
        return {'error': 'contain at least one data'}

    converted = _convert_tournament_input(inputs.dict())
    rank_list = data_pipe.tournament_live(converted)
    return tournament_rank(data=rank_list)


def _convert_tournament_input(inputs) -> 'tournament model':
    dic_list = inputs['data']

    sportid_list = [i['sportid'] for i in dic_list]
    tournamentid_list = [i['tournamentid'] for i in dic_list]
    date_list = [i['date'] for i in dic_list]

    return tournament(sportid_list=sportid_list,
                   tournamentid_list=tournamentid_list,
                   date_list=date_list)

