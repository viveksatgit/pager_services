class DataManager:
    def __init__(self):
        self.team = {}
        self.developer = {}
        self.team_developer = {}

    def add_team(self, team_id, team):
        self.team[team_id] = team

    def add_developer(self, developer_id, developer):
        self.developer[developer_id] = developer
        if developer.team_id not in self.team_developer:
            self.team_developer[developer.team_id] = [developer.developer_id]
        else:
            self.team_developer[developer.team_id].append(developer.developer_id)
