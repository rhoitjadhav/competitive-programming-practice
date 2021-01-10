# Apple and Orange

def is_fruit_in_range(position, s, t):
    if position >= s and position <= t:
        return True
    else:
        return False


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0
    for apple in apples:
        position = a + apple
        if is_fruit_in_range(position, s, t):
            apple_count += 1

    orange_count = 0
    for orange in oranges:
        position = b + orange
        if is_fruit_in_range(position, s, t):
            orange_count += 1

    print(apple_count)
    print(orange_count)


s, t, a, b = 7, 11, 5, 15

apples = list(map(int, "-2 2 1".split()))
oranges = list(map(int, "5 -6".split()))

countApplesAndOranges(s, t, a, b, apples, oranges)
