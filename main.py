from adder import Adder

my_adder = Adder(2, 3)

print('Class method from class:')
Adder.seven_and_five()
print('\nStatic method from class:')
Adder.addition_static(6, 5)
print('\nInstance method from instance:')
my_adder.addition()
print('\nClass method from instance:')
my_adder.seven_and_five()
print('\nStatic method from instance:')
my_adder.addition_static(7, 8)
