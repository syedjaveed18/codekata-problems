n = input()
employees_salary = input().split()
salary = employees_salary[1::2]
salary.sort()
for i in salary:
    print(employees_salary[employees_salary.index(i) - 1])
