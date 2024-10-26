# Advanced Python Calculator Midterm
*This assignment is an advanced command line python calculator that employs various object oreiented practices and software design principles. It manages calculation history and implements the Pandas library to load and store data in .csv files. See the tutorial below for an overview of its functionality.*

[Tutorial](https://drive.google.com/file/d/1W3pDYuGzLucVjNlUp4LCpxUnKS700SeI/view?usp=sharing)

## SOLID Principles
### Single Principle Responsiblity

In the [Caculator](https://github.com/adrianaska0/midterm/tree/main/calculator) package each module has only one responsibility. For instance `calculations.py` exclusivley handles the history of calculations, `calculation.py` handles the creation and execution of a calcualtion object, `operations.py` handles the operations, etc.

### Open/Closed Principle

The applicaton allows for new commands to be added to the system through the extension of the abstract class [Command](https://github.com/adrianaska0/midterm/blob/main/app/commands/__init__.py). 

### Liskov Substitution Principle

The superclass `Command` has subclasses with objects that replace the objects of the superclass. 

## Don't Repeat Yourself

Throughout the program, there are many instances of importing modules for use in other modlues. This way, modules can take advantage of methods that have been implemented elsewhere. Using DRY in this way also helps separeate concern so when something breaks and needs to be fixed, there is one source of truth therefore, changes are applied in one location.
![image](https://github.com/user-attachments/assets/15d0d061-d4b4-4ff8-aefc-badec66f3f2b)


## Environment Variables
Enviornment variables in this instacne were utilzed to specify the data directory for the `.csv` files. Information like this is sometimes different from machine to machine and may even be a sensitive data. That is why it is stored in the `.env` file.
![image](https://github.com/user-attachments/assets/4094238a-fff1-40f5-a901-8848c9385ab6)
![image](https://github.com/user-attachments/assets/8362689a-d6d3-43af-8fb3-8ab6da9664d2)
![image](https://github.com/user-attachments/assets/e56d2d16-f160-495c-9512-5dfe89b87da1)


## Logging

Different levels of logging are employed throughout the program. The debug level is used for more granular scope on a process and often has more messages. It is only significant when one is focusing on a specific issue (debugging). The info level is used keep note of actions as they are completed. The error level is used when something goes wrong. All are useful epseically when trying to track down actions and the times they occured in the program. These three are all used in the `LoadCsvCommand` class for the associated reasons.
![image](https://github.com/user-attachments/assets/e4922318-b798-4b2b-bc3b-c1ebcdb7d53a)

## Look Before You Leap/Easier to Ask for Forgiveness than Permission

In the `LoadCsvCommand` class we see both LBYL and EAFP being employed. I outer-most try-except block makes the assumption that the user is entering the command name followed by one argument. In the more unlikely event that is not true, the error is thrown. Also, the first conditional checks for a data path environment variable and if not sets the data path to a default. This checks the condiiton because there is a reasonable chance the path was never specified.
![image](https://github.com/user-attachments/assets/8c3ba3e6-fda1-44fe-b4da-76ebf70b5b44)
![image](https://github.com/user-attachments/assets/81652b8b-2cf7-415b-8fac-94dc9d70e88d)


## How to Use

### Arithmetic Commands 
Supported Commands
* `add`
* `subtract`
* `multiply`
* `divide`

`Usage: <operation> <operand> <operand>`
`multiply 3 10
30`

### History Management
Supported Commands 
*`show_history` Shows calculator history
*`clear_history` Clears calculator history
*`delete_calc <id>` Deletes calculation from history with associated id

*`save_csv <file_name>` Copies all calculations into a `.csv` file specified by the user
*`load csv <file_name>` Imports all calculaitions from a `.csv` file specified by the user

*`menu` Prints all available commands
*`exit` Shuts down program
