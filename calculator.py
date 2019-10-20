# p[i] = input
# t[i] = target
# w = weight
# b = bias
p = {}
t = {}
p[1] = [1, 2]
t[1] = 1
p[2] = [-1,2]
t[2] = 0
p[3] = [0,-1]
t[3] = 0
w = [0,0]
b = 0
no_error = 0
def hardlim(val):
    return 1 if val >= 0 else 0
iteration = 0
while True:
    for i in range(1,4):
        print "Iteration " + str(iteration)
        print("w old: ")
        print(w)
        print("b old: " + str(b))
        iteration += 1
        # calculate wp+b
        calc = ((w[0] * p[i][0]) + (w[1] * p[i][1])) + b
        print("n: hardlim(" + str(calc) + ")")
        a = hardlim(calc)
        print("a: " + str(a))
        # calculate e = t-a
        e = t[i] - a
        print("e: " + str(e))
        if e != 0:
            no_error = 0
            # calculate w_new = w_old + e * p(Transpose)
            ep = [e * p[i][0], e * p[i][1]]
            w = [w[0]+ep[0],w[1]+ep[1]]
            print("w new: ")
            print(w)
            # calculate b_new = b_old + e
            b = b + e
            print("b new: " + str(b))
        else:
            no_error += 1
            if no_error == 3:
                # 3 input, 3 consecutive matches
                print("Final Answer: ")
                print("Weight:")
                print(w)
                print("Bias:")
                print(b)
                exit()
