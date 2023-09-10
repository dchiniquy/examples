# name = input("Enter your name: ") # Taking input by user in variable name
# print("Hello ",name) # Printing User's name with Hello

# a = b = 5 # Cascaded assignment
# c , d = 10 , 20 # Tuple assignment
# print("a =",a)
# print("b =",b)
# print("c =",c)
# print("d =",d)

# age = int( input("Enter your age") )
# if age >= 18: 
#     print("You are good")
# else: 
#     print("you are not good")

# for a in [1,2,3,4]: 
#     print(a)

def fibo(number):
    if (number <= 2): 
        print("Wrong input. try again")
    else: 
        fib = [0] * number
        fib[1] = 1
        n = 2
        while n < number: 
            fib[n] = fib[n-1] + fib[n-2]
            n += 1
        print("fib sequence: ")
        print(fib)

number = int (input("Enter a number for fibo: "))
fibo(number)