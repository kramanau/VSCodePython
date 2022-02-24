def fizzbuzz(n):
    output = []
    for i in range(1,n+1):
        if not (i % 3) and not (i % 5):
            output.append("FizzBuzz")
        elif not (i % 3):
            output.append("Fizz")
        elif not (i % 5):
            output.append("Buzz")
        else:
            output.append(i)
    return output


if __name__ == "__main__":
    print(fizzbuzz(15))