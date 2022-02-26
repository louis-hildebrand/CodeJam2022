import pandas
import timeit

def sort_csv(file_in: str, file_out: str, categories: list = ["pickup_date_time"], ascending: bool = True):
    sorted = open(file_out, "w")
    csvData = pandas.read_csv(file_in)
    csvData.sort_values(categories, axis=0, ascending=[ascending], inplace=True)
    csvData.to_csv(sorted, index=False, line_terminator='\n')
    # sorted.write(csv)

start = timeit.default_timer()
sort_csv("123Loadboard_CodeJam_2022_dataset.csv", "Sorted.csv", ["origin_city"])
print(timeit.default_timer() - start)