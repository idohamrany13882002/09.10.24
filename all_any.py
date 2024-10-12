# check if a list [True, False, False, True] contains at least 1 False
#   if yes -- print '1+ False' else print '0 False'
if any([True, False, False, True]):
    print("+1 False")
else:
    print("0 False")

# check if a list [False, False, False, False] contains all False
#   if yes -- print 'All False' else print 'not All False'
if all([False, False, False, False]):
    print("not all False")
else:
    print("all False")

# *Bonus: check if a list [3, 9, 12, 15, 16] contains only numbers divided by 3 no reminder
#   if yes -- print 'All 3 divided' else print 'not All3 divided'
if all(num % 3 == 0 for num in [3, 9, 12, 15, 16]):
    print("all divisible by 3")
else:
    print("not all divisible by 3")

bool1: list[bool] = [True, True, True]
bool2: list[bool] = [True, True, False]
bool3: list[int] = [20, 0, 300, 100, 100]
print('all bool1', bool1, all(bool1))  # ? True
print('all bool2', bool2, all(bool2))  # ? False
print('all bool3', bool3, all(bool3))  # ? False

bool1: list[bool] = [True, True, True]
bool2: list[bool] = [True, True, False]
bool3: list[int] = [20, 0, 300, 100, 100]
bool4: list[bool] = [False, False]
bool5: list[int] = [0, 0, 0, 0, 0]
print('any bool1', bool1, any(bool1))  # ? True
print('any bool2', bool2, any(bool2))  # ? True
print('any bool3', bool3, any(bool3))  # ? True
print('any bool4', bool4, any(bool4))  # ? False
print('any bool5', bool5, any(bool5))  # ? False
