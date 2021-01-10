# Time Conversion

def timeConversion(s):
    hh, mm, ss = s.split(":")
    if "PM" in s:
        ss = ss.split("P")[0]

        if int(hh) < 12:
            result = 12 + int(hh)
        else:
            result = int(hh)

    else:
        ss = ss.split("A")[0]
        if int(hh) < 12:
            result = int(hh)
        else:
            result = 12 - int(hh)

    return "{:02d}:{}:{}".format(result, mm, ss)


s = "12:05:45AM"


result = timeConversion(s)

print(result)
