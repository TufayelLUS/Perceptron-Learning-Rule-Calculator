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
        calc = ((w[0] * p[i][0]) + (w[1] * p[i][1])) + b
        print("n: hardlim(" + str(calc) + ")")
        a = hardlim(calc)
        print("a: " + str(a))
        e = t[i] - a
        print("e: " + str(e))
        if e != 0:
            no_error = 0
            ep = [e * p[i][0], e * p[i][1]]
            w = [w[0]+ep[0],w[1]+ep[1]]
            print("w new: ")
            print(w)
            b = b + e
            print("b new: " + str(b))
        else:
            no_error += 1
            if no_error == 3:
                print("Final Answer: ")
                print("Weight:")
                print(w)
                print("Bias:")
                print(b)
                exit()
