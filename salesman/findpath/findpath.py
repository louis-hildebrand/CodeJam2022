from datetime import datetime

from data.filter import filter
from data.utils import cost, sort_loads_by_dist

MAX_INDEX = 500

def calculate_route(start_lat: float, start_long: float, start_time: datetime, max_dest_time: datetime) -> list[int]:
    _, route = calculate_route_and_profit(start_lat, start_long, start_time, max_dest_time)
    return route

def calculate_route_and_profit(start_lat: float, start_long: float, start_time: datetime, max_dest_time: datetime) -> tuple[float, list[int]]:
    loads = filter(start_time, max_dest_time)
    if len(loads.index) == 0:
        return (0, [])
    # Sort loads in ascending order of distance
    sorted_loads = sort_loads_by_dist(loads, start_long, start_lat)
    max_profit = 0
    max_profit_route = []
    for index, load in sorted_loads.iterrows():
        if index >= MAX_INDEX:
            break
        # Find route starting with this load
        new_start_lat = load['destination_latitude']
        new_start_long = load['destination_longitude']
        new_start_time = datetime.fromisoformat(load['arrival_time'])
        profit, route = calculate_route_and_profit(new_start_lat, new_start_long, new_start_time, max_dest_time)
        # Calculate initial deadhead
        profit -= cost(start_long, start_lat, new_start_long, new_start_lat)
        # Choose route with highest profit
        if profit > max_profit:
            max_profit = profit
            max_profit_route = route
    return (max_profit, max_profit_route)
