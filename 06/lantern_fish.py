'''Multiplying Lantern Fish'''

from typing import no_type_check


state = [3,4,3,1,2]


'''
Rules.

If value == 0: reset value to 6 + create another value of 8
Each Iteration Reduce each value by 1 that is present at the start of the iteration

'''



day = 1
print(f"Initial state: {state}")
while day <= 80:
    new_nums = []
    for key, value in enumerate(state):
        if value == 0:
            state[key] = 6
            new_nums.append(8)
        else:
            state[key] -= 1
    for i in new_nums:
        state.append(i)
    if day < 10:
        print(f"After {day} {'day' if day == 1 else 'days'} {state}")
    if day == 18:
        print(f"After {day} {'day' if day == 1 else 'days'} {state}")

    day += 1

print(len(state))