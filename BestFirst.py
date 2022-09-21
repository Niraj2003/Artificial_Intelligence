from queue import PriorityQueue
v = 6
graph = [[] for i in range(v)]

def bestFirst(sr, t, n):
	vis = [False] * n
	pq = PriorityQueue()
	pq.put((0, sr))
	vis[sr] = True
	
	while pq.empty() != True:
		u = pq.get()[1]
		print(u, end=" ")
		if u == t:
			break

		for v, c in graph[u]:
			if vis[v] == False:
				vis[v] = True
				pq.put((c, v))
	print()


def addedge(x, y, cost):
	graph[x].append((y, cost))
	graph[y].append((x, cost))


addedge(0, 1, 10)
addedge(0, 2, 7)
addedge(0, 3, 3)
addedge(1, 2, 17)
addedge(3, 5, 26)
addedge(2, 4, 5)


source = 0
t = 9
print("Best First of Tree : ")
bestFirst(source, t, v)


# Niraj Amrutkar