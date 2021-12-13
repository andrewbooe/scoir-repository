import csv
import os

rows = []

def fileInput():
    fileName = input("Enter file name: ")
    if os.path.exists(fileName) == False:
        print("Invalid input.")
        fileInput()
    else:
        readFile(fileName, rows)
    
def readFile(fileName, rows):
    with open(fileName, "r") as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            rows.append(row)
    filterFile(rows)

def filterFile(rows):
    filter = input("If you want to exit, type 'exit'. Else, filter by 'first_name', 'last_name', or 'birth_year': ")
    if (filter == "first_name"):
        firstName = input("Enter first name: ")
        for row in rows:
            if (firstName in row[0]):
                print(row)
        filterFile(rows)
    elif (filter == "last_name"):
        lastName = input("Enter last name: ")
        for row in rows:
            if (lastName in row[1]):
                print(row)
        filterFile(rows)
    elif (filter == "birth_year"):  
        birthYear = input("Enter 4-digit birth year: ")
        for row in rows:
            if (birthYear in row[2][0:4]):
                print(row)
        filterFile(rows)
    elif (filter == "exit"):
        return
    else:
        print("Invalid input.")
        filterFile(rows)
        
fileInput()