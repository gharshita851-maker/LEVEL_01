num=int(input("enter a number."))

if num%3==0 and num%5==0:
    print("the number is divisible by both.")

elif num%3==0 and num%5!=0:
    print("the number is divisible by 3 only.")

elif num%3!=0 and num%5==0:
    print("the number is divisible by 5 only.")

else:
    print("the number is not divisible by both.")