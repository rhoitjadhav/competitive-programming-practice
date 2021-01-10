# Day of the Programmer
import datetime


def dayOfProgrammer(year):
    if year == 1918:
        return "26.09." + str(year)

    elif (year <= 1917) & (year % 4 == 0):
        return "12.09." + str(year)

    elif (year > 1918) & (year % 400 == 0):
        return "12.09." + str(year)

    elif (year > 1918) & (year % 4 == 0):
        if (year % 100 != 0):
            return "12.09." + str(year)

    return "13.09." + str(year)


year = 1800

result = dayOfProgrammer(year)

print(result)

obj = datetime.datetime(year, 1, 1) + datetime.timedelta(256 - 1)

print(obj.strftime("%d.%m.%Y"))
