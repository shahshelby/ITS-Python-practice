def test():
    print("testing")
    return


def sumOfNum(a, b):
    c = a + b
    print(c)
    return


def fullName(firstName, lastName):
    print(f"{lastName}, {firstName}")
    print("Initials: " + firstName[0] + lastName[0])  # get first letter of firstname and lastname
    return


john = 5
jeff = 4
sumOfNum(john, jeff)
fullName("Jeff", "John")
test()
