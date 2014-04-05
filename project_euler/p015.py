"""Lattice paths

Starting in the top left corner of a 2*2 grid,
there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 20*20 grid?

Answer: 137846528820
"""


def solve():
    GRID_SIZE = 20

    def getNextNodes(x, y):
        nodes = []

        if x < GRID_SIZE:
            nodes.append((x + 1, y))

        if y < GRID_SIZE:
            nodes.append((x, y + 1))

        return nodes

    def getPrevNodes(x, y):
        nodes = []

        if x > 0:
            nodes.append((x - 1, y))

        if y > 0:
            nodes.append((x, y - 1))

        return nodes

    mapVal = [[0] * (GRID_SIZE + 1) for _ in range(GRID_SIZE + 1)]
    mapVal[0][0] = 1

    nodeQueue = [(0, 0)]
    while len(nodeQueue) != 0:
        top = nodeQueue[0]
        nodeQueue = nodeQueue[1:]
        nextNodes = getNextNodes(*top)
        for node in nextNodes:
            (x, y) = node
            if mapVal[x][y] == 0:
                prevNodes = getPrevNodes(*node)
                for prevNode in prevNodes:
                    (a, b) = prevNode
                    mapVal[x][y] += mapVal[a][b]
                nodeQueue.append(node)

    return mapVal[GRID_SIZE][GRID_SIZE]


if __name__ == '__main__':
    print(solve())
