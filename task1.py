n=input("Enter the student's name: ")
marksheet = {'Alice':85,'Bob':70,'Calvin':78,'Drake':90}
if n in marksheet:
    marks=marksheet[n]
    print(f"{n}'s marks: {marks}")
else:
    print(f"Student '{n}' not found")