driving_age=18
user_age=input("entre your age: ")
s="q"
if int(driving_age)>int(user_age):
    print("no your not allowed to drive.")
elif int(driving_age)==int(user_age):
    s=input("do you have license?")
    if str(s)=="yes":
        print("yes your allowed to drive")
    else:
        prnt("no your not allowed to drive ")
elif int(driving_age)<=int(user_age):
    s = input("do you have license?")
    if str(s) == "yes":
        print("yes your allowed to drive")
    else:
        prnt("no your not allowed to drive ")

else:
    breakpoint()

print("*** THANKYOU FOR USING ARE APP ***")