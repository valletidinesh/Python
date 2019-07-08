
import getpass,os
os.system('cls')
user_name = input('enter the user_name')
password = getpass.getpass('enter the password')
ans ,marks = [] , []
fans = open("ans.txt").read().split()
no_que = 2
def ques():
	for i in range(1 , no_que + 1):
		os.system('cls')
		files = open(str(i)+".txt").read()
		print(files)
		x = input('enter your choice')
		ans.append(x)
def ans_Print():
	os.system('cls')
	print ("S.No"+"\tcorrect_Answer"+"\tanswered"+"\tmarks")
	marks = [ 2 if (fans[i] == ans[i]) else 0 for i in range(no_que) ]
	for i in range(no_que):
		print(str(i+1)+"\t"+str(fans[i])+"\t\t"+str(ans[i])+"\t\t"+str(marks[i]))
	return sum(marks)
if (user_name == "ICON") and (password == "CSE"):
	os.system('cls')
	print ("welcome!")
	instructions = open("instr.txt").read()
	print(instructions)
	start = int(input('enter "1" to start '))
	if (start == 1):
		ques()
		ans_Print()
		print("total_Marks:"+str(ans_Print()))
	else: quit()
else: print("invaid credentials")
