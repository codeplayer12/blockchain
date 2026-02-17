Python Datatypes

- Numbers:
    - Integer: Example - 10 , -3
    - Floats: Example - 1.8, -6.973
    - Boolean: Example - True, False
    - Strings: Example - "Hi, there", 'Hi, there'
    - Dictionaries
    - Objects

- Working with variables
    - Examples of variables
    - age = 29

    - Manipulating variables
    - age = 30
    - age = age - 1
    - Storing floats
    - age = 29.5

    - Boolean variables
    - is_old = True

    - String variables
    - name = "Noble"

- Working with Numbers
 - Integer -> As big(small) as the operating system supports
 - Conversion
    - int('1') -> 1
    - int(1.9) -> 1
    - int(True) -> 1
    - int(False) -> 0

- Float
- Conversion
    - float(29) -> 29.0
    - float(True) -> 1.0
    - float(False) -> 0.0

- Float and  Integer ca be written as long numbers is easily readable: 1_000_000.0
- fans -> 1_000_000
- fans -> 1000000

## Operators
Operator    Example     Output
    +       5 + 10      10
    -       5 - 10      -5
    *       5 * 10      50
    /       5 / 10      0.5
    //      5 //10      0
    **      5 ** 10     9765625
    %       5  % 10     5


## Special Behavior when working with numbers
Example
- 1e10 -> 10000000000.o
- 1 - 0.9 -> 0.099999...8
- 1 - 0.5 -> 0.5

## Working with Strings
- name = 'Noble'
- name = "Noble"
- longer_text = """ multi
line
text """

## Working with Lists
Example
- ["some text", 12.9, True ,["nested!", 8]]
- Index in a list starts from 0
- Length is the number of items in a list example:4
- blockchain = [1,8.6,5.1]
Accessing second transaction 
 - blockchain[1]
Copying the blockchain value
 - blockchain[1] + 2 : note does not update the original value
Adding to the list
  - blockchain.append(10)
  - blockchain
Remove and return the removed value
 - blockchain.pop()
 - blockchain

 ## Theory of Blockchain
 -> chain - list of blocks with the previous values and the new values
 -> block - list of values


## Functions
- Defining a funcion
def greet():
    print('Hello')

- Calling a function executes the function
greet()


## Functions receiving arguments
def greet(name):
    print('Hello ' + name)

greet('Noble')


## Functions return values
def sum(a,b):
    return a + b

print(sum(2,5))

## Default Arguments
def greet(name,age=32):
    print('Hello ' + name + ' I am ' + age +' old.')

greet('Noble')

## Using the input function
- Allow the user to enter input
input()

## Variable Scope
- Global Scope : Example
    - name = 'Max' //accessible everywhere
      def greet():
        print('Hi, ' + name)

      greet()

- Local Scope: Example
    - name = 'Max'
      def greet():
        age = 29 // accessible only inside
        print('Hi , + name + ', I am ' + age)
    
      greet()

## Updating Global Variable in the function
    name = 'John'
    def get_name():
        global name
        name = input('Your name :)

    get_name()


## Adding comments and Docstrings
# - is used for comments
Doc strings - """ Returns the last value of the current blockchain """