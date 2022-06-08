import math

functions_available = ["append"]

funcs_present = []
inputfile = open("prac_Exam/input.py").read()
for line in inputfile.split('\n'):
    for func in functions_available:
        if line.find('arr'+'.'+func) > -1:
            funcs_present.append(func)

print("Functions detected in input file:",funcs_present, "\n")

def amortized_aggregate_dynamic(func):
    # func = list of funcs in order

    cost = 0
    for i in range(len(func)):
        if i > 0 and math.log2(i).is_integer() and func[i] == "append":
            cost += i-1
        cost += 1

    amortized_cost = cost/len(func)
    return int(math.ceil(amortized_cost))

def amortized_accounting_dynamic(func):
    #  trial and error
    # func = list of funcs in order
    bank = 0
    try_cost = 1
    while bank >= 0:
        for i in range(len(func)):
            if func[i] == "append":
                if i > 0 and math.log2(i).is_integer():
                    bank -= i
                bank += try_cost
                bank -= 1
            if bank < 0:
                try_cost += 1
                break
        if bank >= 0:
            return try_cost
        bank = 0

    #  assume 'd' coins for each insertion. 1 coin for inserting if we dont need to resize.
    #  So, we save d-1 coins at each step to pay for extra cost whike copying array in future.
    # Suppose we resize at size k, k/2 elements haven't been copied before. So we can use the coins saved while inserting them.
    # (d - 1)*k/2 >= k
    # d >= 3
    # So, minimum cost is 3

def amortized_potential_dynamic(func):
    # potential func = 2n - m
    # n = current number of elements
    # m = length of array
    n = 0
    m = 0

    actual_cost = 0

    for i in range(len(func)):
        if func[i] == "append":
            if n > 0 and m == n and math.log2(n).is_integer():
                m *= 2
                actual_cost += n
            if n == 0:
                m = 1
            n += 1
            actual_cost += 1
        
    return int(math.ceil((actual_cost + (2*n - m) - 0) / len(func)))

print("Aggregate:", amortized_aggregate_dynamic(funcs_present))

print("Accounting:", amortized_accounting_dynamic(funcs_present))

print("Potential:", amortized_potential_dynamic(funcs_present))