#Functions with outputs
# def format_names(f_n, l_n):
#     if f_name == "" or l_name == "":
#         return "You didn't provide anything"
#
#     return f"{f_name.title()}  {l_name.title()}"
#
# f_name = input("Enter your First Name:")
# l_name = input("Enter your Last Name:")
# print(format_names(f_n=f_name, l_n=l_name))

#Days in the month

# def is_leap(year):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
#         return True
#     else:
#         return False
#
# def Days_in_month(year, month):
#     if month > 12 or month < 1:
#         return "Invalid month"
#     month_days = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return 29
#
#     return month_days[month - 1]
# enter_year = int(input("Enter the Year:"))
# enter_month = int(input("Enter the Month:"))
# print(is_leap(year = enter_year))
# print(Days_in_month(year = enter_year, month= enter_month))


#Calculator

# def add(n1, n2):
#     return n1 + n2
#
# def sub(n1, n2):
#     return n1 - n2
#
# def mul(n1, n2):
#     return n1 * n2
#
# def div(n1, n2):
#     return n1 / n2
#
# operations = { "+" : add,
#                "-" : sub,
#                "*" : mul,
#                "/" : div
# }
# def calculator():
#     n1 = int(input("Enter the First number:"))
#
#     should_continue = True
#     while should_continue:
#         for symbols in operations:
#             print(symbols)
#         operations_symbols = input("Choose any of the above operations:")
#         n2 = int(input("Enter the Next number:"))
#         calculation_functions = operations[operations_symbols]
#         answer = calculation_functions(n1, n2)
#
#         print(f"{n1} {operations_symbols} {n2} = {answer}")
#         if input(f"Type y to continue with {answer}, or c to do some other calculations:") == "y":
#            n1 = answer
#
#         else:
#             should_continue = False
#             calculator()
# calculator()

# while not calculation_done:
#     operations_symbols = input("Pick another operation:")
#     n3 = int(input("What is your next number:?"))
#     calculation_functions = operations[operations_symbols]
#     second_answer = calculation_functions(first_answer, n3)
#     print(f"{first_answer} {operations_symbols} {n3} = {second_answer}")
#     should_continue = input("Type yes to continue and no for exit").lower()
#     if should_continue == "no":
#         calculation_done = True
#     else:
#         calculation_done = False


