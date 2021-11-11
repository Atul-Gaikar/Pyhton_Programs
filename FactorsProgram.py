"""
   * Author - Atul Gaikar
   * Date -  06-Nov-2021
   * Time -  9:41 PM
   * Title - Factors
"""
f = 0
num = int(input("Enter the number: "))

for i in range(2, num + 1):
    if num % i == 0:
        for j in range(2, int(i / 2)):
            if i % j == 0:
                f = 1
                break
        if f == 0:
            print(i)
