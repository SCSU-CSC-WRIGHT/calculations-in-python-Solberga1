### Lab 1 ###

principal= int(input("Enter the principal amount "))
rate= int(input("Enter the rate of interest "))
time= int(input("Enter the time period (in years): "))

simple_interest= (principal*rate*time)/100

print(f"The simple interest is: {simple_interest}")