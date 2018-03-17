#Uses python3
import sys
import math
import queue

join = []

def joinThem(n1, n2):
#	print("join", n1, n2)
	idxN1 = -1
	idxN2 = -2
	v = 0
	
	for arr in join:
		
		try: arr.index(n1); idxN1 = v;
		except ValueError: pass
			
		try: arr.index(n2); idxN2 = v
		except ValueError: pass
	
		v = v + 1
			
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


def clustering(x, y):
	heap = queue.PriorityQueue()	
	
	
	for v in range(0, x.__len__() - 1):
		for k in range(v + 1, x.__len__()):
			node1 = (x[v],y[v]);
			node2 = (x[k],y[k]);
			heap.put([calcDist(node1, node2), node1, node2]);
	
	
	result = 0.0;
	while not heap.empty():
		n = heap.get()
		
		
		if (joinThem(n[1], n[2])):
			result = result + n[0]
		
	return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(clustering(x, y)))
