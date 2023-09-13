employees = [
    {
        "first_name": "Jose",
        "last_name": "Lopez",
        "email": "joselopez0944@example.com",
        "age": 25,
        "job_title": "Project Manager",
        "years_of_experience": 1,
        "salary": 8500,
        "department": "Product"
    },
    {
        "first_name": "Diane",
        "last_name": "Carter",
        "email": "dianecarter1228@example.com",
        "age": 26,
        "job_title": "Machine Learning Engineer",
        "years_of_experience": 2,
        "salary": 7000,
        "department": "Product"
    },
    # ... (other employee data)
]

# Task 1: Print the name of the person with the highest salary
highest_salary_employee = max(employees, key=lambda x: x["salary"])
print("Person with the highest salary:", highest_salary_employee["first_name"], highest_salary_employee["last_name"])

# Task 2: Print the combined years of experience of all employees
combined_experience = sum(employee["years_of_experience"] for employee in employees)
print("Combined years of experience:", combined_experience)

# Task 3: Collect details of employees without an email address
employees_without_email = [employee for employee in employees if employee["email"] is None]
print("Employees without email:", employees_without_email)

# Task 4: Compare total salaries in the Product and Business departments
product_department_salaries = sum(employee["salary"] for employee in employees if employee["department"] == "Product")
business_department_salaries = sum(employee["salary"] for employee in employees if employee["department"] == "Business")
if product_department_salaries > business_department_salaries:
    print("Product department costs more.")
else:
    print("Business department costs more.")

# Extension 5: Calculate the average salary for people over 30 years of age
over_30_employees = [employee for employee in employees if employee["age"] > 30]
average_salary_over_30 = sum(employee["salary"] for employee in over_30_employees) / len(over_30_employees)
print("Average salary for people over 30:", average_salary_over_30)

# Extension 6: Calculate the count of employees by job title
job_title_count = {}
for employee in employees:
    job_title = employee["job_title"]
    if job_title in job_title_count:
        job_title_count[job_title] += 1
    else:
        job_title_count[job_title] = 1
print("Job title count:", job_title_count)