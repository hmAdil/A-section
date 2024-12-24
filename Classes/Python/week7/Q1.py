def department_with_highest_experience():
    department_experience = {}
    department_count = {}

    # Read employee data from "employees.csv"
    with open("employees.csv", "r") as file:
        next(file)  # Skip the header line
        for line in file:
            name, age, department, salary, experience = line.strip().split(",")
            experience = int(experience)

            # Accumulate experience and count per department
            if department in department_experience:
                department_experience[department] += experience
                department_count[department] += 1
            else:
                department_experience[department] = experience
                department_count[department] = 1

    # Calculate the average experience for each department
    highest_avg_department = ""
    highest_avg_experience = 0
    for dept, total_experience in department_experience.items():
        avg_experience = total_experience / department_count[dept]
        if avg_experience > highest_avg_experience:
            highest_avg_experience = avg_experience
            highest_avg_department = dept

    return highest_avg_department, highest_avg_experience


def salary_by_age_group():
    age_groups = {"20-30": 0, "31-40": 0, "41-50": 0, "51-60": 0}

    with open("employees.csv", "r") as file:
        next(file)  # Skip the header line
        for line in file:
            name, age, department, salary, experience = line.strip().split(",")
            age = int(age)
            salary = int(salary)

            # Determine the age group and add the salary
            if 20 <= age <= 30:
                age_groups["20-30"] += salary
            elif 31 <= age <= 40:
                age_groups["31-40"] += salary
            elif 41 <= age <= 50:
                age_groups["41-50"] += salary
            elif 51 <= age <= 60:
                age_groups["51-60"] += salary

    return age_groups


def employees_above_average_salary():
    department_salary = {}
    department_count = {}
    employee_data = []
    above_avg_employees = []  # Initialize the list to store results

    # Read employee data and accumulate salaries per department
    with open("employees.csv", "r") as file:
        next(file)  # Skip the header line
        for line in file:
            name, age, department, salary, experience = line.strip().split(",")
            salary = int(salary)

            employee_data.append((name, department, salary))

            # Accumulate salary and count per department
            if department in department_salary:
                department_salary[department] += salary
                department_count[department] += 1
            else:
                department_salary[department] = salary
                department_count[department] = 1

    # Calculate average salary for each department
    department_avg_salary = {}
    for dept in department_salary:
        department_avg_salary[dept] = department_salary[dept] / department_count[dept]

    # Find employees with above-average salary in their department
    for employee in employee_data:
        name, dept, salary = employee
        if salary > department_avg_salary[dept]:
            above_avg_employees.append(name)

    return above_avg_employees



def give_raises():
    updated_data = []

    # Read and update employee data
    with open("employees.csv", "r") as file:
        header = file.readline().strip()  # Save the header
        updated_data.append(header)

        for line in file:
            name, age, department, salary, experience = line.strip().split(",")
            salary = int(salary)
            experience = int(experience)

            # Increase salary by 10% if experience > 5 years
            if experience > 5:
                salary = int(salary * 1.1)  # Increase salary by 10%

            updated_data.append(f"{name},{age},{department},{salary},{experience}")

    # Write the updated data back to the CSV file
    with open("employees.csv", "w") as file:
        for line in updated_data:
            file.write(line + "\n")


print("Department with highest average experience:", department_with_highest_experience())
print("Salary by age group:", salary_by_age_group())
print("Employees with above-average salary:", employees_above_average_salary())
give_raises()
print("Salaries updated for employees with over 5 years of experience.")

