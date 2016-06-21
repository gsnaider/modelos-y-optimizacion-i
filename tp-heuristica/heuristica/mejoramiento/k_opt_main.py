'''
Created on Jun 21, 2016

@author: gaston
'''
from heuristica.construccion.nearest_neighbor import nearest_neighbor, \
    print_route
from heuristica.mejoramiento.k_opt import k_opt


route = nearest_neighbor()
print ""
print "Ruta inicial"
print ""
print_route(route)
print ""

enhanced_route = k_opt(route)
print ""
print "Ruta mejorada"
print ""
print_route(enhanced_route)