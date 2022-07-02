n = int(input())
attendance_entry = input()
attendance = (attendance_entry.count('P')/n) * 100

print("Blacklisted") if attendance <= 25 else print("Not Blacklisted")
