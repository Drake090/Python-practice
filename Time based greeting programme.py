# Time based greeting programme.
time = int(input("Enter the time (24 Hour format)"))
if 5<=time and time<12:
 print("Good Morning!")
elif 12<=time and time<17:
 print("Good Afternoon!")
elif 17<time and time<20:
 print("Good Evening")
else:
 print("Good Night")

