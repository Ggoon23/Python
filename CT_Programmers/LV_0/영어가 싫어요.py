numbers = "onetwothreefourfivesixseveneightnine"


def solution(numbers):
    
    if "zero" in numbers:
        numbers = numbers.replace("zero", "0")
    if "one" in numbers:
        numbers = numbers.replace("one", "1")
    if "two" in numbers:
        numbers = numbers.replace("two", "2")
    if "three" in numbers:
        numbers = numbers.replace("three", "3")
    if "four" in numbers:
        numbers = numbers.replace("four", "4")
    if "five" in numbers:
        numbers = numbers.replace("five", "5")
    if "six" in numbers:
        numbers = numbers.replace("six", "6")
    if "seven" in numbers:
        numbers = numbers.replace("seven", "7")
    if "eight" in numbers:
        numbers = numbers.replace("eight", "8")
    if "nine" in numbers:
        numbers = numbers.replace("nine", "9")

    return int(numbers)


print(solution(numbers))