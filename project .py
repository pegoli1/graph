graph = {}
graph["start"] = {}
graph["start"]["b"]=0.2;
graph["start"]["c"]=0.2;
graph["start"]["d"]=0.6;

graph["b"]= {}
graph["b"]["d"]=3.9
graph["b"]["c"]=2.8

graph["c"] = {}
graph["c"]["d"]=0.4
graph["c"]["e"]=4.8

graph["d"] = {}
graph["d"]["f"]=3.8
graph["d"]["g"]=6.3

graph["e"] = {}
graph["e"]["g"]=3.8
graph["e"]["h"]=9

graph["f"] = {}
graph["f"]["g"]=2

graph["g"] = {}
graph["g"]["i"]=0.3

graph["h"] = {}
graph["h"]["i"]=0.1
graph["h"]["l"]=8.2

graph["i"] = {}
graph["i"]["m"]=3.5
graph["i"]["j"]=0.2

graph["j"] = {}
graph["j"]["n"]=2
graph["j"]["k"]=1.1

graph["k"] = {}
graph["k"]["o"]=3.6

graph["o"] = {}
graph["o"]["n"]=1.8

graph["n"] = {}
graph["n"]["fin"]=0.2

graph["m"] = {}
graph["m"]["n"]=0.8

graph["l"] = {}
graph["l"]["m"]=3.6

graph["fin"] = {}

costs={}
infinit = float("inf")
costs["b"]=0.2;
costs["c"] =0.2
costs["d"]=0.6;
costs["e"]=infinit
costs["f"]=infinit
costs["g"]=infinit
costs["h"]=infinit
costs["i"]=infinit
costs["j"]=infinit
costs["k"]=infinit
costs["o"]=infinit
costs["n"]=infinit
costs["m"]=infinit
costs["l"]=infinit
costs["fin"]=infinit

parents={}
parents["b"]="start"
parents["c"]="start"
parents["d"]="start"
parents["f"]=None
parents["g"]=None
parents["h"]=None
parents["i"]=None
parents["j"]=None
parents["k"]=None
parents["o"]=None
parents["n"]=None
parents["m"]=None
parents["l"]=None
parents["fin"]=None

processed = []

def find_lowst_cost_node(costs):
    nodes =costs.keys()
    lowest = float("inf")
    key = None;
    for n in nodes:
        if lowest > costs[n] and n not in processed:
            lowest = costs[n]
            key = n;
    return key
   
   

def find_best_path(graph,costs,parents):
    node = find_lowst_cost_node(costs)     
    while node is not None:
        cost = costs[node]
        neighbors=graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node;
        processed.append(node)
        node = find_lowst_cost_node(costs)
    return parents;

# print (find_best_path(graph,costs,parents))  # u can uncoment this line and get the returning value of the find_best_path function 
def show_best_path_and_cost(graph,costs,parents):
    parents=find_best_path(graph,costs,parents)
    node = "fin"
    path = []
    for i in range(len(parents)):
        if node == "fin":
            path.append("fin")
        route=parents[node]
        path.append(route)    
        if route == "start":
            break
        node = route
    path.reverse()
    print("This is the best path: "+'->'.join(path))
    print("This is the costs: "+str(round(costs['fin'],1)))
show_best_path_and_cost(graph,costs,parents)

