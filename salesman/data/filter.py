import pandas as pd

def filter_date(start_time: str, end_time: str):
    csvfile = pd.read_csv(r'123Loadboard_CodeJam_2022_dataset.csv')

    mask = (csvfile['pickup_date_time'] >= start_time) & (csvfile['pickup_date_time'] < end_time)
    output = csvfile.loc[mask]
    print(output)

filter_date('2022-02-28  5:00:00','2022-03-28  5:00:00')