import os
import csv

decision = 1
print("Learning Modalities Analyzer")
filePath = input("Data file path: ")

if os.path.exists(filePath):
    while (decision != str(4)):
        print("\n1. List dates")
        print("2. Learning modality by state on date")
        print("3. Find all Districts by state")
        print("4. Exit\n")
        decision = input("Enter the number of the option (1, 2, 3, or 4):")

        # user enters 1
        # ===========================
        if (decision == "1"):
            with open(filePath, 'r') as file:
                reader = csv.reader(file) # parses through the csv file
                for row in reader:
                    print(row[2]) # prints the dates (found in index 2 of each row)
        # ===========================

        # user enters 2
        # ===========================
        elif (decision == "2"):
            checker = "y"

            while checker == "y" or checker == "Y":
                print("Enter the two digit code (CA, MO, IL, TX, etc.) for a state or 'all' for all states.")
                state = input("State (2 letter code): ")
                date = input("Date (MM/DD/YYYY): ")
                date += " 12:00:00 AM"

                with open(filePath, "r") as file:
                    reader = csv.reader(file)
                    totalSchools = 0
                    totalStudents = 0

                    # index 0: in-person, index 1: hybrid, index 2: remote
                    studentModality = [0, 0, 0]
                    schoolModality = [0, 0, 0]
                    # row[3] = modality, row[4] = number of operational schools, row[5] = total number of students
                
                    for row in reader:
                        if (row[7] == state) and (row[2] == date): # if the data row is in the desired state and date...    
                            totalSchools += int(row[4])
                            totalStudents += int(row[5])

                            if (row[3] == "Hybrid"):
                                studentModality[1] += int(row[5])
                                schoolModality[1] += int(row[4])
                            elif (row[3] == "In Person"):
                                studentModality[0] += int(row[5])
                                schoolModality[0] += int(row[4])
                            else:
                                studentModality[2] += int(row[5])
                                schoolModality[2] += int(row[4])

                    print("-------------------------------")
                    print(f"Date: {date}")
                    print(f"Description: {state}")
                    print(f"{totalSchools} schools")
                    print(f"{totalStudents} students")
                    print("Schools per modality:")
                    print(f"* {schoolModality[0]} ({round((float(schoolModality[0]) / totalSchools) * 100,1)}%) In Person")
                    print(f"* {schoolModality[1]} ({round((float(schoolModality[1]) / totalSchools) * 100,1)}%) Hybrid")
                    print(f"* {schoolModality[2]} ({round((float(schoolModality[2]) / totalSchools) * 100,1)}%) Remote")
                    print("Students per modality:")
                    print(f"* {studentModality[0]} ({round((float(studentModality[0]) / totalStudents) * 100,1)}%) In Person")
                    print(f"* {studentModality[1]} ({round((float(studentModality[1]) / totalStudents) * 100,1)}%) Hybrid")
                    print(f"* {studentModality[2]} ({round((float(studentModality[2]) / totalStudents) * 100,1)}%) Remote")
                    print("-------------------------------")
                    checker = input("\nEnter another state and date: (y/n) ")
        # ===========================

        # user enters 3
        # ===========================
        elif (decision == "3"):
            checker = "y"
            while checker == "y" or checker == "Y":
                print("Enter the two digit code (CA, MO, IL, TX, etc.) for a state or 'all' for all states.")
                state = input("State (2 letter code): ")
                with open(filePath, 'r') as file:
                    reader = csv.reader(file) # parses through the csv file

                    for row in reader:
                        if row[7] == state:
                            print(f"{row[1]}, operational schools: {row[4]}, total students: {row[5]}")
                checker = input("\nEnter another state and date: (y/n) ")
        # ===========================

        # user enters invalid input
        # ===========================
        elif (decision != "4"):
            print("error: invalid input, please enter 1, 2, 3, or 4\n")
        # ===========================

else:
    print("error: file not found")