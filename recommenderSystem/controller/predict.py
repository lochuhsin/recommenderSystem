from fastapi import APIRouter
from fastapi import Request
from recommenderSystem.viewmodel.tournament import tournament_data, tournament_rank
from recommenderSystem.viewmodel.user import user_data
from recommenderSystem.domainmodel.tournament import tournament
from recommenderSystem.domainmodel.user import user
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


@router.post("/predict/user_preference", tags=["personalized"])
def get_user_preference(inputs: user_data):
    supported_methods = {'user_user'}
    if inputs.method not in supported_methods:
        return {'error': 'input method not supproted'}

    converted = _convert_user_input(inputs.dict())


def _convert_user_input(inputs) -> 'user model':
    user_list = inputs['users']
    user_id_list = [i['user_id'] for i in user_list]
    method = inputs['method']

    return user(userid_list=user_id_list, method=method)

def _convert_tournament_input(inputs) -> 'tournament model':
    dic_list = inputs['data']

    sportid_list = [i['sportid'] for i in dic_list]
    tournamentid_list = [i['tournamentid'] for i in dic_list]
    date_list = [i['date'] for i in dic_list]

    return tournament(sportid_list=sportid_list,
                   tournamentid_list=tournamentid_list,
                   date_list=date_list)

