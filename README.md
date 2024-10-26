# Advanced Python Calculator Midterm
*This assignment is an advanced command line python calculator that employs various object oreiented practices and software design principles. It manages calculation history and implements the Pandas library to load and store data in .csv files. See the tutorial below for an overview of its functionality.*
(https://drive.google.com/file/d/1W3pDYuGzLucVjNlUp4LCpxUnKS700SeI/view?usp=sharing)
## SOLID Principles
### Single Principle Responsiblity

The modules in the `Caculator` package each module has only one responsible. For instance `calculations.py` exclusivley handles the history of calculations, `calculation` handles the creation and execution of a calcualtion object, `operations` handles the operations, etc.

### Open/Closed Principle

The applicaton allows for new commands to be added to the system through the extension of the abstract class `Command`. 

### Liskov Substitution Principle

The superclass `Command` has subclasses with objects that replace the objects of the superclass. 

## Don't Repeat Yourself

Throughout the program, there are many instances of importing modules for use in other modlues. This way, other modules can take advantage of methods that have been implemented elsewhere. Using DRY in this way also helps separeate concern so when something breaks and needs to be fixed, there is one source of truth and changes only have to be applied in one location.

## Environment Variables
Enviornment variables in this instacne were utilzes to specify the data directory for the `.csv` files. 

## Logging

Different levels of logging are employed throughout the program. The debug level is used for more granular scope on a process and often has more messages. It is only significant when one is focusing on a specific issue (debugging). The info level is used keep note of actions as they are completed. The error level is used when something goes wrong. All are useful epseically when trying to track down actions and the times they occured in the program. These three are all used in the `LoadCsvCommand` class for the associated reasons.

## Look Before You Leap/Easier to Ask for Forgiveness than Permission

In the `LoadCsvCommand` class we see both LBYL and EAFP being employed. I outer-most try-except block makes the assumption that the user is using the user is enter the command name followed by one  argument. In the more unlikely event that is not True, the error is thrown. Also, the first conditional checks for a data path environment variable and if not sets the data path to a default. This checks the condiiton because there is a decent chance the path was never specified.

