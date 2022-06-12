import csv
from sort import MergeSort


csv_data = []
with open('real-estate.csv', 'r') as file:
            reader = csv.reader(file)
            csv_data.extend(list(reader))

sorted=MergeSort(csv_data)
print(sorted)

with open('write.csv', 'w') as file:
    writer_var = csv.writer(file)

    writer_var.writerow(sorted.data)
print(writer_var)