

def is_prime(n: int):
    if n <= 1:  # 1 is not a prime number
        return False
    if n <= 3: # 2 and 3 are prime numbers and 1 is not
        return True


    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5 # we already checked for 1 , 2 ,3 and 4 isnt a prime number so we can start from 5
    while i * i <= n:
        if (n % i == 0 or
                n % (i + 2) == 0):
            return False
        i = i + 6

    return True

# Question 1 --> function to return the sum of all prime factors
def factor_sum(x:int):
    sum = 0
    for i in range(1, x-1):
        if x % i == 0:
            if is_prime(i):
                sum += i

    return sum


# Question 4 --> A recursive function to return all the numbers between a and b excluding a 3rd number c
def printnumbers(x:int,y:int,z:int):
    if x == y:
        return print(y)
    if x < y and x!=z:
        print(x)
    printnumbers(x+1,y,z)


# Question 5 --> # Create a new list that hold the element in a and makes him appear each element in b number of times
def listproduct(a:list,b:list):
    _newsize = 0
    for i in range(len(b)):
        _newsize += b[i] # finding the new size of for _newlist
    print(_newsize) # check for the new size

    _newlist = [] # create a new list
    for i in range(_newsize): #iterating on _newlist from 0 to the size of _newlist
        if i == len(b): # a condition to stop the loop when we finish the creation
            break
        for j in range(0, b[i]): # iterating on b list
            _newlist.append(a[i]) # adding to the end of _newlist each element in a b[j] amount of times

    print(_newlist) # printing the new list

    return _newlist
