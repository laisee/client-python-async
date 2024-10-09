import csv

def lookup_conversion_number_by_id(csv_file_path, id):
    with open(csv_file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        # Iterate over the rows in the CSV file
        for row in csv_reader:
            # Match on the first column
            if row[0] == id:
                # Return the last two columns from the matched row
                return 10**int(row[-2]), 10**int(row[-1])
    return 1,1  # Return default value of 1 if no match found
