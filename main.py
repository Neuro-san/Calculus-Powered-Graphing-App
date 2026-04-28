import core.parser

user = input("Enter a function: ")
#future implementation: display function before x-input by user
user_input = float(input("Enter x-value: "))

print(core.parser.parse_function(user, user_input))