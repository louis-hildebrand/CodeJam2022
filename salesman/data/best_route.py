import pandas as pd
import filter as f

def find_best_route(start_date_time, end_date_time, start_lat, start_lon, profit):
    # Get possible routes
    # No need to sort routes becuase we try all of them anyway # Sort possible routes by closest ones that have 
    # Compute a new start time after a load
    # Try 1 (recursively)


    # pseudocode:
    # if you have 0 posibilities, return the profit
    # if you have 2 possibilities, then find the max of the two recursive call 
    # but first (compute the cost with helper method and substract it from the profit and that result will be the profit in the recusive call and the time it takes to get there which will be the start time in the recursive call)
    # otherwise if you have more than 2 possibilities, then for loop through all the possibilities and recursive call with the last step
    # the return is the profit, so you need to compute it before recursing every time
    
    best_route = [0, []]

    possible_routes = f.filter_routes(start_date_time, end_date_time)

    if len(possible_route.iterrows()) == 0:
        return profit
    elif len(possible_routes.iterrows()) == 2: 
        cost = cost(start_lon, start_lat, possible_routes['origin_longitude'].iloc[0], possible_routes['origin_latitude'].iloc[0])
        print(start_lon, start_lat, possible_routes['origin_longitude'].iloc[0], possible_routes['origin_latitude'].iloc[0])
        
        return max(find_best_route(possible_routes['origin_latitude'].iloc[0], possible_routes['origin_longitude'].iloc[0]))

    for route in possible_routes:

        time_to_origin = start_date_time + f.to_t_delt(f.find_dist(start_lon, start_lat, route["origin_long"], route["origin_lat"]) // 55) # Find time at which we can reach origin of load

        if time_to_origin > route["pickup_date_time"]: # If we arrive later than pickup time, skip this road
            continue

        find_best_route(route["arrival_time"], end_date_time, route["origin_latitude"], route["origin_longitude"], cumul_cost)



    return best_route

def cost(start_lon, start_lat, end_lon, end_lat):
    distance = f.find_dist(start_lon, start_lat, end_lon, end_lat)
    return distance * 0.4       #cost of driving somewhere

