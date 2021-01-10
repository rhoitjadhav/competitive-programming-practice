import re


def validTime(time):
    return bool(re.match('(?:[01]\\d|2[0-3]):[0-5]\\d', time))


time = "00:65"
result = validTime(time)
print(result)