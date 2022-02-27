import os
import pandas as pd

from data.utils import find_dist, to_t_delt

ORIGINAL_MARKETPLACE = r'data\123Loadboard_CodeJam_2022_dataset.csv'
TMP_MARKETPLACE = r'data\marketplace.tmp'
FILLED_MARKETPLACE = r'data\marketplace.csv'

def fill_data(file_in: str, file_out: str):
    csvfile = pd.read_csv(file_in)
    #compute linear distance for all the shipments
    distance_value = []
    arrival_time = []
    pay = []
    for _, entry in csvfile.iterrows(): 
        distance = find_dist(entry.origin_longitude, entry.origin_latitude, entry.destination_longitude, entry.destination_latitude)
        arrival_time.append(str(pd.to_datetime(entry.pickup_date_time) + to_t_delt(distance / 55)))
        distance_value.append(distance)
        pay.append(entry.amount - (distance *  0.4))
    csvfile.insert(10, "geo_dist", distance_value)
    csvfile.insert(12, "arrival_time", arrival_time)
    csvfile.insert(10, "net_pay", pay)
    
    csvfile.to_csv(file_out, index = False, line_terminator="\n")
    return csvfile

def sort_csv(file_in: str, file_out: str, categories: list = ["pickup_date_time"], ascending: bool = True):
    sorted = open(file_out, "w+")
    csvData = pd.read_csv(file_in)
    csvData.sort_values(categories, axis=0, ascending=[ascending], inplace=True)
    csvData.to_csv(sorted, index=False, line_terminator='\n')
    sorted.close()
    return

def main():
    fill_data(ORIGINAL_MARKETPLACE, TMP_MARKETPLACE)
    sort_csv(TMP_MARKETPLACE, FILLED_MARKETPLACE)
    os.remove(TMP_MARKETPLACE)

if __name__ == "__main__":
    main()
