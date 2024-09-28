

#ماشین حساب(Calculator)

#تابع تعیین علامت(Determining the mathematical operator)
def alamat55():
    while True: 
        alamat1 = input ("Please enter your operator [ +,  -,  /,  *,  **,  % ]: ")
        if alamat1 in  ["*","/","-","+","**","%"]:
               return alamat1    
        else:
            print("\n","You used the wrong operator, ","\n","just: [ +,  -,  /,  *,  **,  % ]","\n")




#تابعی که فقط عدد دریافت میکند(A function that only receives numbers)
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
           print("\n","You entered something other than a number","\n", "please use numbers. ","\n")


#تابعی که کل محاسبات را انجام میدهد(A function that performs all calculations)
def mashin(adad1,alamat,adad2):
    if alamat == "+":
        javab = adad1 + adad2
    elif alamat == "**":
        javab = adad1 ** adad2
    elif alamat == "%":
        if adad2 == 0:
            print("\n","You cannot request the remainder of a number divided by zero. ","\n")
            return
        else:
            javab = adad1 % adad2    
    elif alamat == "-":
        javab = adad1 - adad2
    elif alamat == "/":
        if adad2 != 0:
            javab = adad1 / adad2
        else:
            print("\n","You cannot divide a number by zero. ","\n")
            return
    elif alamat == "*":
        javab = adad1 * adad2

    print(adad1,alamat,adad2,"=",javab)


#گرفتن ورودی و صدا کردن تابع ها(Taking input and calling functions)

print("\n\n\t\t","Created by: Abolfazl Tahery Haghighi","\n\n\t\t\t\t","V 1.0.0","\n\n")

plp = "yes"
pkp = "yes"
while plp == pkp:
    
    adad11 = get_number("Enter the desired first number: ")
    print("\n")
    alamat1 = alamat55()
    print("\n")
    adad22 = get_number("Enter the second desired number:")
    print("\n")
   
    mashin(adad11,alamat1,adad22)
    pkp = input("try agian ? (yes or no)")
input("please hit enter to exit the app.")
exit()

# V 1.0.0
#Created by:Abolfazl Taheri Haghighi
#https://t.me/Aboli_est
#https://wa.me/989174874818