def calculate(a, *args, **kwargs):
    mode = kwargs.get('mode','add')
    def modes(a, *args):
        if mode == "add":
            return a + sum(args)
        elif mode == "mul":
            result = a
            for arg in args:
                result *= arg
            return result
        elif mode == "avg":
            return (a + sum(args)) / (1 + len(args))
    return modes(a,*args)

print(calculate(2, 3, 4, mode="add"))
print(calculate(2, 3, 4, mode="mul"))
print(calculate(2, 3, 4, mode="avg"))
print(calculate(2,4))
print(calculate(2, mode="mul"))
#print(calculate())
