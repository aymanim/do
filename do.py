#!/usr/bin/python


import io
import string
import optparse
import sys
import os
import Tkinter as tk


filedb = "sample.txt"
collectiondb = "collection.txt"
# Indicators
t_short = ">"
t_long = ">>"
t_short_com = "<"
t_long_com = "<<"
t_nextaction = "+" # It will be very difficult to main consistency
t_task = "*"
t_task_com = "^"

day_weekly_review = "Saturday"




#Future expansion.... parse out Dates... NLP on tasks maybe
# So make another class for Subtasks
# Understand what they mean
# Make it do insteresting stuff

class SubTask:
	title = ""
	contexts = []
	# future feilds
	date = None

	def __init__(self, title="", context=[]):
		self.title=title
		self.contexts=[]

	def tostring(self):
		print self.title

	def getcontexts(self):
		return self.contexts;

	def gettitle(self):
		return self.title




class Task:
	""" Houses one task with project and subsequent subtasks """

	#unique ID for a key value system. 
	project = ""
	subtasks = []
	def __init__(self, project=""):
		self.project = project
		self.subtasks = []
	
	def create(self, projname="Project"):
		self.project=projname
	
	def gettasks(self):
		return self.subtasks
	def addtask(self, sub="subtask"):
		self.subtasks.append(sub)


	# def deletetask(self):

	def printtask_title(self):
		print self.project

	def tostring(self):
		# later, have an argument for 'template' to allow
		# for formatting string
		print "Project: ", self.project
		for x in self.subtasks:
			print " - ", x.gettitle()
		#for task in self.subtasks:
		#	print ") ", self.subtasks
	def printtasks_tasks(self):
		print self.gettasks()




class System:
	""" Houses the entire task management system """
	shortterm = []
	longterm = []
	contexts = []
	filedb = ""
	def __init__(self):
		shortterm = []
		longterm = []
		contexts = []
		filedb = ""

	def setfiledb(self, file):
		self.filedb = file

	def addshorterm(self, task):
		if self.shortterm is None:
			self.shortterm = [task]
		else:
			self.shortterm.append(task)
	
	def addlongterm(self, task):
		self.longterm.append(task)

	def addcontext(self, context):
		self.contexts.append(context)
	
	def printshort(self):
		for task in self.shortterm:
			task.tostring()
	def printlong(self):
		for task in self.longterm:
			task.tostring()

	def printall(self):
		print "Short term"
		self.printshort()
		print "Long term"
		self.printlong()

	def dumpto(self, file):
		ofile = open(file, 'w')

		for task in self.shortterm:
			ofile.write(t_short + task.project + "\n")
			subtasks = task.gettasks()
			for t in subtasks:
				ofile.write(t_task + t.gettitle()+"\n")
		ofile.write("\n\n")
		for task in self.longterm:
			ofile.write(t_short + task.project+"\n")
			subtasks = task.gettasks()
			for t in subtasks:
				ofile.write(t_task + t.gettitle()+"\n")

		ofile.write("\n\n")
		ofile.close()
		









# the name of the system
# then add to the style of the one
	
	




gtdsystem = System()


def process_do(system, args, line):

	# blank screen
	# remind person to get off the computer for 2 mins
	# and do this action

	# was it done? if yes, GO FORWARD with no change to SYSTEM
	# larger than 2 mins? make a project or add as todo to SYSTEM
	print "THIS WORKS"




""" 
Add this as a next action.
It may be the case that 'line' is a desired outcome
as it comes directly from the collection box. 
So, that can be a default 'project'



"""
def process_todo(system, args, line):
	# add as an individual TODO list item in SYSTEM
	# args may contain 
	print "THIS WORKS"

def process_other(system, args, line):
	# add to the system as a task and associate a person
	# persons array can retrieved and 
	# we can see who i have to hear from
	print "THIS WORKS"

def process_someday(system, args, line):
	# long term goal
	# or to do list
	# or project
	print "THIS WORKS"

def process_cal(system, args, line):
	# if i can use this with the google api
	# http://code.google.com/apis/calendar/data/2.0/developers_guide_python.html
	# IT HAS QUICK ADD API!!!
	print "THIS WORKS"

def process_useless(system, args, line):
	# Pretty my delete it and skip it
	print "THIS WORKS"

def process_ref(system, args, line):

	# Reference for my system... 
	# Independednt from other reference pools
	# maybe look at this weekly or monthly
	print "THIS WORKS"

def process_proj(system, args, line):
	# make it part of the PROJECTS LIST
	# weekly review will bring this to the surface (short term)
	# monthly review will bring up long term ones too
	print "THIS WORKS"





def process_line(line):
	print line
	

