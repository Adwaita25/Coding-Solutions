class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        is_undefeated = [True] * n

        for winner, loser in edges:
            is_undefeated[loser] = False
        
        champ = -1
        champ_count = 0

        for team in range(n):
            if is_undefeated[team]:
                champ = team
                champ_count += 1
        
        if champ_count == 1:
            return champ
        return -1
