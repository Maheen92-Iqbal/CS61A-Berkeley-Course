def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    if n <= 3:
        
        return n
        
    else:
        
        return g(n-1) + 2*g(n-2) + 3*g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    if n <= 3:
        
        return n
        
    else:
        
        #In this particular problem we do (n-3) means that how many loops we need to make
        #with each loop we update the values of b and c and a
        #these values are shifted to the right
        #We then return the sum through iteration rather than recursion
        
        a,b,c = 1,2,3
        
        for i in range((n-3)):
            
            a,b,c = b,c,c+2*b+3*a
            
        return c

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    number = str(k)
    digits = map(int, list(number))
    
    for i in digits:
        
        if i == 7:
            
            value = True
            break
        else:
            
            value = False
            
    return value
            

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    
    def select_number(k,direction,ret):
        
        if k == n:
            
            return ret + direction
            
        elif k%7 == 0 or has_seven(k):
            
                        
            return select_number(k+1,-direction,ret+direction)
            
        else:
           
                      
           return select_number(k+1,direction,ret+direction)
           
    return select_number(1,1,0) 
              
            
def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    
    
    def select_count(k,result):
        
               
        if result == 0:
            
            return 1
            
        elif result < 0:
            
            return 0
            
        elif k > result:
            
            return 0
            
        else:
          
           
           one_kind = select_count(k,result-k)
          
           all_kind_without_one = select_count(k*2,result)
           
           return one_kind + all_kind_without_one
           
    return select_count(1,amount) 
              
    

def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game, starting
    with n disks on the start pole and finishing on the end pole.

    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"
   
    if n == 1:
        
        print 'Move the top disk from ' + str(start) + ' to ' + str(end)
        
    else:
        
        spare = 6 - start - end
        
        towers_of_hanoi(n-1,start,spare)
        towers_of_hanoi(1,start,end)
        towers_of_hanoi(n-1,spare,end)


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    
    def fact(n):
        
        if n == 1:
            
            return 1
            
        else:
            
            return mul(n,fact(sub(n,1)))
            
    return fact
