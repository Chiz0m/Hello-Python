# name lenght checker
name = "Ch"
name_lenght = len(name)
if name_lenght < 3:
    message = "Name must be at least 3 characters"
elif name_lenght > 50:
    message = "Name can be a maximum of 50 characters"
else:
    message = "Name looks good"

print(message)
