# # Exercise 1
# nums1 = [1, 3, 5, 7, 8, -1, -3, -5, -7, -8, -100, -534, -32, -15, -77,
#          -222, -788, -345, -75645, -22, 100, 534, 32, 15, 77, 222, 788, 345, 75645, 22]

# # Given an array of positive integers nums, return a list of all of the negative integers.

# # def negative_list(num_list):
# #     neg_list = []
# #     for num in num_list:
# #         if num >= 0:
# #             neg_list.append(-num)
# #         else:
# #             if num < 0:
# #                 neg_list.append(num)
# #     return neg_list
# # print(negative_list(nums1))

# def make_negative(negativenums):
#     negativenumbs = [-num for num in negativenums or -num for -num in negativenums] 
#     return negativenumbs
# print(make_negative(nums1))
# for it to work with any numbers
# Exercise 2

# Given a string, return a list of all of the digits in the string.
# Ex. 1
# address = "123 Real Street, Apt. 2, Springfield, OR 43498"
# Expected Output: ['1', '2', '3', '2', '4', '3', '4', '9', '8']


sentence = "My phone number is (555) 555-4321"
def string_return(string_numbers):
    num_string = [num for num in string_numbers if num.isdigit() > 0]
    return num_string
print(string_return(sentence))


# Exercise 3

# Given a string digits, return a string of the digits + 1
# digits = '122'
# def add1(number):
#     number = int(number) + 1
#     return str(number)
# print(add1(digits))


# Ex. 1
# digits = '123'
# Expected Output: '124'

# Ex. 2
# digits = '99'
# Expected Output: '100'
