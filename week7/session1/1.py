#Problem 1: Hello Hello
#A recursive function is a function that calls itself within the body of the function.

#Step 1: Copy the recursive function repeat_hello() into Replit and run it.

#tep 2: Then create another function repeat_hello_iterative() that produces the same output without using recursion.

#Compare your iterative (non-recursive) solution to the recursive solution provided. What is similar? What is different?

def repeat_hello(n):
	if n > 0:
		print("Hello")
		repeat_hello(n - 1)
		
#repeat_hello(5)

def repeat_hello_iterative(n):
    if n == 1:
        print ("hello")
    else:
        print ('hello')
        repeat_hello_iterative(n-1)
    
repeat_hello_iterative(5)    
    