def check_password_strength(password):
    has_length=len(password)>=8

    has_upper=False
    has_lower=False
    for char in password:
        if char.isupper():
            has_upper=True
        elif char.islower():
            has_lower=True

    has_digit=False
    for char in password:
        if char.isdigit():
            has_digit=True

    return{
        "length":has_length,
        "case":has_upper and has_lower,
        "digit":has_digit
    }

user_password=input("enter a password:")
results=check_password_strength(user_password)

print("\n--- Results ---")
print(f"At least 8 characters: {results['length']}")
print(f"Has upper & lower case: {results['case']}")
print(f"Has at least one digit: {results['digit']}")