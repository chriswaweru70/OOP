##This module defines the Counter class

##Models a tally counter whose a value can be incremented, viewed, or reset

#An object stores its data in instance variables. An instance of a class is an object of the class. 
#By convention, instance variables in Python start with an underscore to indicate that they should be private.
#However, the underscore indicates to class users that they should not directly access the instance variables.
class Counter:
    ## Gets the current value of this counter
    #  @return the current value
    #
    #Each object of a class has its own set of instance variables.
    #A method definition is very similar to a function with these exceptions:
    #A method is defined as part of a class definition.
    #The first parameter variable of a method is called self.
    def getValue(self):
        #it is sufficient to note that instance variables must be referenced within a method using the self parameter (self._value).
        #_value is an instance variable it starts with an _ to show that it is private
        
        return self._value
    
    ##Advance the value of this counter by 1
    #
    def click(self):
        self._value = self._value + 1
        
    ## Resets the value of this counter to 0 
    #
    def reset(self):
        self._value = 0    
        
#Specifying the Public Interface of a Class


## A simulated cash register that tracks the item count and the total amount due.
#

# The method definitions and comments make up the public interface of the class. 
# The data and the method bodies make up the private implementation of the class.
class CashRegister :
   ## Adds an item to this cash register.
   #  @param price the price of this item
   #
   #A mutator method modifies the object on which it operates. The CashRegister class has two mutators: addItem and clear.
   #After you call either of these methods, the object has changed. 
   #You can observe that change by calling the getTotal or getCount methods.
   def addItem(self, price) :
      
  
   ## Gets the price of all items in the current sale.
   #  @return the total price
   #
   # An accessor method queries the object for some information without changing it.
   # The CashRegister class has two accessors: getTotal and getCount.
   def getTotal(self) :
      
  
   ## Gets the number of items in the current sale.
   #  @return the item count
   #
  
   def getCount(self) :
      
  
   ## Clears the item count and the total.
   #
   def clear(self) :
      
      
#Designing the Data Representation

#An object stores its data in instance variables. These are variables that are declared inside the class.
#Go through all methods and consider their data requirements. It is a good idea to start with the accessor methods. 
#For example, a CashRegister object must be able to return the correct value for the getTotal method.

#Constructors
#A constructor defines and initializes the instance variables of an object. 
# The constructor is automatically called whenever an object is created.
#The constructor is responsible for defining and initializing all of the instance variables that are to be contained in the object.
#After the constructor completes its work, a reference to the newly created and initialized object is returned. 
#The reference is saved in a variable so we can later call methods on the object.
#The constructor is defined using the special method name 
__init__.
#Python uses the special name __init__ for the constructor because its purpose is to initialize an instance of the class:
def __init__(self) :
   self._itemCount = 0
   self._totalPrice = 0.0
   
#Python allows you to define only one constructor per class.
#But you can define a constructor with default argument that simulate multiple definitions.
#Consider, for example, a BankAccount class that needs two forms for the constructor: one that accepts an argument for the initial balance and another that uses a default initial balance of 0.
#This can be achieved by including a default argument for the initialBalance parameter variable,

class BankAccount :
   def __init__(self, initialBalance = 0.0) :
      self._balance = initialBalance

#The user of the class can choose which form to use when creating an object. If no value is passed to the constructor when a BankAccount object is created,

joesAccount = BankAccount()
# the default value will be used. If a value is passed to the constructor

joesAccount = BankAccount(499.95)
# that value will be used instead of the default one.

#Implementing Methods

# When implementing a class, you need to provide the bodies for all methods. 
# Implementing a method is very similar to implementing a function, with one essential difference: 
# You access the instance variables of the object in the method body.

#In a method, you access instance variables through the self parameter variable.
#To access an instance variable, such as _itemCount or _totalPrice, in a method, you must access the variable name through the self reference.
# This indicates that you want to access the instance variables of the object on which the method is invoked, and not those of some other CashRegister object.

#Testing a Class
# In the preceding section, we completed the implementation of the CashRegister class. What can you do with it? 
# In the long run, your class may become a part of a larger program that interacts with users, stores data in files, and so on.
# However, before integrating a class into a program, it is always a good idea to test it in isolation.
# Testing in isolation, outside a complete program, is called unit testing.

#A unit test verifies that a class works correctly in isolation, outside a complete program.


#nteractive testing is quick and convenient but it has a drawback. When you find and fix a mistake, you need to type in the tests again.

#As your classes get more complex, you should write tester programs.
#A tester program is a driver module that imports the class and contains statements to run methods of your class. 

# 1.Construct one or more objects of the class that is being tested.

# 2.Invoke one or more methods.

# 3.Print out one or more results.

# 4.Print the expected results.