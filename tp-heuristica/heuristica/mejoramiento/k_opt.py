'''
Created on Jun 21, 2016

@author: gaston
'''

from heuristica.construccion.nearest_neighbor import *



def calculate_distance(route):
    distance = 0
    idx = 1
    
    for bank in route[1:]:
        previous_bank = route[idx - 1]
        dist_from_previous_bank = DISTANCES[previous_bank][bank]
        distance += dist_from_previous_bank
        idx += 1
    
    return distance

def swap(route, i, j):
    
    if(i < j):
        min = i
        max = j
    else:
        min = j
        max = i        
    
    new_route = []
    new_route.extend(route[:min])
    new_route.extend(list(reversed(route[min:max+1])))
    new_route.extend(route[max+1:])
    return new_route

def is_route_possible(route):
    money = 0
    
    for bank in route:
        movement = MOVEMENTS[bank]
        money += movement
        if ((money < 0) or (money >= MAX_MONEY)):
            return False
        
    return True
        

def k_opt(route):

    done = False
    distance = calculate_distance(route)
        
    while not done:
        i = 1
        change = False
        while (i <= N - 1) and not change:
            j = i + 1
            while (j <= N) and not change:
                new_route = swap(route, i, j)
                new_distance = calculate_distance(new_route)
                if ((is_route_possible(new_route)) and (new_distance < distance)):
                    change = True
                    distance = new_distance
                    route = new_route
                    print "Intercambiando",BANKS[route[j]],"y",BANKS[route[i]]
                    print "Nueva distancia: ", new_distance
                    print ""
                j += 1
            i += 1
        
        if(i == N):
            print "No hay mas intercambios posibles."
            print ""
            done = True
            
    return route
