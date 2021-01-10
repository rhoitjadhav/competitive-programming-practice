
# Birthday Cake Candles

def birthdayCakeCandles(candles):
    return candles.count(max(candles))


candles = list(map(int, "3 2 1 3".split()))

result = birthdayCakeCandles(candles)

print(result)
