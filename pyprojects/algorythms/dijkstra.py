graph = {}

graph["start"] = {}
graph["a"] = {}
graph["c"] = {}
graph["d"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2
graph["c"]["d"] = 6
graph["c"]["fin"] = 3
graph["d"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["d"] = 7
graph["fin"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 5
costs["b"] = 2
costs["d"] = infinity
costs["c"] = infinity
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

def find_lowest_cost_node(costs):
    lower_cost = float("inf")
    lower_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lower_cost and node not in processed:
            lower_cost = cost
            lower_cost_node = node
    return lower_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
    

find_lowest_cost_node(costs)
print(costs)
#print (graph["start"].keys())
#print (graph["start"]["a"])