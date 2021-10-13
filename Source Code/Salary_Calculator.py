"""
    Salary Calculator

    This program will calculate 2% raise of salary for each following year that user will receive.

        1. First things first user need to enter their name if the name is empty the program will ask the name again and
           again until name is not empty.

        2. User need to enter their salary that must be over 10000 if salary is not over 10000 the program will be ask
           again.

        3. User need to enter their years worked that also must be between 1 to 10 years if not the program will show
           error message and user need to input the correct year again.

        4. All above are correct and done the program will start calculate the total salary and show the user that their
           salary year by year and total salary.
"""


def main():

    print("Welcome to the Salary Calculator")
    
    name = input("Please enter your name: ")  # User name

    total_salary = 0

    while name == "":  # When input name is "empty" this loop will be start and ask again

        print("Sorry, please enter your name !")

        name = input("Please enter your name: ")

    while name != "":  # When user input name is not "empty" this loop will be start

        salary = float(input("Please enter your beginning salary: "))  # user salary

        while salary < 10000:  # When user input salary is less than 10000 this loop will be start and ask again

            print("Sorry, your beginning salary must be at least 10000")

            salary = float(input("Please enter your beginning salary: "))

        while salary >= 10000:  # When user input salary is greater than 10000 this loop will be start

            years_worked = int(input("Please enter the years worked: "))  # user years worked

            while years_worked > 10:  # When user input years worked is greater than 10 this loop will be start

                print("You must enter a value between 1 and 10")

                years_worked = int(input("Please enter the years worked: "))

                # Start if condition

            if years_worked < 10:  # When user input years worked is less than 10 this "if" condition will be start

                print("Thank you", name)

                print("Your salary will be")

                for years_worked in range(1, years_worked+1):
                    # Start calculating 2% raise of user salary year by year in this "for" loop

                    print("Year", years_worked, ":", "{:.2f}".format(salary))

                    total_salary = total_salary + salary          # Calculating total salary
                    salary = salary + (salary*0.02)               # 2% raise in salary

                print("Total salary is {:.2f}".format(total_salary))    # Total salary will be show

            else:

                print("Somethings wrong!")

            # End if condition

            return years_worked

        return salary

    return name


if __name__ == '__main__':
    main()

    print("")

    print("Created By Min Khant Soe (HakHak)")

    input("")

