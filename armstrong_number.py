def check_armstrong(number):
    digits = []
    num = number
    while num > 0:
        digit = num % 10
        digits.append(digit)
        num //= 10

    sum_of_cubes = sum([i**3 for i in digits])
    if sum_of_cubes == number:
        return "It's an armstrong number."
    else:
        return "It's not an armstrong number."


if __name__ == "__main__":
    print(check_armstrong(153))
