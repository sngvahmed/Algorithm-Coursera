#Uses python3
import sys
import math
import queue

join = []
vis = {}
cluster_count = 0

def joinThem(n1, n2):
	idxN1 = -1
	idxN2 = -2
	v = 0
	
	for arr in join:
		
		try: arr.index(n1); idxN1 = v;
		except ValueError: pass
			
		try: arr.index(n2); idxN2 = v
		except ValueError: pass
	
		v = v + 1
	vis[n1] = True
	vis[n2] = True
	if idxN1 == idxN2:
		return False
	
	if idxN1 == -1 and idxN2 == -2:
		join.append([n1, n2])
		return True
	
	if idxN1 == -1:
		join[idxN2].append(n1)
		return True
	
	if idxN2 == -2:
		join[idxN1].append(n2)
		return True
	
	for node in join[idxN1]:
		join[idxN2].append(node)
		
	join.pop(idxN1)
		
	return True


def calcDist(n1, n2):
	return math.sqrt( ((n1[0] - n2[0])**2) + ((n1[1] - n2[1])**2) )


def getOptimalWeight(x, y):
	mn = sys.maxsize
	
	for v in join:
		for vv in v:
			for q in join:
				if v == q:
					continue
				for qq in q:
					mn = min(mn, calcDist(vv,qq))	
	
	for i in range(len(x)):
		if ((x[i],y[i]) in vis) == False:
			for nd in join:
				for s in nd:
					mn = min(mn, calcDist([x[i],y[i]],s))	
	if mn == sys.maxsize: return -1.0
	return mn

def clustering(x, y, k):

	heap = queue.PriorityQueue()	
	cluster_count = len(x)
	
	for v in range(0, x.__len__() - 1):
		for q in range(v + 1, x.__len__()):
			node1 = (x[v],y[v]);
			node2 = (x[q],y[q]);
			heap.put([calcDist(node1, node2), node1, node2]);
	
	res = -1.;
	
	while not heap.empty():
		n = heap.get()
		if (k == cluster_count):
			res = getOptimalWeight(x, y)
		
		if (joinThem(n[1], n[2])):
			cluster_count = cluster_count - 1;
		
	return res


if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n = data[0]
	data = data[1:]
	x = data[0:2 * n:2]
	y = data[1:2 * n:2]
	data = data[2 * n:]
	k = data[0]
	print("{0:.9f}".format(clustering(x, y, k)))
