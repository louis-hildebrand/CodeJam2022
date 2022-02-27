from datetime import datetime
import pandas as pd

from data.filter import filter
from data.utils import cost, sort_loads_by_dist

MAX_INDEX = 3

def calculate_route(start_lat: float, start_long: float, start_time: datetime, max_dest_time: datetime) -> list[int]:
    _, route = calculate_route_and_profit(start_lat, start_long, start_time, max_dest_time)
    return reversed(route)

def calculate_route_and_profit(start_lat: float, start_long: float, start_time: datetime, max_dest_time: datetime) -> tuple[float, list[int]]:
    loads = filter(start_time, max_dest_time)
    if len(loads.index) == 0:
        return (0, [])
    # Sort loads in ascending order of distance
    sorted_loads = sort_loads_by_dist(loads, start_long, start_lat)
    max_profit = 0
    max_profit_route = []
    i = 0
    for _, load in sorted_loads.iterrows():
        if i >= MAX_INDEX:
            break
        # Find route starting with this load
        new_start_lat = load['destination_latitude']
        new_start_long = load['destination_longitude']
        new_start_time = datetime.fromisoformat(load['arrival_time'])
        profit, route = calculate_route_and_profit(new_start_lat, new_start_long, new_start_time, max_dest_time)
        # Calculate profit (including initial deadhead)
        profit += pd.to_numeric(load['net_pay']) - cost(start_long, start_lat, new_start_long, new_start_lat)
        # Update route
        load_id = pd.to_numeric(load['load_id'])
        route.append(load_id)
        # Choose route with highest profit
        if profit > max_profit:
            max_profit = profit
            max_profit_route = route
        i += 1
    return (max_profit, max_profit_route)
