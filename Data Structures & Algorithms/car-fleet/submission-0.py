class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0
        elif len(position) == 1:
            return 1
        pos = sorted(position)
        cars, fleets = 1, 1
        time = (target - pos[-1])/speed[position.index(pos[-1])]
        i = 0
        for i in range(len(pos) - 2, -1, -1):
            t = (target - pos[i])/speed[position.index(pos[i])]
            if t <= time:
                cars+=1
            else:
                fleets+=1
                time = t
                cars = 1
        
        return fleets

        