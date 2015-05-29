class Marcador:
    teamios = ["", 0]
    teamandroid = ["", 0]
    actualizado = False

    def __init__(self, team1, team2):
        self.teamios[0] = team1
        self.teamandroid[0] = team2

    def addGoal(self, team):
        winner = ""
        if team == "teamios":
            self.teamios[1] += 1
        elif team == "teamandroid":
            self.teamandroid[1] += 1

        if self.teamios[1] == 7:
            winner = "teamios"
        elif self.teamandroid[1] == 7:
            winner = "teamandroid"

        self.actualizado = team

        return winner

    def estaActualizado(self):
        if self.actualizado:
            sal = self.actualizado
            self.actualizado = False
            return sal
        else:
            return False

