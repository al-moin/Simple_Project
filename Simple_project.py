first_name =input("Write Your First Name:")
second_name =input("Write Your Second Name:")

full_name = f"{first_name} {second_name}"

print("Your Full Name Is :",full_name)
print("Title Format:",full_name.title())
print("Upper Case Format:",full_name.upper())

change_second_name =input("Replace Your Second Name :")
new_full_name =full_name.replace(second_name,change_second_name)
print("Your Old Full Name is",full_name,". Your New Full Name Is",new_full_name)

