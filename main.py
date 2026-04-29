import core.parser as parser
import core.differentiator as differentiator
import core.integrator as integrator

evaluate = True
user_input = 0

user = input("Enter a function: ")
condition = input("Evaluate function? (y/n): ")

if condition == 'y':
    #future implementation: display function before x-input by user
    user_input = float(input("Enter x-value: "))
else:
    evaluate = False

print(differentiator.differentiate(user, user_input, evaluate))
print(parser.parse_function(user, user_input, evaluate))
print(integrator.integration(user, user_input, user_input2, evaluate))
