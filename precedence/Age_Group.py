# Input from the user
age = int(input("Enter Age Group: "))

# Function to check the age group
def check_age_group(age):
    if age < 0:
        return "Invalid age!"
    elif age <= 12:
        return "Child"
    elif age <= 17:
        return "Teenager"
    elif age <= 35:
        return "Young Adult"
    elif age <= 55:
        return "Adult"
    else:
        return "Invalid Age"

# Check the age group
age_group = check_age_group(age)

# Display the result
print(f"You belong to the '{age_group}' age group.")

#Age Group Categories:

# Child: 0–12 years
# Teenager: 13–17 years
# Young Adult: 18–35 years
# Adult: 36–55 years
# Senior: 56-150 years