def depositProfit(deposit, rate, threshold):
    years = 0
    while deposit < threshold:
        percent = lambda part, whole:float(whole) / 100 * float(part)
        deposit += percent(rate, deposit)
        years += 1

    return years

d, r, t = 1, 100, 64
result = depositProfit(d, r, t)
print(result)

