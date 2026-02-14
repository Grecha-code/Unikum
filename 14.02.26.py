def factorial(n): # Первая задача
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def combination(all_people, need_people):
    result = factorial(all_people) // (factorial(need_people) * factorial(all_people - need_people))
    return result


def lucky_ticket(number_digits, target_sum):
    result = 0
    start_num = 10 ** (number_digits - 1)
    end_num = 10 ** number_digits - 1

    for i in range(start_num, end_num ):
        s = str(i)
        current_sum = sum(int(j) for j in s)

        if current_sum == target_sum:
            result += 1

    return result