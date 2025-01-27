 

#Task 2
class Tournament:
    def __init__(self,name='Default'):
        self.__name = name

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

class Cricket_Tournament(Tournament):
  def __init__(self, name="Default", team=0, types="No type"):
    super().__init__(name)
    self.team=team
    self.types = types

  def detail(self):
    return (f"Cricket Tournament Name: {self.get_name()} \nNumber of Teams: {self.team} \nType: {self.types}")

class Tennis_Tournament(Tournament):
  def __init__(self, name, players):
    super().__init__(name)
    self.players=players

  def detail(self):
    return (f"Tennis Tournament Name: {self.get_name()} \nNumber of players: {self.players} ")

ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL",10,"t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros",128)
print(tt.detail())