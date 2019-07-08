
import getpass,os
os.system('cls')
user_name = input('enter the user_name')
password = getpass.getpass('enter the password') #username and password for writing the Quiz         
						 #getpass method is used to hide the password entered
ans ,marks = [] , []
fans = open("ans.txt").read().split()            #ans.txt contains correct answers and it is stored like space between answers
no_que = 10
def ques():                                      #ques function is used to call the questions with options to the screen which are stored in text files
	for i in range(1 , no_que + 1):		 #no_que is the variable which stores the numbers of questions in Quiz
		os.system('cls')
		files = open(str(i)+".txt").read()
		print(files)
		x = input('enter your choice')
		ans.append(x)
def ans_Print():				#ans_print function is used to the print the Total_marks, answer_entered and correct_answer
	os.system('cls')
	print ("S.No"+"\tcorrect_Answer"+"\tanswered"+"\tmarks")
	marks = [ 2 if (fans[i] == ans[i]) else 0 for i in range(no_que) ]
	for i in range(no_que):
		print(str(i+1)+"\t"+str(fans[i])+"\t\t"+str(ans[i])+"\t\t"+str(marks[i]))
	return sum(marks)
if (user_name == "ICON") and (password == "CSE"):    #check wheather Username and Password is correct or not
						     #Here user_name = ICON and password = CSE
	os.system('cls')
	print ("welcome!")
	instructions = open("instr.txt").read()       #instr.txt is a text file which tells about the instructions to write the Quiz
	print(instructions)
	start = int(input('enter "1" to start '))   #Here Quiz starts on entering "1"
	if (start == 1):
		ques()
		ans_Print()
		print("total_Marks:"+str(ans_Print()))
	else: quit()
else: print("invaid credentials")
