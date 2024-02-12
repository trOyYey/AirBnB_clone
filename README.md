# 0x00. AirBnB clone - The console
## Description
The AirBnB clone project is a project to build a clone of the AirBnB website, step by step learning the real life implementation of complex Object Oriented Programming and adminstrating it's usefullness in websites such as the AirBnB website and developint the necessary skills towards building a full web application. This first step is very important and will be built upon subsequently in following projects such as: HTML/CSS templating, database storage, API, front-end integration..

Each task important task in achieving full working web, starting by:
1. Building parent Class(BaseModel) in our case
2. Build a functioning console that does basic commands ssuch as help - quit
3. Create class method for serialization and deserialization
4. Create more classes thats gonna be used (City, place, review, etc...)
5. unittest pretty much everything we have done so far

## Command Interpreter

after that we need to make our console a little bit more usefull, Doing more important commands:
1. Create new objects
2. Retrieve a stored object
3. manipulate the stored objects
4. Updating objects
5. Destroying Objects

## How to Start
First of all make sure you have python installed in your machine
To start, follow those steps below:
1. Clone the repository to your local machine:
		`git clone https://github.com/11Falcon/AirBnB_clone`
2. Navigate to AirBnB_clone Directory:
   		`cd AirBnB_clone`
3. Run the command interpreter:
   	`./console.py`

## How to Use
- once you see the prompt message , then you are set to performs different commands, and to you use any command Effeciently use help then write the command after that like in the following example
`help create`
- help command is gonna be your guide in this journy 
- keep in mind most command can be followed by input you provide,
## Examples
### Example 1:
```
create BaseModel
```
Output:
```
5ad197d0-4974-46d3-a65e-1be2f4686046
```
keep in mind that this id is generated randomly 

### Example 2:
we gonna use command `show` to print details of our Base_Model we created in previous example
```
show BaseModel 5ad197d0-4974-46d3-a65e-1be2f4686046
```
Output:
```
[BaseModel] (5ad197d0-4974-46d3-a65e-1be2f4686046) {'id': '5ad197d0-4974-46d3-a65e-1be2f4686046', 'created_at': datetime.datetime(2024, 2, 12, 0, 41, 22, 864668), 'updated_at': datetime.datetime(2024, 2, 12, 0, 41, 22, 864672)}
```
### Example 3: DESTROY !
```
destroy BaseModel 5ad197d0-4974-46d3-a65e-1be2f4686046
```

### Example 4: Bye Bye !!

once you are done and you want to quit, you can simply write `quit` , and thats it !

Rememeber there is much more to it when combining different classes and commands, and remember, `help` is always your bestfriend
