no_of_employee = int(input())
employees_DOB = input().split()

date = [int(date) for date in employees_DOB[::3]]
month = employees_DOB[1::3].copy()
year = [int(year) for year in employees_DOB[2::3]]

employees_index = ''
for i in range(0,no_of_employee):
    if year[i] <= 1987 :
        if month[i].upper() in ['JANUARY','MARCH','MAY']:
            employees_index += str(i+1) + " "
        elif month[i].upper() == 'JULY' and date[i] <= 22:
            employees_index += str(i+1) + " "
        elif month[i].upper() in ['AUGUST','SEPTEMBER','OCTOBER','DECEMBER'] and year[i] < 1987:
            employees_index += str(i+1) + " "

if len(employees_index) > 0:
    print(employees_index[:-1])
else:
    print(-1)
