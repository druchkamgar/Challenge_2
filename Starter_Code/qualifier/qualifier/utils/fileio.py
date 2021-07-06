# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

#User story: as a user, I need the ability to save the qualifying loans to a CSV file so that I can share the results as a spreadsheet.
# We want to build a function that saves qualifying loans, dubbed save_qualifiy_laons
# We then want to build a function that exports the output of function save_qualifying_loans() to a .csv. We will call this function save_csv()

def save_csv(output_path):
    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        header = []
        csvwriter.writerow(header)
        for row in csvwriter:
            csvwriter.writerow(row)

