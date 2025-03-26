a = 69

def f1(): 
    a = 99  
    print('f1() called')
    print(a)    

def f2(): 
    global a  # Declare 'a' as global to modify the global variable
    a = 100  
    print('f2() called')
    print(a)

f1()    # Call f1() to see its local variable 'a'
f2()
print(a)  
print(a)