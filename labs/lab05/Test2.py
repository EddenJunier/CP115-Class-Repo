#Biodata
name = input("Enter your name: ")
date_of_birth = input("Enter your date of birth (DD-MM-YYYY): ")
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
nationality = input("Enter your nationality: ")
phone_number = input("Enter your phone number: ")
email = input("Enter your email address: ")



print("\nBiodata Summary:")
print(f"Name: {name}")
print(f"Date of Birth: {date_of_birth}")
print(f"Age: {age}")
print(f"Gender: {gender}")
print(f"Nationality: {nationality}")
print(f"Phone Number: {phone_number}")
print(f"Email: {email}")

years_of_programming = int(input("\nOne more thing, how many years have you been programming? (answer in years total): "))
if years_of_programming < 5:
    print("No job for you. Go homeless and learn more programming skills.")
elif years_of_programming >= 5:
    print("Welcome to the house, ma man")