class Team:
    def __init__(self, team_id, team_name):
        self.team_id = team_id
        self.team_name = team_name


class Developer:
    def __init__(self, developer_id, phone_number, developer_name, team_id):
        self.developer_id = developer_id
        self.phone_number = phone_number
        self.developer_name = developer_name
        self.team_id = team_id
