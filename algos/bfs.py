# Breadth-first search algorithm
# Implementation via dicts and deque

from collections import deque

def person_is_seller(name):
    return name[-1] == 'm'

def bfs(graph):
    search_queue = deque()
    search_queue += graph['you']
    checked = []
    while search_queue:
        person = search_queue.popleft()
        if not person in checked:
            if person_is_seller(person):
                print(f'{person} is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                checked.append(person)


graph = dict()

graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

bfs(graph)