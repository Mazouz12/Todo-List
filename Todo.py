from pyfiglet import figlet_format
__author__ = 'Mazouz'
instructions = " \n  list ==> show your todos \n\n  add ==> add a todo \n\n  remove ==> delete a particular todo\n\n  clear ==> remove all todos\n\n  help ==> show instructions\n\n  quit ==> exit the program\n"
print(figlet_format("Todo-List"))
#############################################################################
# A helpful function
#############################################################################
def toString(newlist):
	result = ''
	for todo in newlist:
		result += todo 
	return result
#############################################################################
#############################################################################
command = ''
while True:
	command = input(" ==> ")
	if command == 'list':
		with open('todos.db') as f:
			f.seek(0)
			todos = f.readlines()
			for x in range(len(todos)):
				if len(todos) > 0:
					print(f"  {x}) {todos[x]}")
#############################################################################
#############################################################################
	elif command == 'add':
		todo = input('  What do you wanna do: ')
		if todo != '' :
			with open('todos.db' , 'a') as f:
				f.write(todo + '\n')
				print('Done type "list" to check your todos')
		else : 
			print('Write something !!')
#############################################################################
#############################################################################
	elif command == 'remove':
		idx = input('  Which one(Number): ')
		if idx != '':
			todos.pop(int(idx))
			with open('todos.db' , 'w') as f:
				f.write(toString(todos))
				print('Done type "list" to check your todos')
		else : 
			print('Write something valid !!')
#############################################################################
#############################################################################
	elif command == 'clear':
		todos = []
		with open('todos.db' , 'w') as f:
				f.write('')
				print('You are done ? good for you :)')
#############################################################################
#############################################################################
	elif command == 'help':
		print(instructions)
#############################################################################
#############################################################################
	elif command == 'quit':
		break
#############################################################################
#############################################################################
	else :
		if command == '':
			print('Type something !!')
		elif command[0] == 'h' and command != "help":
			print(' Did you mean "help" ?')
		elif command[0] == 'a' and command != "add":
			print(' Did you mean "add" ?')
		elif command[0] == 'c' and command != "clear":
			print(' Did you mean "clear" ?')
		elif command[0] == 'r' and command != "remove":
			print(' Did you mean "remove" ?')
		elif command[0] == 'l' and command != "list":
			print(' Did you mean "list" ?')
		elif command[0] == 'q' and command != "quit":
			print(' Did you mean "quit" ?')
		else :
			print(f' "{command}" is not a valid command type "help" to know more')


















