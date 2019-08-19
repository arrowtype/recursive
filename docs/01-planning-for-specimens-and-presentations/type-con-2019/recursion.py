def countUp(number, max):
    print(number)
    if number < max:
        countUp(number + 1, max)

countUp(1,500)
