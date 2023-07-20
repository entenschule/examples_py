def pi(number_of_addends):
    result = 1
    numerator, denominator = 2, 1
    for i in range(number_of_addends):
        result *= numerator / denominator
        if i % 2:
            numerator += 2
        else:
            denominator += 2
    return 2 * result
