# Name: Samuel Hamilton.
# ID#: 620119624
def hello():
    print("ECSE3038 - Engineering IoT Systems")

def checkPassword(password):
        alnum, digits = 0, 0

        if len(password) >= 8 and password.isalnum():
            for i in password:
                try:
                    if i.isdigit():
                        digits = digits + 1
                except:
                    pass
            if digits >= 2:
                return True

        return False
def sumUpToN(digit):
    val = 0
    if digit > 1:
        for i in range(1, digit+1):
            val += i
    else:
        val = -1
    return val
if __name__ == "__main__":

# Part 1
    hello()
    print("\n")

# Part 2
    password = "Lalalalalala12"
    if checkPassword(password):
        print("This password is valid since it has more than 8 characters, ")
        print("and has at least two numbers and consists of alphanumeric characters only. ")
        print("\n")
    else:
        print("The password must only have alphanumeric characters and atleast two numbers. ")

# Part 30
    SUM = sumUpToN(-5)
    print(SUM)


