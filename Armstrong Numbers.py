def is_armstrong_number(number):
    num_str = str(number)
    num_len = len(num_str)
    armstrong_sum = 0
    for digit in num_str:
        armstrong_sum += int(digit) ** num_len
    if armstrong_sum == number:
        return True
    else:
        return False