import csv

rowOfData: list = []
file_test: list = [
    r"C:\Users\LuiHo\Desktop\Python Projects\Useful-Python\Test Data\Combine CSV\MOCK_DATA(1).csv",
    r"C:\Users\LuiHo\Desktop\Python Projects\Useful-Python\Test Data\Combine CSV\MOCK_DATA.csv",
    r"C:\Users\LuiHo\Desktop\Python Projects\Useful-Python\Test Data\Combine CSV\MOCK_DATA(5).csv",
    r"C:\Users\LuiHo\Desktop\Python Projects\Useful-Python\Test Data\Combine CSV\MOCK_DATA(4).csv",
    r"C:\Users\LuiHo\Desktop\Python Projects\Useful-Python\Test Data\Combine CSV\MOCK_DATA(3).csv",
    r"C:\Users\LuiHo\Desktop\Python Projects\Useful-Python\Test Data\Combine CSV\MOCK_DATA(2).csv"
]

for file in file_test:
  # Open the CSV file
  with open(file, mode='r', newline='') as file:
      reader = csv.reader(file)
      next(reader)
      # Iterate through the rows
      for row in reader:
          # print(row)
          rowOfData.append(row)

with open(file_test[0], mode='r', newline='') as file:
    reader = csv.DictReader(file)
    # Iterate through the rows
    rowOfData.insert(0, reader.fieldnames)

print(rowOfData)

with open("combineCsv.csv",'w', newline='') as csvfile:
  combineCSVWriter = csv.writer(csvfile)

  for rows in rowOfData:
    if any(rows):
      combineCSVWriter.writerow(rows)
