import math
import pandas as pd

def find_dist(long1, lat1, long2, lat2):
    """
    const R = 6371000; // metres
    const φ1 = lat1 * Math.PI/180; // φ, λ in radians
    const φ2 = lat2 * Math.PI/180;
    const Δφ = (lat2-lat1) * Math.PI/180;
    const Δλ = (lon2-lon1) * Math.PI/180;

    const a = Math.sin(Δφ/2) * Math.sin(Δφ/2) +
            Math.cos(φ1) * Math.cos(φ2) *
            Math.sin(Δλ/2) * Math.sin(Δλ/2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));

    const d = R * c; // in metres
    """
    R = 6371000
    phi1 = lat1 * math.pi/180
    phi2 = lat2 * math.pi/180
    delta_phi = (lat2 - lat1) * math.pi/180
    delta_lambda = (long2 - long1) * math.pi/180
    a = math.sin(delta_phi/2) * math.sin(delta_phi/2) + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2) * math.sin(delta_lambda/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c * 0.000621371
    return d

def to_t_delt(number):
    return pd.to_timedelta(f'{math.floor(number)}hours {(number - math.floor(number)) * 100}min')

def cost(start_lon, start_lat, end_lon, end_lat):
    """
    Cost of driving somewhere.
    """
    distance = find_dist(start_lon, start_lat, end_lon, end_lat)
    return distance * 0.4

def sort_loads_by_dist(loads: pd.DataFrame, start_long: float, start_lat: float) -> pd.DataFrame:
    distances = []
    for row in loads.itertuples():
        lat = getattr(row, 'origin_latitude')
        long = getattr(row, 'origin_latitude')
        d = find_dist(start_long, start_lat, lat, long)
        distances.append(d)
    loads.insert(0, 'd', distances)
    loads_with_dist = loads.sort_values('d', axis=0, ascending=True, inplace=False)
    return loads_with_dist
