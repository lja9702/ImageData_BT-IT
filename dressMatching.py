import csv
import pandas as pd

color_matching = {'red' : ['red', 'orange', 'gray', 'black', 'white'],
                  'orange' : ['red', 'orange', 'gray', 'blue', 'black', 'white', 'brown'],
                  'yellow' : ['blue', 'black', 'gray', 'white', 'orange', 'green', 'brown'],
                  'green' : ['orange', 'yellow', 'skyblue', 'black', 'white', 'brown'],
                  'blue' : ['blue', 'yellow', 'purple', 'skyblue', 'pink', 'gray', 'black', 'white'],
                  'purple' : ['blue', 'skyblue', 'gray', 'pink', 'black', 'white'],
                  'skyblue' : ['skyblue', 'gray', 'black', 'pink', 'purple', 'white', 'blue'],
                  'pink' : ['orange', 'white', 'blue', 'black', 'gray', 'skyblue'],
                  'gray' : ['red', 'orange', 'yellow', 'blue', 'purple', 'skyblue', 'pink', 'gray', 'black', 'white', 'brown'],
                  'black' : ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'skyblue', 'pink', 'gray', 'black', 'white', 'brown'],
                  'white' : ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'skyblue', 'pink', 'gray', 'black', 'white', 'brown'],
                  'brown' : ['orange', 'yellow', 'blue', 'gray', 'black', 'white', 'green']
                  }

type_matching = {'jacket' : ['dress', 'pants long ', 't shirt long ', 'skirt', 'headwear', 't shirt short ', 'shirt'],
                 'dress' : ['jacket', 'coat', 'padded'],
                 'pants long ' : ['jacket', 't shirt long ', 'headwear', 'coat', 't shirt short ', 'shirt', 'padded'],
                 't shirt long ' : ['jacket', 'pants long ', 'skirt', 'headwear', 'coat', 'pants shorts ', 'padded'],
                 'skirt' : ['jacket', 't shirt long ', 'coat', 't shirt short ', 'shirt', 'padded'],
                 'headwear' : ['jacket', 'pants long ', 't shirt long ', 'pants shorts ', 't shirt short ', 'padded'],
                 'coat' : ['dress', 'pants long ', 'skirt', 't shirt long ', 'shirt'],
                 'pants shorts ' : ['jacket', 't shirt long ', 'headwear', 't shirt short '],
                 't shirt short ' : ['jacket', 'pants long ', 'skirt', 'headwear', 'pants shorts '],
                 'shirt' : ['jacket', 'pants long ', 'skirt', 'coat', 'padded'],
                 'padded' : ['dress', 'pants long ', 't shirt long ', 'skirt', 'headwear', 'shirt']
                 }

class matching_area2:
    #dress_path: 불러온 옷의 경로, closet_path: 옷장의 경로
    def __init__(self, dress_path, closet_path, type, simplecolor):
        self.dress_path = dress_path
        self.closet_path = closet_path
        self.type = type
        self.simplecolor = simplecolor

    def matching_cloth(self, rowtype, rowcolor):
        colorList = color_matching[self.simplecolor]
        typeList = type_matching[self.type]
        if (rowcolor in colorList) and (rowtype in typeList):
            return True
        else:
            return False

