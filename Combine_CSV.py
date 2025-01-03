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

      # Iterate through the rows
      for row in reader:
          # print(row)
          rowOfData.append(row)

print(rowOfData)

with open("combineCsv.csv",'w', newline='') as csvfile:
  combineCSVWriter = csv.writer(csvfile)

  for rows in rowOfData:
    combineCSVWriter.writerow(rows)
