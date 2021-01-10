# Bill Division

def bonAppetit(bill, k, b):
    bon_appetit = 0
    for i in range(len(bill)):
        if i !=k:
            bon_appetit += bill[i]
    
    bon_appetit /= 2

    if bon_appetit == b:
        print("Bon Appetit")
    
    else:
        print(int(abs(bon_appetit - b)))

k = 1
b = 7
bill = [3, 10, 2, 9]

bonAppetit(bill, k, b)