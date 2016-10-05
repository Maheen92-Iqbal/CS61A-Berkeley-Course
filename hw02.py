def square(x):
    return x * x

def triple(x):
    return 3 * x

def identity(x):
    return x

def increment(x):
    return x + 1

def piecewise(f, g, b):
    """Returns the piecewise function h where:

    h(x) = f(x) if x < b,
           g(x) otherwise

    >>> def negate(x):
    ...     return -x
    >>> abs_value = piecewise(negate, identity, 0)
    >>> abs_value(6)
    6
    >>> abs_value(-1)
    1
    """
    def h(x):
        
        if x < b:
            
            print f(x)
            
        else:
            
            print g(x)
            
    return h


def repeated(f, n):
    """Return the function that computes the nth application of f.

    >>> add_three = repeated(increment, 3)
    >>> add_three(5)
    8
    >>> repeated(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    """
    def repeatation(x):
        
        #first would be the value with x as the input argument
        #then we use the loop uptill n to compute the function n times
        ans = f(x)
        
        for i in range(1,n):
            
            ans = f(ans)
            
        return ans
        
    return repeatation

def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

###################
# Church Numerals #
###################

#f is the function provided to this method
def zero(f):
    
    #lambda = input arguments, : x is equals to expression that is returned
    return lambda x: x

def successor(n):
    
    #in n we provide the function zero and in that we provide first the input argument f which would be a function
    #Now when we did n(f) it means zero(f) 
    #so for example f = increment so increment(2) is equals to 2 (as zero(f) returns x)
    # then we do increment(2) = 3
    
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    """Church numeral 1: same as successor(zero)"""
    
    def result(x):
        
        return f(x)
        
    return result
    
def two(f):
    
    """Church numeral 2: same as successor(successor(zero))"""
    
    def middle_fnc(x):
        
       result = f(f(x))
       return result
      
    return middle_fnc
        
#successor(successor(successor(zero)))
three = successor(two)

def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    # n = zero,one....etc and f is the function which we will give as increment and increment of 0 is 1
    # then increment(increment(0)) = increment(1) = 2 => (church_to_int(two))
    # so on..
    return n(increment)(0)
        
        

def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.

    >>> church_to_int(add_church(two, three))
    5
    """
    x = church_to_int(m)
    y = church_to_int(n)

    return x + y
    
def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.

    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    x = church_to_int(m)
    y = church_to_int(n)

    return x * y
    

def pow_church(m, n):
    """Return the Church numeral m ** n, for Church numerals m and n.

    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    "*** YOUR CODE HERE ***"
    x = church_to_int(m)
    y = church_to_int(n)

    return pow(x,y)
