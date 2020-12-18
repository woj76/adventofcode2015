def dijkstra(g, source, dest = None):
	q = []
	dist = {}
	prev = {}

	for v1,v2 in g.keys():
		dist[v1] = dist[v2] = float('inf')
		for v in [x for x in [v1, v2] if x not in q]:
			q.append(v)
	dist[source] = 0

	while q != []:
		u = sorted([(dist[v],v) for v in q])[0][1]
		q.remove(u)
		if u == dest:
			break
		for v in [y for x,y in g.keys() if x == u and y in q]:
			alt = dist[u] + g[(u,v)]
			if alt < dist[v]:
				dist[v] = alt
				prev[v] = u
	return dist, prev
