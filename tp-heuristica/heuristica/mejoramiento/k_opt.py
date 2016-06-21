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

def swap(lst, i, j):
    aux = lst[i]
    lst[i] = lst[j]
    lst[j] = aux

def is_route_possible(route):
    money = 0
    
    for bank in route:
        movement = MOVEMENTS[bank]
        money += movement
        if (money < 0):
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
                swap(route, i, j)
                new_distance = calculate_distance(route)
                if ((is_route_possible(route)) and (new_distance < distance)):
                    change = True
                    distance = new_distance
                    print "Intercambiando",i,"y",j
                    print ""
                else:
                    swap(route, i, j)
                j += 1
            i += 1
        
        if(i == N):
            print "No hay mas intercambios posibles."
            print ""
            done = True
            
    return route
