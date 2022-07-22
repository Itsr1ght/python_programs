
class Divisors:
    def __init__(self, num):
        self.num = num
        self.number = []
        for i in range(1, self.num+1):
            if self.num % i:
                pass
            else:
                self.number.append(i)   

    def get_sum(self) -> int:
        return sum(self.number)

    def get_count(self) -> int:
        return len(self.number)


num = int(input("Enter a number greater than 1:"))

if num<2:
    print("error : low value")
else:
    divisor = Divisors(num)
    print(f"The number of divisor of {num} is {divisor.get_count()}")
    print(f"The sum of divisor of {num} is {divisor.get_sum()}")