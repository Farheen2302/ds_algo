from pythonds import Graph
from pythonds import Queue


def buildGraph(wordFile):
	d = {}
	g = Graph()
	w = open(wordFile, 'r')
	for word in w:
		word = word[:-1]
		for i in range(len(word)):
			pattern = word[:i] +'_' + word[i+1:]
			if pattern in d:
				d[pattern].append(word)
			else:
				d[pattern] = [word]
	for pattern in d.keys():
		for word1 in d[pattern]:
			for word2 in d[pattern]:
				if word1 != word2:
					g.addEdge(word1, word2)
	return g


def bfs(g, start):
	queue = Queue()
	queue.enqueue(start)
	while(queue.size() > 0):
		current = queue.dequeue()
		for nbr in current.getConnections():
			if nbr.getColor() == 'white':
				nbr.setColor('grey')
				queue.enqueue(nbr)
		current.setColor('black')



g = buildGraph("D:\\GitHub\\ds_algo\\data_structures\\non-linear\\graph\\words.txt")
bfs(g, g.getVertex('sage'))