import os
import csv

#Open the file, `cereal.csv` and start by skipping the header row

cereal_csv = os.path.join("..", "Solved", "cereal.csv")
#print(cereal_csv)
with open(cereal_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # the below statement will skip the first row
    next(csvreader)
    print("------------------------") 
    print("Cereal Cleaner")
    print("------------------------")  
    # Set the variable to chaeck if we found the cereal
    found = False
    for cereal in csvreader:
        cereal_name=cereal[0]
        fiber=cereal[7]
        float_fiber=float(fiber)
        if float_fiber>=5:
            print(f"{cereal_name} has {fiber} grams of fiber")
            found=True
