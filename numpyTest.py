import numpy as np


#zeros created an array with float values equal to the arguement
b= np.zeros(3)
print "numpy.zeros creates arrays with zero float values as well as numpy.ones: " + str(b)
print type(b[0])
print ""


#returns the shape of the array
print b.shape
#changing the shape to 3 rows in one column can be changed to expand the flexiblity of arrays for refrence and seperation 
b.shape = (3,1)
print "Reshaping Array" + str(b)


print ""


print "You can also create an empty array with .empty:" 
b=np.empty(3)
print b 

print ""

print "Creating specified arrays with numpy.linspace :"
b=np.linspace(2,10,5)
# linspace(a,b,c) a=starting number b=ending number c=the amount of values
print "b=np.linspace(2,10,5)"
print b


print ""

print "Creating random arrays np.random.randint(10,size=6):"
#bumpy.random.randint(a,size=b) Creates a random array of number from 0 to ten with the array length of six values
b=np.random.randint(10,size=6)
print b
