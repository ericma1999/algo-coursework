from .Euclidean import euclidean_distance

class BruteForce2:

    def __init__(self, G):
        self.bestScore = -1
        self.bestPath = []
        self.G = G
        self.x = []
        self.y = []

        vertices = [x for x in range(G.V)]

        self.__permutations(len(vertices), vertices)

    def __tryPathAndScore(self, pathRoute):
        path = []
        x = []
        y = []
        score = 0

        previous_position = None
        for index, vertex in enumerate(pathRoute):
            currentStation = self.G.getStation(vertex)
            path.append(currentStation.getName())
            x.append(currentStation.lat)
            y.append(currentStation.lng)
            if (index == 0):
                previous_position = (currentStation.lat, currentStation.lng)
                continue
            
            score += euclidean_distance(previous_position[0], previous_position[1], currentStation.lat, currentStation.lng)

            previous_position = (currentStation.lat, currentStation.lng)
        
        if score < self.bestScore or self.bestScore == -1:
            self.bestPath = path
            self.bestScore = score
            self.x = x
            self.y = y


    def __permutations(self, size, values):
        if size == 1:
            self.__tryPathAndScore(values)
        else:

            self.__permutations(size - 1, values)

            for i in range(size - 1):
                if size % 2 == 0:
                    values[i], values[size - 1] = values[size - 1], values[i]
                else:
                    values[0], values[size - 1] = values[size - 1], values[0]
                
                self.__permutations(size - 1, values)