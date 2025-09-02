
# Simple Password Strength Checker with Retry

def check_strength(password):
    strength = 0

    # length check
    if len(password) >= 8:
        strength += 1

    # lowercase check
    if any(c.islower() for c in password):
        strength += 1

    # uppercase check
    if any(c.isupper() for c in password):
        strength += 1

    # number check
    if any(c.isdigit() for c in password):
        strength += 1

    # special char check
    specials = "@#$%^&*!?"
    if any(c in specials for c in password):
        strength += 1

    return strength


while True:
    password = input("Enter a password: ")
    strength = check_strength(password)

    if strength == 5:
        print("Very Strong ")
        break
    elif strength == 4:
        print("Strong ")
        break
    elif strength == 3:
        print("Okay ")
        break
    elif strength == 2:
        print("Weak ")
        break
    else:
        print("Very Weak , please try a stronger password!\n")
