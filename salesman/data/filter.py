import pandas as pd

from update_marketplace import FILLED_MARKETPLACE

def filter(start_time: str, end_time: str):
    csvfile = pd.read_csv(FILLED_MARKETPLACE)

    mask = (csvfile['pickup_date_time'] >= start_time) & (csvfile['pickup_date_time'] < end_time) & (csvfile['arrival_time'] < end_time)
    output = csvfile.loc[mask]
    # date_filtered = open('data_filtered.csv', 'w+')
    # output.to_csv(date_filtered)
    # date_filtered.close()
    return output

if __name__ == '__main__':
    filter('2022-02-28  5:00:00','2022-03-28  10:00:00')
