n = int(input("Enter size of dictionary:"))
vacation_schedule = {}
for i in range(n):
    name, day, month = input().split()
    if month not in vacation_schedule:
        vacation_schedule[month] = []
    vacation_schedule[month].append(name)


requested_month = input("Requested month:")
if requested_month in vacation_schedule:
    print(" ".join(vacation_schedule[requested_month]))
else:
    print()

print("Hello World!")
print("Asanali fkgmklgmkgmk")
print("ASan")
print("Hellooooo")