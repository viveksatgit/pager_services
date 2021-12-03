from flask import Flask
from flask import request
import team_service
from manage import DataManager

data_manager = DataManager()
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/team", methods=['POST'])
def create_request():
    team = request.json
    team_id = team_service.create_team(team)
    return {'error': False, 'team_id': team_id}


@app.route("/alert/<team_id>", methods=['POST'])
def create_alert(team_id):
    developer = team_service.create_notification(team_id)
    if not developer:
        return {'error': True, 'message': 'failure in sending the notification'}
    return {'error': False, 'message': 'notification has been sent to{}'.format(developer.phone_number)}


if __name__ == '__main__':
    app.run()

    '''interview@barraiser.com'''
