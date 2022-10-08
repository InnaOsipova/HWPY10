#Морской бой


class SeaMap:

    history =()

    def shoot(self, row, col, result):
        self.row = row
        self.col = col
        self.result = result
        if result == 'sink':
            for i in range (self.row -1, self.row+2):
                for j in range (self.col -1, self.col+2):
                    if i == self.row and j == self.col: 
                        som_tuple = (self.row, self.col, self.result)
                        SeaMap.history +=(som_tuple, )
                    else:
                        som_tuple = (i, j, 'miss')
                        SeaMap.history +=(som_tuple, )
        else:                    
            som_tuple = (self.row, self.col, self.result)
            SeaMap.history +=(som_tuple, )
        return SeaMap.history
    
  
    def cell(self, row, col):
        self.row = row
        self.col = col
        for i in SeaMap.history:
            if i[0] == self.row and i[1] == self.col and i[2] == "hit":
                return 'x'
            if i[0] == self.row and i[1] == self.col and i[2] == "miss":
                 return '*'
            if i[0] == self.row and i[1] == self.col and i[2] == "sink":
                return 'x'
        return '.'

            
        


sm = SeaMap()
#(sm.sim(5,6))
sm.shoot(0, 0, 'sink')
sm.shoot(0, 9, 'sink')
sm.shoot(9, 0, 'sink')
sm.shoot(9, 9, 'sink')
# sm.shoot(5, 7, 'sink')
for i in range(10):
    for j in range (10):
        print(sm.cell(i,j), end = ' ')
    print()

