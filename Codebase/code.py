import pandas as pd
import matplotlib.pyplot as plt

while True:
    print("======PLACEMENT DATA ANALYSIS======")
    print("1. Test Case 1: Normal Input")
    print("2. Test Case 2: Minimum Input")
    print("3. Test Case 3: Invalid Input")
    print("4. Test Case 4: Different Valid Scenario")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = {
            "Student" : ["Aman","Riya","Karan"],
            "Branch" : ["CSE", "CSE", "ECE"],
            "Company" : ["TCS", "Infosys", "Wipro"],
            "Package(LPA)" : [6, 8, 4] 
        }

    elif choice == "2":
        data = {
            "Student" : ["Neha"],
            "Branch" : ["CSE"],
            "Company" : ["TCS"],
            "Package(LPA)" : [3.5]
        }

    elif choice == "3":
        data = {
            "Student" : ["Aman", "Riya", "Karan"],
            "Branch" : ["CSE", "CSE", "ECE"],
            "Company" : ["TCS", "Infosys", "Wipro"],
            "Package(LPA)" : ["abc", 8, -4]
        }

    elif choice == "4":
        data = {
            "Student" : ["Aman", "Riya", "Karan", "Ravi"],
            "Branch" : ["CSE", "CSE", "ECE", "ECE"],
            "Company" : ["TCS", "Infosys", "Wipro", "Accenture"],
            "Package(LPA)" : [6, 8, 4, 12]
        }

    elif choice == "5":
        print("Thankyou!")
        break

    else:
        print("Invalid choice! Please try again.")
        continue

    df = pd.DataFrame(data)

    if choice == "3":
        valid_data = []

        for index, row in df.iterrows():
            package = pd.to_numeric(
                row["Package(LPA)"], errors="coerce"
            )

            if pd.isna(package):
                print("Row", index + 1,
                      "skipped: invalid Package'" +
                      str(row["Package(LPA)"]) + "'")
                
            elif package <= 0:
                print("Row", index + 1,
                      "skipped: Package must be positive.")
                
            else:
                valid_data.append({
                    "Student" : row["Student"],
                    "Branch" : row["Branch"],
                    "Company" : row["Company"],
                    "Package(LPA)" : float(package)
                })

        df = pd.DataFrame(valid_data)
        df = df.drop_duplicates()

    if choice == "4" and len(df) > 0:
        branch_count = df.groupby("Branch").size()
        branch_average = df.groupby("Branch")["Package(LPA)"].mean()

        print("Placements: ")
        print("|".join(
            branch + ":" + str(branch_count[branch])
            for branch in branch_count.index
        ))

        print("Average Package:")
        print("|".join(
            branch + " " + "{:.2f}".format(branch_average[branch])
            for branch in branch_average.index
        ))

        print("Above 7 LPA:")
        filtered_data = df[df["Package(LPA)"] > 7]
        print(" | ".join(
            row["Student"] + "({:.2f})".format(row["Package(LPA)"])
            for _, row in filtered_data.iterrows()
        ))

        plt.figure()
        plt.pie(
            branch_count.values,
            labels=branch_count.index,
            autopct="%1.1f%%"
        )
        plt.title("Branch-wise Placements")
        plt.show(block=True)

        plt.figure()
        plt.bar(
            branch_average.index,
            branch_average.values
        )
        plt.xlabel("Branch")
        plt.ylabel("Average Package (LPA)")
        plt.title("Branch-wise Average Package")
        plt.show(block=True)

    elif choice in ["1", "2", "3"]:
        if len(df) == 0:
            print("No valid placement records found.")

        else:
            total = len(df)
            avg = df["Package(LPA)"].mean()
            highest = df["Package(LPA)"].max()
            student = df[df["Package(LPA)"] == highest].iloc[0]
            
            if choice == "3":
                print("Valid records: {} | Total placed: {}".format(total, total))        
                print("Average package: {:.2f} LPA".format(avg))

            else:
                print("Total placed:", total,
                      "| Average package: {:.2f} LPA".format(avg))
        
                print("Highest: {:.2f} LPA ({}, {})".format(
                    highest,
                    student["Student"],
                    student["Company"]
                ))