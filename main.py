""" Implementation of a REPL (Read-Eval-Print-Loop) """


class Repl:
    running = True
    chunk = ""
    i = 0

    nums = []
    op = []
    def __init__(self, running, exp):
        self.running = running
        self.exp = exp
        self.i = i
        self.chunk = chunk
        self.nums = nums
        self.op = op


    def evaluation(self):
        chunk = exp.split(" ")
        # chunk = exp
        l = 0
        # for l in range(len(chunk)):
        for l in chunk:
            # print(chunk[l])

            if (l.isnumeric()):
                print(f"{l} will be added to the nums")
                Repl.nums.append(int(l))

            elif (l.isspace()):
                pass

            elif (l == "q"):
                Repl.running = False
                break
            else:
                print(f"{l} is on the op, using now")
                Repl.op.append(l)
            
        for t in chunk:
            if (not len(Repl.op) == 0):
                if (Repl.op.pop() == "+"):
                    lhs = Repl.nums.pop()
                    rhs = Repl.nums.pop()
                    print(f"[{i}] {lhs + rhs}")
            else:
                pass

            # print(f"type of {chunk[l]}: {type(chunk[l])}")
       
    def runner(self):
        #while Repl.running:
            # prompt = input("> ")
        # print(f"[{i}] {eval(exp)}")
        Repl.evaluation(exp)
        pass


# exp = "5 + 6"
i = 0
while Repl.running:
    try:
        i += 1
        exp = input(f"[{i}]> ")
        if (exp == "exit"):
            Repl.running = False
            break

        Repl.runner(exp) 
    except KeyboardInterrupt:
        break
    except SyntaxError:
        print(f"{Repl.chunk} token is not allowed")
