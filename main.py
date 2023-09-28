from collections import Counter
from collections import OrderedDict

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score
     
    def player_rank(self, rank):
        players = list(self.standings.keys())

        for i in range(len(players)):
            currentPlayer = players[i]

            for j in range(i+1, len(players)):
                nextPlayer = players[j]

                nextPlayerScoreIsHigher = self.standings[nextPlayer]["score"] > self.standings[currentPlayer]["score"]
                scoresAreEqual = self.standings[nextPlayer]["score"] == self.standings[currentPlayer]["score"]
                nextPlayerGamesAreFewer = self.standings[nextPlayer]["games_played"] < self.standings[currentPlayer]["games_played"]
                gamesPlayedAreEqual = self.standings[nextPlayer]["games_played"] == self.standings[currentPlayer]["games_played"]
                nextPlayerIsNearerInListOrder = players.index(nextPlayer) < players.index(currentPlayer) 

                if(nextPlayerScoreIsHigher or (scoresAreEqual and (nextPlayerGamesAreFewer or gamesPlayedAreEqual and nextPlayerIsNearerInListOrder))):
                    temp = players[i];
                    players[i] = players[j]
                    players[j] = temp;
        
                    currentPlayer = players[i]
                    continue
                
                        
        return players[rank-1]

if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 2)
    table.record_result('Arnold', 3)
    table.record_result('Chris', 4)
    table.record_result('Chris', 1)
    print(table.player_rank(1))