from z3 import *

user_input = [Int(f'user_input_{i}') for i in range(28)]
solver = Solver()
solver.add(len(user_input) == 28)

solver.add(user_input[4] == 51)
solver.add(user_input[4] - user_input[3] == 1)
solver.add(user_input[15]*2 == 214)
solver.add(user_input[1] + user_input[0] == 147)
solver.add(user_input[11] == 99)
solver.add(user_input[7] - user_input[11] == 9)
solver.add(user_input[21] - user_input[18] == 21)
solver.add(user_input[15]*2 - user_input[13] == 113)
solver.add(user_input[14] * user_input[25] == 5049)
solver.add(user_input[5] == 123)
solver.add(user_input[0] + user_input[1] + user_input[2] == 231)
solver.add(user_input[15] + user_input[11] + user_input[14] == 305)
solver.add(user_input[21] + user_input[11] == 215)
solver.add(user_input[0] * user_input[25] == 4080)
solver.add(user_input[9]*2 == 206)
solver.add(user_input[17] - user_input[9] == 11)
solver.add(user_input[27] - user_input[25] == 74)
solver.add(user_input[26] + user_input[27] + user_input[25] == 271)
solver.add(user_input[26] == user_input[23])
solver.add(user_input[23] == user_input[10])
solver.add(user_input[6] * 2 == 204)
solver.add(user_input[12] - user_input[6] == 2)
solver.add(user_input[12] - user_input[16] == 3)
solver.add(user_input[22] / 2 == 52)
solver.add(user_input[20] - user_input[22] == 1)
solver.add(user_input[24] * 2 == 244)
solver.add(user_input[24] + user_input[19] == 241)
solver.add(user_input[8] == 97)

if solver.check() == sat:
    model = solver.model()
    solution = [model.evaluate(ui).as_long() for ui in user_input]
    print("Solution found:")
    for i in solution:
        print(chr(i), end="")
else:
    print("No solution found.")

