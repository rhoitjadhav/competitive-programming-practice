# Is IPv4 Address
def isIPv4Address(s):
    if s[0] == ".":
        return False
    string_array = s.split(".")
    if len(string_array) != 4:
        return False

    for i in string_array:
        if len(i) > 1:
            if i[0] == "0":
                return False 
        try:
            i = int(i)
        except:
            return False

        if (i < 0) or (i > 255):
            return False

    return True

# dnl-blkv's solution
def isIPv4Address1(s):
    p = s.split('.')
    return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)

# vanpet90's solution
import ipaddress
def isIPv4Address2(inputString):
    try:
        ipaddress.ip_address(inputString)        
    except:
        return False
    return True

if __name__ == "__main__":
    s = "1.1.1.1.1"
    print(isIPv4Address(s))