""" This method will go through collection box"""
def process_inbox(system, collectionfile):

	file = open(collectionfile)
	lines = file.readlines()
	file.close()
	# valid options for inbox items
	optionfunctions = {
				'1' : process_do,
				'd'	: process_do,
				'2' : process_todo,
				't' : process_todo,
				'3' : process_other,
				'o' : process_other,
				'4' : process_cal,
				'c' : process_cal,
				'5' : process_proj,
				'p' : process_proj,
				'6' : process_useless,
				'u' : process_useless,
				'7' : process_someday,
				's' : process_someday,
				'8' : process_ref,
				'r' : process_ref
			}


	option ="0"


	for line in lines:
		flag = False
		sline = line.strip()

		if sline != "":
			print "Did " + option + " on previous item"
			option ="0"
			try:
				while  not option[0] in optionfunctions:
					os.system("clear")
					print option + "\n\n" + sline + "\n\n"
					# begin
				
					# We can avoid another indirection by
					# making it unix style
					# basically ... % option argument
					option = raw_input(	"Actionable\n"+
										"----------\n"+
										"1 | (d)o \t: Will take TWO MINUTES do it now\n"+
										"2 | (t)odo \t: Project-less TODO item AS SOON AS I CAN\n"
										"3 | (o)ther \t: Not my responsibility, DELEGATE IT\n"+
										"4 | (c)al \t: Add to Calendar \n" +
										"5 | (p)roj \t: Make project (optional next action)\n"+
										"\n"+
										"Not Actionable\n"+
										"--------------\n"+
										"6 | (u)seless \t: Useless or Trash\n"+
										"7 | (s)omeday \t: Someday Maybe Long term\n"+
										"8 | (r)ef \t: Reference Library, read it on leisure\n\n" + 
										"Usage (option argument) : "
									)
				soption = option.strip()
				opt = soption[0]
				args = soption.split()[1:]
				optionfunctions[opt](system, args, sline)						# commit
				print args

				raw_input("You want me to to " + option + " to " + sline)
				
				
				
					
				
			except (KeyboardInterrupt, SystemExit):
				# ROLL BACK HERE
				print "\n saving current files"
				system.dumpto("test.txt")
				raise
			except:
				print "Please enter an option!"
			else:
				print "commit here"
				system.dumpto("test.txt")
				



def prepend_hyphen(arguments):
	new_args = []
	for arg in arguments:
		if arg[0] != '-':
			#arg = '-'+arg
			arg = arg
		new_args.append(arg)
	return new_args	

def option_parser_init():

	# Set the option parser
	parser = optparse.OptionParser(usage='%prog [Options]',version='%prog 0.2')
	

	### Add options here

	# formatted file
	parser.add_option('-f', '--file', default=filedb,
		type='string', help='This is the formatted task list')

	# colleciton file
	parser.add_option('-c', '--collection', default=collectiondb,
		type='string', help='Explicit collection file')


	# tutorial mode (like verbose)
	parser.add_option('-t', '--tutorial', action='store_true',
		help="Use this option to go into tutorial / verbose mode")	

	# parse collection file
	parser.add_option('-i', '--inbox', action='store_true',
		help="Go through your inbox / collection box and decide on items")


	# list task file contents
	parser.add_option("-p", "--listall", action="store_true", 
		help="List the contents of the todo list")

	


	return parser




def init(system, file):
	system = System()
	system.setfiledb(file)
	# Load file (FUTURE: take care if file does not exist)
	loaded = open(file)
	currentproj = None
	""" iterator through the task file and fill data structure"""
	for line in loaded.xreadlines():
		# short term project?
		if line[0] == t_short:
			projname = line[1:].strip()
			newtask = Task(projname)
			system.addshorterm(newtask)
			currentproj = newtask
		# long term project	
		if line[0] == t_long:
			projname = line[1:].strip()
			newtask = Task(projname)
			system.addlongterm(newtask)
			currentproj = newtask

		# task.. add it to the previous project
		if line[0] == t_task:
			title = line[1:].strip()
			subtask = SubTask(title, [])
			try :
				currentproj.addtask(subtask)
			except:
				# No projects have been added. Make this into a project
				newtask = Task(title)
				# design descision
				currentproj = newtask
				system.addshorterm(newtask)

	loaded.close()





""" Main method """
def main():

	#print '\033[92m' + "Who else" + '\033[0m'
	#print " "+ "\033[01;41m" + " " +"\033[01;46m" + " " + "\033[01;42m"
	# Options supported by this program
	

	""" Uncomment this """

	#if(len(sys.argv) == 1):
		#parser.print_help()
		#return 0

	parser = option_parser_init()

	(options, args) = parser.parse_args(prepend_hyphen(sys.argv[1:]))
	print options


	init(gtdsystem, options.file)


	# Keep track of WEEKLY REVIEWS based on DATE
	# define date above


	## Go through inbox
	if options.inbox:
		process_inbox(gtdsystem, options.collection)

	if options.listall:
		print "----------------- Current Task List: -----------------"
		gtdsystem.printall()



if __name__ == "__main__":
	main()
