# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def runningSum(nums):
#     running_sum_list = [x for x in nums]
#     for i, x in enumerate(nums[1:]):
#         previous_val = running_sum_list[i]
#         running_sum_list[i + 1] = previous_val + x
#     return running_sum_list

# def smallerNumbersThanCurrent(nums):
#     sorted_nums = sorted((e, i) for i, e in enumerate(nums))
#     smaller_numbers_list = [0 for _ in nums]
#     for i, tup in enumerate(sorted_nums[1:], start=1):
#         if sorted_nums[i-1][0] < sorted_nums[i][0]:
#             smaller_numbers_list[tup[1]] = i
#         else:
#             smaller_numbers_list[tup[1]] = smaller_numbers_list[sorted_nums[i-1][1]]
#     return smaller_numbers_list

def myAtoi(str_var):
    if len(str_var) == 0:
        return 0
    str_striped = str_var.lower().split()
    first_element = str_striped[0]
    # check if first index is either + or -
    if first_element[0] == "-" or first_element[0] == "+":
        # check if all elements are digits up until the last number
        alpha_index = 0
        while (alpha_index + 1 < len(first_element)) and first_element[1+alpha_index].isnumeric():
            alpha_index = alpha_index + 1
        magic_number = int(first_element[0:alpha_index])
        if magic_number > 2147483647:
            return 2147483647
        if magic_number < -2147483648:
            return -2147483648
        return magic_number
    else:
        # check if all elements are digits
        alpha_index = 0
        while (alpha_index < len(first_element)) and first_element[alpha_index].isnumeric():
            alpha_index = alpha_index + 1
        if alpha_index >= 1:
            magic_number = int(first_element[0:alpha_index])
            if magic_number > 2147483647:
                return 2147483647
            if magic_number < -2147483648:
                return -2147483648
            return magic_number
        else:
            return 0


if __name__ == '__main__':
    # nums = [1,1,1,1,1]
    # result = runningSum(nums)
    # print(result)
    # nums = [8,1,2,2,3]
    # result = smallerNumbersThanCurrent(nums)

    str1 = "42"
    answer1 = myAtoi(str1)
    str2 = "    -42"
    answer2 = myAtoi(str2)
    str3 = "4193with words"
    answer3 = myAtoi(str3)
    str4 = "words and 987"
    answer4 = myAtoi(str4)
    str5 = "-9128347.2332"
    answer5 = myAtoi(str5)