import pandas as pd
import filter as f

def find_best_route(start_date_time, end_date_time, start_lat, start_lon):
    # Get possible routes
    # No need to sort routes becuase we try all of them anyway # Sort possible routes by closest ones that have 
    # Compute a new start time after a load
    # Try 1 (recursively)

    best_route = [0, []]

    possible_routes: pd.DataFrame = f.filter_routes(start_date_time, end_date_time)

    if possible_route

    for route in possible_routes:

        time_to_origin = start_date_time + f.to_t_delt(f.find_dist(start_lon, start_lat, route["origin_long"], route["origin_lat"]) // 55) # Find time at which we can reach origin of load

        if time_to_origin > route["pickup_date_time"]: # If we arrive later than pickup time, skip this road
            continue

        find_best_route(route["arrival_time"], end_date_time, route["origin_latitude"], route["origin_longitude"], cumul_cost)



    return best_route

