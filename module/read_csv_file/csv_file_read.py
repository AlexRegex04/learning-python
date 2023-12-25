import pandas as pd
import csv
x = csv.reader(
    './annual-enterprise-survey-2021-financial-year-provisional-csv.csv')

# * Reading CSV files
# Using csv.reader() function
# with open('./annual-enterprise-survey-2021-financial-year-provisional-csv.csv') as csv_file:
#     csv_reader = csv.reader(csv_file,delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1

# *Read a CSV into a Dictionar

# *Write a CSV into a Dictionary

# Writing CSV Files
data = [{'Rank': 'B', 'first_name': 'Parker', 'last_name': 'Brian'},
        {'Rank': 'A', 'first_name': 'Smith', 'last_name': 'Rodriguez'},
        {'Rank': 'C', 'first_name': 'Tom', 'last_name': 'smith'},
        {'Rank': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'},
        {'Rank': 'A', 'first_name': 'Alex', 'last_name': 'Tim'}]

"""Dialect.delimiter: This attribute is used as the separating character between the fields. The default value is a comma (,).
Dialect.quotechar: This attribute is used to quote fields that contain special characters.
Dialect.lineterminator: It is used to create new lines, and the default value is '\r\n'."""
with open('Python.csv', 'w') as csvfile:
    fieldnames = list(data[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                            delimiter='.', quotechar='F', lineterminator='\n')
    writer.writeheader()
    for x in data:
        writer.writerow(x)
        print("Writing complete")


