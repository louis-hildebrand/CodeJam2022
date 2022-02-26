import csv
from fileinput import close
import math
import pandas as pd

def filter_routes(start_time, end_time):
    fill_data()
    return filter_date(start_time, end_time)


def filter_date(start_time: str, end_time: str):
    csvfile = pd.read_csv(r'full_data.csv')

    mask = (csvfile['pickup_date_time'] >= start_time) & (csvfile['pickup_date_time'] < end_time) & (csvfile['arrival_time'] < end_time)
    output = csvfile.loc[mask]
    date_filtered = open('data_filtered.csv', 'w+')
    output.to_csv(date_filtered)
    date_filtered.close()
    return output

def fill_data():
    csvfile = pd.read_csv('123Loadboard_CodeJam_2022_dataset.csv')
    #compute linear distance for all the shipments
    distance_value = []
    arrival_time = []
    pay = []
    for _, entry in csvfile.iterrows(): 
        distance = find_dist(entry.origin_longitude, entry.origin_latitude, entry.destination_longitude, entry.destination_latitude)
        arrival_time.append(str(pd.to_datetime(entry.pickup_date_time) + to_t_delt(distance / 55)))
        distance_value.append(distance)
        pay.append(entry.amount - (distance *  0.4))
    csvfile.insert(10, "Linear distance", distance_value)
    csvfile.insert(12, "arrival_time", arrival_time)
    csvfile.insert(10, "net pay", pay)
    
    csvfile.to_csv('full_data.csv', index = False, line_terminator="\n")
    # print(csvfile)
    return csvfile

def to_t_delt(number):
    return pd.to_timedelta(f'{math.floor(number)}hours {(number - math.floor(number)) * 100}min')


""" const R = 6371000; // metres
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

    
def find_dist(long1, lat1, long2, lat2):
    R = 6371000
    phi1 = lat1 * math.pi/180
    phi2 = lat2 * math.pi/180
    delta_phi = (lat2 - lat1) * math.pi/180
    delta_lambda = (long2 - long1) * math.pi/180
    a = math.sin(delta_phi/2) * math.sin(delta_phi/2) + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2) * math.sin(delta_lambda/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c * 0.000621371
    return d

if __name__ == '__main__':
    print(filter_routes('2022-02-28  5:00:00','2022-02-28  5:01:00'))