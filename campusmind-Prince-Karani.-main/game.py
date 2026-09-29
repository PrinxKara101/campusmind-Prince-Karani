CAMPUS_GRAPH = {
    'MainGate': ['Admin', 'Cafeteria'],
    'Admin': ['MainGate', 'Library', 'StudentCentre'],
    'Library': ['Admin'],
    'StudentCentre': ['Admin', 'Cafeteria', 'SportsComplex'],
    'Cafeteria': ['MainGate', 'StudentCentre', 'SportsComplex'],
    'SportsComplex': ['StudentCentre', 'Cafeteria']
}

UTILITIES = {
    'MainGate': 2 - 1,        # 1
    'Admin': 1 - 2,           # -1
    'Library': 0 - 3,         # -3
    'StudentCentre': 2 - 1,   # 1
    'Cafeteria': 3 - 0,       # 3
    'SportsComplex': 3 - 1    # 2
}

class CampusMindGame:
    def __init__(self, start_node='MainGate', max_depth=3):
        self.start_node = start_node
        self.max_depth = max_depth

    def get_neighbors(self, node):
        return CAMPUS_GRAPH.get(node, [])

    def utility(self, node):
        return UTILITIES[node]
