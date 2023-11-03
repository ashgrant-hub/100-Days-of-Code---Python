#LESSON 4 - DAY 1 - VARIABLES

#TASK: Write a program that switches the values stored in the variables a and b.
#The first input is stored in the variable called ‘Python’. The second input is stored in the variable called ‘Monty’. Given are the two inputs: Python and  Monty.

#Assign a variables for “Python” & “Monty”
a="Python"
b="Monty"

#The KEY to this is by introducing a third variable (c)—this is because we temporarily need to store a value here. 

#Using the third variable, here, I will be using ‘c’ are the temporary variable.
c=a
#As ‘c’ took over the variable for ‘a’, ‘a’ now has no value
a=b
#As ‘a’ took over the variable for ‘b’, ‘b’ now has no value
b=c
#As ‘b’ took over the variable for ‘c’, ‘c’ now has no value (which is what we want)

print ("a: " + a)
print ("b: " + b)
