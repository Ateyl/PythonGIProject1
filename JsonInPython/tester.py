

def sec_val(tup):
    return tup[1]

x =[(3,5), (1,4), (6,3),(9,2)]
x.sort(key=sec_val )
print(x)

a = lambda num, name: print(num, name)
a(1, 'hello')

b =lambda: print('hello world')
b()