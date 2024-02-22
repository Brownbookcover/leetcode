class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        trust_list = [0] * n
        no_trust_list = [0] * n

        for i in trust:
            trust_list[i[1]-1] += 1
            no_trust_list[i[0]-1] += 1
        
        for i in range(1, n+1):
            if trust_list[i-1] == n-1 and no_trust_list[i-1] == 0:
                return i
            
        return -1