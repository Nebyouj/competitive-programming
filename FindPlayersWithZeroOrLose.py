class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost_count = defaultdict(int)
        players = set()

        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            lost_count[loser] += 1

        zeroloss = sorted(player for player in players if lost_count[player] == 0)
        oneloss = sorted(player for player in players if lost_count[player] == 1)

        return [zeroloss, oneloss]
        
