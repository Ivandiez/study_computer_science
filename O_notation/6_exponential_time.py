# Time complexity: O(c**n), c is constant. In our example O(10**n)
# Space complexity: O(n)
pin = "931"
n = len(pin)
for i in range(10**n):
    if str(i) == pin:
        print(i)