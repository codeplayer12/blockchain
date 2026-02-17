name = input("Enter your name: ")
age = int(input("Enter your age: "))

def user_info(name, age):
    """
    Gets the user and age input and prints them out

    Arguments:
        :param name: Gets user name input as a string
        :param age: Get user age input as an int
    """
    print(f"Your name is {name} and your age is {age}")


def calculate_decades_lived(age):
    """
    Returns the modulus of the age to show decades lived
    Arguments:
        :param age: Gets the user age input
    
    Returns the decades lived
    """
    return age // 10


def print_decades_lived():
    """
    Prints the decade lived as a string
    """
    decades_lived = calculate_decades_lived(age)
    print(f"{age} = {decades_lived} decades")

user_info(name,age)
print_decades_lived()