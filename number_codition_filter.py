#Filters for if n is a multiple of 6 AND if the sum of its digits is divisible by 6
multiple_of_six = []
digits_sum_is_multiple_of_six = []
multiple_of_six_and_digits_sum_is_multiple_of_six = []

for n in range(10001):
    SUM = 0
    num = n
    for i in range(len(str(num))):
        SUM += (num % 10)
        num //= 10
    if SUM % 6 == 0:
        digits_sum_is_multiple_of_six.append(n)
    if n % 6 == 0:
        multiple_of_six.append(n)

    if SUM % 6 == 0 and n % 6 == 0:
        multiple_of_six_and_digits_sum_is_multiple_of_six.append(n)

#print(multiple_of_six_and_digits_sum_is_six)


#Fliters for if n is a multiple of 4, the sum of its digits are even and the last digit is not 0

multiple_of_four = []
digits_sum_is_even = []
last_digit_is_not_zero = []
multiple_of_four_and_digits_sum_is_even_and_last_digit_is_not_zero = []

for n in range(5001):
    num = n
    SUM = 0
    for i in range(len(str(num))):
        SUM += (num % 10)
        num //= 10
    if SUM % 2 == 0:
        digits_sum_is_even.append(n)
    if n % 4 == 0:
        multiple_of_four.append(n)
    if n % 10 != 0:
        last_digit_is_not_zero.append(n)
    if SUM % 2 == 0 and n % 4 == 0 and n % 10 != 0:
        multiple_of_four_and_digits_sum_is_even_and_last_digit_is_not_zero.append(n)

amount_of_numbers = len(multiple_of_four_and_digits_sum_is_even_and_last_digit_is_not_zero)

#print(f'There are {amount_of_numbers} numbers that got filtered')

#print("Here are the first 10: ", end='')
#for i in multiple_of_four_and_digits_sum_is_even_and_last_digit_is_not_zero[1:11]:
    #print(i, end=', ')


#Filter for if n is divisible by 12, the sum of the digits is divisible by 3, reversing the digits of the number gives a number that is divisible by 4 and the number does not contain the digit 0

multiple_of_twelve = []
digits_sum_is_divisible_by_three = []
reversed_digits_is_divisible_by_four = []
does_not_contain_digit_zero = []
multiple_of_twelve_and_digits_sum_is_divisible_by_three_and_reversed_digits_is_divisible_by_four_and_does_not_contain_digit_zero = []

for n in range(100001):
    SUM = 0
    num = n
    reversed_num_list = []
    reversed_num = 0
    contains_zero = False
    for i in range(len(str(num))):
        digit = num % 10
        if digit == 0:
            contains_zero = True
        SUM += digit
        reversed_num_list.append(digit)
        num //= 10
    for i in reversed_num_list:
        reversed_num = reversed_num * 10 + i
    if reversed_num % 4 == 0:
        reversed_digits_is_divisible_by_four.append(n)
    if n % 12 == 0:
        multiple_of_twelve.append(n)
    if SUM % 3 == 0:
        digits_sum_is_divisible_by_three.append(n)
    if contains_zero == False:
        does_not_contain_digit_zero.append(n)
    if n % 12 == 0 and SUM % 3 == 0 and reversed_num % 4 == 0 and not contains_zero:
        multiple_of_twelve_and_digits_sum_is_divisible_by_three_and_reversed_digits_is_divisible_by_four_and_does_not_contain_digit_zero.append(n)

#print(multiple_of_twelve_and_digits_sum_is_divisible_by_three_and_reversed_digits_is_divisible_by_four_and_does_not_contain_digit_zero)

#Filter for if n is a multiple of 18, the sum of the squares of its digits is divisible by 9, the reversed digits gives a number greater than the original and the number contains at most one repeated digit

multiple_of_eighteen = []
sum_of_squared_digits_is_divisible_by_nine = []
reversed_digits_greater_than_original = []
number_contains_maximum_one_repeated_digit = []
multiple_of_eighteen_and_sum_of_squared_digits_is_divisible_by_nine_and_reversed_digits_greater_than_original_and_number_contains_maximum_one_repeated_digit = []

for n in range(1, 200001):
    repeated_digits = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    SUM_of_squared_digits = 0
    num = n
    reversed_num_list = []
    reversed_num = 0
    twice_count = 0
    digit_more_than_twice = False

    for i in range(len(str(num))):
        digit = num % 10
        repeated_digits[str(digit)] += 1
        if repeated_digits[str(digit)] == 2:
            twice_count += 1
        if repeated_digits[str(digit)] == 3:
            digit_more_than_twice = True
        reversed_num_list.append(digit)
        SUM_of_squared_digits += (digit ** 2)
        num //= 10

    for i in reversed_num_list:
        reversed_num = reversed_num * 10 + i

    if not digit_more_than_twice and twice_count <= 1:
        number_contains_maximum_one_repeated_digit.append(n)
    if SUM_of_squared_digits % 9 == 0:
        sum_of_squared_digits_is_divisible_by_nine.append(n)
    if reversed_num > n:
        reversed_digits_greater_than_original.append(n)
    if n % 18 == 0:
        multiple_of_eighteen.append(n)
    if n % 18 == 0 and SUM_of_squared_digits % 9 == 0 and reversed_num > n and not digit_more_than_twice and twice_count <= 1:
        multiple_of_eighteen_and_sum_of_squared_digits_is_divisible_by_nine_and_reversed_digits_greater_than_original_and_number_contains_maximum_one_repeated_digit.append(n)

print(multiple_of_eighteen_and_sum_of_squared_digits_is_divisible_by_nine_and_reversed_digits_greater_than_original_and_number_contains_maximum_one_repeated_digit)