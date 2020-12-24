MIN_DRIVING_AGE = 18

def allowed_driving(name, age):
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant"""
    allowed = False
    if age >= MIN_DRIVING_AGE:
        allowed = True

    if allowed:
        output = "is allowed to drive"
    else:
        output = "is not allowed to drive"

    print(f"{name} {output}")

    return
