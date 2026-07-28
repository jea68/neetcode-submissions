class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        
        pos = [(position[i],speed[i]) for i in range(len(position))]
        pos = sorted(pos, key = lambda x :x[0])

        res = 0
        cur_max = -1
        print(pos)
        for i in range(len(position) - 1, -1, -1):
            time = (target - pos[i][0])  / pos[i][1]

            if time > cur_max:
                cur_max = time
                res +=1

        return res