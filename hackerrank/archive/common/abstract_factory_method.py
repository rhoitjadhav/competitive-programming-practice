class DSA:
    def price(self):
        return 11000

    def __str__(self):
        return "DSA"


class STL:
    def price(self):
        return 8000
    
    def __str__(self):
        return "STL"


class SDE:
    def price(self):
        return 15000

    def __str__(self):
        return "SDE"


if __name__ == "__main__":
    dsa = DSA()
    stl = STL()
    sde = SDE()

    print("Name of course is {} and its price is {}".format(dsa, dsa.price()))
    print("Name of course is {} and its price is {}".format(stl, stl.price()))
    print("Name of course is {} and its price is {}".format(sde, sde.price()))
