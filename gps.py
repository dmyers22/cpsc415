#!/usr/bin/env python3

'''
CPSC 415 -- Homework #2 template
Daffney Myers, University of Mary Washington, fall 2021
'''

from atlas import Atlas
import numpy as np
import logging
import sys
import math


def find_best_path(atlas):
    '''Finds the best path from src to dest, based on costs from atlas.
    Returns a tuple of two elements. The first is a list of city numbers,
    starting with 0 and ending with atlas.num_cities-1, that gives the
    optimal path between those two cities. The second is the total cost
    of that path.'''

    # THIS IS WHERE YOUR AMAZING CODE GOES
    path = [0] # used to store the nodes visited
    cost = 0 # used to store total path cost
    current_city = 0 #used to remember where we are
    goal_city = atlas.get_num_cities() - 1 #wanted city
    poss_dist = 0 #used to test cheaper path
    poss_node = 0 #used to remember cheaper path outside of loop
    
    
    while current_city != goal_city:
        small_dist = math.inf #temp. make smallest infinity
        small_node = math.inf #temp. make smallest infinity
        
        #for loop check all distances between current_city to next node(i) (0 - numcities)
        for i in range(0, atlas.get_num_cities()):
            
            #makes sure no path = 0
            if i != current_city:
                poss_dist = atlas.get_road_dist(current_city, i)
                poss_node = i
            
            #keep shortest path as long as it is not infinite
            if poss_dist < small_dist and poss_dist != math.inf:
                small_dist = poss_dist
                small_node = poss_node
        
        if small_node == math.inf:
            print("Route not available")
            break
        
        elif small_node not in path:
            
            #go to new node (j) and add to path[]
            path.append(small_node)
            
            #add to total cost
            cost = cost + small_dist
            
            #change current node to (j)
            current_city = small_node
        
    return (path,cost)



if __name__ == '__main__':

    if len(sys.argv) not in [2,3]:
        print("Usage: gps.py numCities|atlasFile [debugLevel].")
        sys.exit(1)

    if len(sys.argv) > 2:
        if sys.argv[2] not in ['DEBUG','INFO','WARNING','ERROR']:
            print('Debug level must be one of: DEBUG, INFO, WARNING, ERROR.')
            sys.exit(2)
        logging.getLogger().setLevel(sys.argv[2])
    else:
        logging.getLogger().setLevel('INFO')

    try:
        num_cities = int(sys.argv[1])
        logging.info('Building random atlas with {} cities...'.format(
            num_cities))
        usa = Atlas(num_cities)
        logging.info('...built.')
    except:
        logging.info('Loading atlas from file {}...'.format(sys.argv[1]))
        usa = Atlas.from_filename(sys.argv[1])
        logging.info('...loaded.')

    path, cost = find_best_path(usa)
    print('Best path from {} to {} costs {}: {}.'.format(0,
        usa.get_num_cities()-1, cost, path))
    print('You expanded {} nodes: {}'.format(len(usa._nodes_expanded),
        usa._nodes_expanded))

