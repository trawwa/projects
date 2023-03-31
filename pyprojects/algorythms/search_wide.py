from collections import deque

graph = {}
graph["you"] = ["alice", "coc", "claire"]
graph["coc"] = ["anju", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anju"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    saearch_queue = deque()
    saearch_queue += graph[name]
    searched = []
    while saearch_queue:
        person = saearch_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")  
            else:
                saearch_queue += graph[person]
                searched.append(person)

search("you")


