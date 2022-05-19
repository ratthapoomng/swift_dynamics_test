from operator import index


def zero_from_factorial(n:int) -> int:
    if n < 0:
        raise Exception("input must be 0 or greater than 0")
    multiplier_of_5 = n//5
    number_of_zeros = 0
    while multiplier_of_5 > 0:
        number_of_zeros += multiplier_of_5
        multiplier_of_5 = multiplier_of_5 // 5
    return number_of_zeros

if __name__ == "__main__":
    print("please input a factorial number to find number of zeros of the factorial (ex. 5)")
    n = int(input())
    print(zero_from_factorial(n))