def find_the_gcd(a,b):

    while b: #Euclid Algoritması
        a,b=b,a%b
    return a
numb1=int(input("Enter a number: "))
numb2=int(input("Enter a second number: "))
print(f"GCD is {find_the_gcd(numb1,numb2)} ")
