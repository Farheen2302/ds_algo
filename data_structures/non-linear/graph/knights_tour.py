from pythonds.graphs import Graph


def getNodeId(row, col, bdsize):
    return (row * bdsize) + col


def islegal(x, bdsize):
    return (x >= 0 and x < bdsize)


def getLegalMoves(row, col, bdsize):
    legalMoves = []
    possiblities = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                    (2, 1), (2, -1), (-2, 1), (-2, -1)]
    for i in possiblities:
        x = row + i[0]
        y = col + i[1]
        if islegal(x,bdsize) and islegal(y, bdsize):
        	legalMoves.append((x,y))
    return legalMoves


def buildGraph(bdsize):
    ktGraph = Graph()
    for row in range(bdsize):
        for col in range(bdsize):
            nodeId = getNodeId(row, col, bdsize)
            legalMoves = getLegalMoves(row, col, bdsize)
            for options in legalMoves:
            	nid = getNodeId(options[0], options[1], bdsize)
            	ktGraph.addEdge(nodeId, nid)
    return ktGraph

buildGraph(8)