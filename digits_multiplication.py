# https://github.com/Empire-of-Code-Puzzles/checkio-empire-digits-multiplication

def golf(n):
 return eval('*'.join(i for i in str(n) if i!='0'))

if __name__ == '__main__':
   # These "asserts" using only for self-checking and not necessary for auto-testing
   assert golf(123405) == 120
   assert golf(999) == 729
   assert golf(1000) == 1
   assert golf(1111) == 1
   print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")