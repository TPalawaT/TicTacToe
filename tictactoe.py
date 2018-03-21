import time #to halt the output for a few seconds
#from IPython.display import clear_output

def list_in():     #For input of variable
	global row1,row2,row3,turn
	if turn==1:
		pos=int(input("Enter your choice for player 1 (X)\n"))
	if turn==2:
		pos=int(input("Enter your choice for player 2 (O)\n"))
	
	if 1<=pos<=3:			#For row 1
		if row1[pos-1]=='X' or row1[pos-1]=='O':   #to make sure position is not already filled
			print('Position already filled, choose again')
			#time.sleep(5)
		if turn==1:
			row1[pos-1]='X'
			turn=2
		elif turn==2:
			row1[pos-1]='O'
			turn=1

	if 4<=pos<=6:			#For row 1
		if row2[pos-4]=='X' or row2[pos-4]=='O':   #to make sure position is not already filled
			print('Position already filled, choose again')
			#time.sleep(5)
		if turn==1:
			row2[pos-4]='X'
			turn=2
		elif turn==2:
			row2[pos-4]='O'
			turn=1

	if 7<=pos<=9:			#For row 1
		if row3[pos-7]=='X' or row3[pos-7]=='O':   #to make sure position is not already filled
			print('Position already filled, choose again')
			time.sleep(5)	
		if turn==1:
			row3[pos-7]='X'
			turn=2
		elif turn==2:
			row3[pos-7]='O'
			turn=1

def list_out(): #To show the output
	#clear_output()
	print(row1)
	print(row2)
	print(row3)

def list_check():
	global result
	if (row1[0]=='X' and row1[1]=='X' and row1[2]=='X') or (row1[0]=='X' and row2[0]=='X' and row3[0]=='X') or (row1[0]=='X' and row2[1]=='X' and row3[2]=='X') or (row1[1]=='X' and row2[1]=='X' and row3[1]=='X') or (row1[2]=='X' and row2[1]=='X' and row3[0]=='X') or (row1[2]=='X' and row2[2]=='X' and row3[2]=='X') or (row2[0]=='X' and row2[1]=='X' and row2[2]=='X') or (row3[0]=='X' and row3[1]=='X' and row3[2]=='X') :
		print('Player 1 wins')
		con='no'
		result='p1'
	elif (row1[0]=='O' and row1[1]=='O' and row1[2]=='O') or (row1[0]=='O' and row2[0]=='O' and row3[0]=='O') or (row1[0]=='O' and row2[1]=='O' and row3[2]=='O') or (row1[1]=='O' and row2[1]=='O' and row3[1]=='O') or (row1[2]=='O' and row2[1]=='O' and row3[0]=='O') or (row1[2]=='O' and row2[2]=='O' and row3[2]=='O') or (row2[0]=='O' and row2[1]=='O' and row2[2]=='O') or (row3[0]=='O' and row3[1]=='O' and row3[2]=='O') :
		print('Player 2 wins')
		con='no'
		result='p2'
	elif row1[0]!=1 and row1[1]!=2 and row1[2]!=3 and row2[0]!=4 and row2[0]!=5 and row2[2]!=6 and row3[0]!=7 and row3[1]!=8 and row3[2]!=9 :
		print('Game over. DRAW!')
		con='no'
		result='d'

turn=1
global row1,row2,row3
row1=[1,2,3]
row2=[4,5,6]
row3=[7,8,9]
global con
con='yes'
result='x'
list_out()
while con=='yes' :
	list_in()
	list_out()
	list_check()
	if result=='d' or result=='p1' or result=='p2' :
		con=input('Wanna play again(yes/no)\n')
		if con=='yes':
			row1=[1,2,3]
			row2=[4,5,6]
			row3=[7,8,9]
			list_out()
			result='x'