from collections import defaultdict


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loseCounts = defaultdict(int)
        for match in matches:
            winner = match[0]
            loser = match[1]
            loseCounts[winner] += 0
            loseCounts[loser] += 1
        winners = []
        losers = []
        for player in loseCounts:
            if loseCounts[player] == 0:
                winners.append(player)
            elif loseCounts[player] == 1:
                losers.append(player)
        ans = [sorted(winners), sorted(losers)]
        return ans
