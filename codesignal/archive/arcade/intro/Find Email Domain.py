def findEmailDomain(address):
    return address.split("@")[-1]


address = ""

result = findEmailDomain(address)

print(result)
