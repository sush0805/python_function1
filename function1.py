'''types of variable in functions
1) local variable:-the variable which is declared inside a function called as Local var
This var. wil nt be accessible outside the function
Local var is having a restricted scope
means it will be accessible only to that function or within the function
outside we  cant access.'''

def sample():
    x = 'local'
    print(x)
    def test():
        print(x)
    test()
    print(x)
#calling sample function
sample()
#print(x)  this will give error that x is not define however local variable is only available inside the function
'''if we want ot access local variable outside the function then their sre some methods can used 
1) used reuturn statement'''
def sample1():
    b = 'local1'
    print(b)
    def sam2():
        print(b)
    sam2()
    return b
b = sample1()
print(b)
'''2) used global keyword'''
z = 5
def dem():
    global y
    y = 'glb'
    print(z,y)
dem()
print(z,y)
# ----------------------------
cm = 'udhhav thakrey'
# def politics():
#     cm = cm.replace('uddhav thakrey','eknath shinde')
#     print(cm)
# politics() # in local changing cm is not possible
def politics():
    global cm
    cm = cm.replace('udhhav thakrey','eknath shinde')
politics()
print(cm)
'''2) global variable:= the variable which is available everywhere through out the program
      this variable is called global variable'''
r = 'global'
def demo():
    print(r)
    def demo2():
        print(r + ' ' + 'variable')
    demo2()
demo()
'''3)Non-local variable:- it is associaed with nested function'''
def outer():
    x = 200 #local to outer
    def inner():
        nonlocal x
        x = 400
        print('Inner:',x)
    inner()
    print('Outer:',x)
outer()
print('--------------')
print('before used nonlocal')
def sampl1():
    var_1 = 'local_1'
    def sampl2():
        var_1 = 'local_2'
        print('sampl2',var_1)
    sampl2()
    print('sampl1',var_1)
sampl1()
print('--------------------------')
print('after used nonlocal')
def sampl1():
    var_1 = 'local_1'
    def sampl2():
        nonlocal var_1
        var_1 = 'local_2'
        print('sampl2',var_1)
    sampl2()
    print('sampl1',var_1)
sampl1()