
def get_gcd(a,b):
    if not a:
        return b
    else:
        return get_gcd(b%a, a)

a,b = int(input("Enter the First numbers : ")) , int(input("Enter the second number : "))
num = get_gcd(a, b)
print(f"gcd value of {a} and {b} are {num}") 