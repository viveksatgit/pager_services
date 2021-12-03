from models import Team, Developer
from main import data_manager
import requests

team_constant = 1
developer_constant = 1


def _get_team_id(team_name):
    return team_name + str(team_constant)


def _get_developer_id(developer_name):
    return developer_name + str(team_constant)


def create_team(team_object):
    global team_constant, developer_constant
    team_name = team_object['team']['name']
    team_id = _get_team_id(team_name)
    team = Team(team_id, team_name)
    data_manager.add_team(team_id, team)
    team_constant += 1

    for developer_object in team_object['developers']:
        developer_id = _get_developer_id(developer_object['name'])
        developer = Developer(developer_id, developer_object['phone_number'],
                              developer_object['name'], team_id)
        data_manager.add_developer(developer_id, developer)
        developer_constant += 1
    return team_id


def create_notification(team_id):
    headers = {
        "Content-Type": "application/json"
    }
    developer_id = data_manager.team_developer[team_id][0]
    developer = data_manager.developer[developer_id]
    body = {"phone_number": developer.phone_number, "message": "Too many 5xx!"}
    request_url = "https://run.mocky.io/v3/fd99c100-f88a-4d70-aaf7-393dbbd5d99f"
    response = requests.post(request_url, headers=headers, data=body)
    if response.status_code == 200:
        return developer
    return None
