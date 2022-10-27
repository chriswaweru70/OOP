#objects - In an object-oriented program, objects are asked to carry out the tasks that are necessary to achieve a goal.

# "Hello" and ["World"]

#methods - 	In order to get an object to carry out a task, you invoke a method on it. 

# upper and pop 

# classes - A class describes a set of objects with the same behavior. str and list

# public interface - The public interface of a class tells you what you can do with objects of the class.

# encapsulation - The user of a class only knows the public interface, not the implementation details, of a class.


from counter import Counter

#Here is an example of using the Counter class. First, we construct an object of the class:
#Tally is the object
#Tally is also an instance of the class.


tally = Counter()
#reset and click are medhods

#we call the reset method before calling any other methods, so that the _value instance variable is created and initialized

tally.reset()
tally.click()
tally.click()


#getValue is a method to check how many times the button was pushed.

result = tally.getValue()
print("Value:", result)

tally.click()
result = tally.getValue()
print("Value:", result)


#Specifying the Public Interface of a Class

#To see a method in action, we first need to construct an object:
register1 = CashRegister()
   # Constructs a CashRegister object.
   register1.addItem(1.95) 
   



