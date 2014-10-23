#!/usr/bin/env python

#Phone Tool application
#Mike Lafky, 7/10/2014

from PyQt4 import QtCore
from PyQt4 import QtGui
from ui_phonetool import Ui_PhoneTool
from ui_add import Ui_Add
import sys
import operator
import shlex
import subprocess
import sqlite3
import time

class PhoneTool(QtGui.QMainWindow, Ui_PhoneTool):
	def __init__(self, parent = None):

		#location of the SQLite database to connect to
		self.dbloc = './names.db'

		#Check to see if the program is launched with arguments.
		#if so, function commandrun() will print the results to the command line
		if len(sys.argv) == 2 or len(sys.argv) == 3:
			self.commandrun()

        	super(PhoneTool, self).__init__(parent)
       		self.setupUi(self)

		#Code to connect gui objects to relevant functions
	       	QtCore.QObject.connect(self.searchField, QtCore.SIGNAL("textChanged(const QString&)"), self.searchnames)  
	       	QtCore.QObject.connect(self.searchField_2, QtCore.SIGNAL("textChanged(const QString&)"), self.searchgroups)
		QtCore.QObject.connect(self.addButton, QtCore.SIGNAL("clicked()"),self.editdb)
		QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL("cellDoubleClicked(int, int)"), self.edit)
		QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), self.closeit)
	       	
	       	#timer to kill the program after a certain amount of time has elapsed
       		self.countdown = 0
	       	self.timer = QtCore.QTimer()
	       	self.timer.timeout.connect(self.mdk)
	       	self.timer.start(1000)
	       	
	       	#Limits row count to 20 (arbitrary) and sets focus to the name search field
	       	self.tableWidget.setRowCount(20)
       		self.searchField.setFocus()  		
       
        #this function will run if the application is run with 1 or 2 arguments
        #it will search the database and print the results to the command line (or wherever)
	def commandrun(self):
		i = 0
		#connect to names database
       		db = sqlite3.connect(self.dbloc)
       		cursor = db.cursor()
       		if len(sys.argv)==2:
	       		query = '%' + str(sys.argv[1]) + '%'
		else:
			query = '%' + str(sys.argv[1]) + ' ' + str(sys.argv[2]) + '%'
       		#make the query	
		cursor.execute("SELECT * FROM names WHERE name LIKE ?", (query,))
		#grab the number of results
		numrows = len(cursor.fetchall())
		#rerun the query
		cursor.execute("SELECT * FROM names WHERE name LIKE ?", (query,))
		#arbitrarily limit the number of rows to 10 results
		maxrows = 10
		#Set up a template for how the results are displayed
		template = "{0:15}{1:10}{2:20}{3:20}{4:10}"
		#Display the results
		if numrows == 0:
			print 'Zero results found for query: "' +  query.translate(None,'%') + '"'
		elif numrows < maxrows:
			print str(numrows) + ' results found for query "' + str(query.translate(None,'%')) + '"'
			print template.format("Name:","Office:","Cell:","Home:","Pager:","Preference:")
		elif numrows > maxrows:
			print str(numrows) + ' results found for query "' + str(query.translate(None,'%')) +  '". Displaying first ' + str(maxrows) + ' results:'
			print template.format("Name:","Office:","Cell:","Home:","Pager:","Preference:")
		for row in cursor:
			i = i + 1
			if i > maxrows:
				break
			print template.format(str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]))
		db.close()
		sys.exit()
       
       	def closeit(self):
       		sys.exit()
       
       	#Function executes when cell is double clicked, then connects the cellChanged signal to the edit2 function
       	def edit(self):
       		if(self.checkBox.isChecked()):
			QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL("cellChanged(int, int)"), self.edit2)
		else:
			self.statusBar().showMessage("Click the edit box to save changes!")
	#Function executes every second, closing the program after 240 seconds
       	def mdk(self):
       	
       		self.countdown = self.countdown + 1
       		if (self.countdown > 240):
       			sys.exit()
       	
       	#Function executes when the user changes the cell value, and immediately disconnects the cell changed signal
       	def edit2(self):
       	
       		#reset countdown timer
       		self.countdown = 0
		
		QtCore.QObject.disconnect(self.tableWidget, QtCore.SIGNAL("cellChanged(int, int)"), self.edit2)       	
       		db = sqlite3.connect(self.dbloc)
       		cursor = db.cursor()
       	
       		row = int(self.tableWidget.currentRow())
       		col = int(self.tableWidget.currentColumn())
       		name = str(self.tableWidget.item(row,0).text())
		#gets the text of the currently selected cell
		try:
			text = self.tableWidget.item(self.tableWidget.currentRow(),self.tableWidget.currentColumn()).text()
		except AttributeError:
			text = ' '
		#A bunch of if statements to figure out which field is being edited to prepare the SQLite statement
		#Will only work if "checkBox" has been checked
		if (self.checkBox.isChecked() and col!= 0):
			if (int(self.tableWidget.currentColumn())!=1):
				try:
					office = str(self.tableWidget.item(self.tableWidget.currentRow(),1).text())
				except AttributeError:
					office = ' '
			elif (int(self.tableWidget.currentColumn())==1):
				office = str(text)
			if (int(self.tableWidget.currentColumn())!=2):
				try:
					cell = str(self.tableWidget.item(self.tableWidget.currentRow(),2).text())
				except AttributeError:
					cell = ' '
			elif (int(self.tableWidget.currentColumn())==2):
				cell = str(text)
			if (int(self.tableWidget.currentColumn())!=3):
				try:
					home = str(self.tableWidget.item(self.tableWidget.currentRow(),3).text())	
				except AttributeError:
					home = ' '
			elif (int(self.tableWidget.currentColumn())==3):	
				home = str(text)	
			if (int(self.tableWidget.currentColumn())!=4):
				try:
					pager = str(self.tableWidget.item(self.tableWidget.currentRow(),4).text())	
				except AttributeError:
					pager = ' '
			elif (int(self.tableWidget.currentColumn())==4):
				pager = str(text)
			if (int(self.tableWidget.currentColumn())!=5):
				try:
					pref = str(self.tableWidget.item(self.tableWidget.currentRow(),5).text())
				except AttributeError:
					pref = ' '
			elif (int(self.tableWidget.currentColumn())==5):
				pref = str(text)
			if (int(self.tableWidget.currentColumn())!=6):
				try:
					notes = str(self.tableWidget.item(self.tableWidget.currentRow(),6).text())
				except AttributeError:
					notes = ' '
			elif (int(self.tableWidget.currentColumn())==6):
				notes = str(text)
			if (int(self.tableWidget.currentColumn())!=7):
				try:
					grop = str(self.tableWidget.item(self.tableWidget.currentRow(),7).text())
				except AttributeError:
					grop = ' '
			elif (int(self.tableWidget.currentColumn())==7):
				grop = str(text)
			if (int(self.tableWidget.currentColumn())!=8):
				try:
					supervisor = str(self.tableWidget.item(self.tableWidget.currentRow(),8).text())
				except AttributeError:
					supervisor = ' '
			elif (int(self.tableWidget.currentColumn())==8):
				supervisor = str(text)
			#SQLite statement to update database
       			cursor.execute("UPDATE names SET office = ?, cell = ?, home = ?, pager = ?, pref = ?, notes = ?, grop = ?, supervisor = ? WHERE name = ?",(office, cell, home, pager, pref, notes, grop, supervisor, name))
			db.commit()
       		       	db.close()
       		       	self.statusBar().showMessage('Edits Saved!')
		else:
			self.statusBar().showMessage('Editable Text Box not checked!  Edits not saved.')
			
		if (self.checkBox.isChecked() and col == 0):
			self.statusBar().showMessage('Names can not be edited from here.  Use the Add/Delete contact button!')
       	
       	#Function to search the database via the "name" field.  Also populates the table.
       	def searchnames(self):
       	
       		#reset countdown variable
       		self.countdown = 0
       		
       		#This function connects the text in the name search field to the names 
       		#database, sorting by the "name" field in the "names" table
       		self.statusBar().clear()
       		self.searchField_2.clear()
       		self.tableWidget.clearContents()

       		#connect to names database
       		db = sqlite3.connect(self.dbloc)
       		cursor = db.cursor()
       		query = '%' + str(self.searchField.text()) + '%'
       		#make the query	
		cursor.execute("SELECT * FROM names WHERE name LIKE ?", (query,))
		i = 0;
		#populate tableWidget with data
       		for row in cursor:
			self.tableWidget.setItem(i,0,QtGui.QTableWidgetItem(str(row[0])))
			self.tableWidget.setItem(i,1,QtGui.QTableWidgetItem(str(row[1])))
			self.tableWidget.setItem(i,2,QtGui.QTableWidgetItem(str(row[2])))
			self.tableWidget.setItem(i,3,QtGui.QTableWidgetItem(str(row[3])))
			self.tableWidget.setItem(i,4,QtGui.QTableWidgetItem(str(row[4])))
			self.tableWidget.setItem(i,5,QtGui.QTableWidgetItem(str(row[5])))
			self.tableWidget.setItem(i,6,QtGui.QTableWidgetItem(str(row[6])))
			self.tableWidget.setItem(i,7,QtGui.QTableWidgetItem(str(row[7])))
			self.tableWidget.setItem(i,8,QtGui.QTableWidgetItem(str(row[8])))
			i = i + 1;
       		db.close()
       		self.tableWidget.setRowCount(i)
       	
       	#Function to search the database via the "grop" field (group is a protected name is sqlite)
       	def searchgroups(self):
       	
       		#reset countdown variable
       		self.countdown = 0
       	
       		#This function connects the text in the group search field to the names
       		#database, sorting by the "grop" field in the "names" table
       		self.searchField.clear()
       		self.tableWidget.clearContents()
       		db = sqlite3.connect(self.dbloc)
       		cursor = db.cursor()
       		query = '%' + str(self.searchField_2.text()) + '%'
       		#make the query	
		cursor.execute("SELECT * FROM names WHERE grop LIKE ?", (query,))
		i = 0;
		#populate tableWidget with data
       		for row in cursor:
			self.tableWidget.setItem(i,0,QtGui.QTableWidgetItem(str(row[0])))
			self.tableWidget.setItem(i,1,QtGui.QTableWidgetItem(str(row[1])))
			self.tableWidget.setItem(i,2,QtGui.QTableWidgetItem(str(row[2])))
			self.tableWidget.setItem(i,3,QtGui.QTableWidgetItem(str(row[3])))
			self.tableWidget.setItem(i,4,QtGui.QTableWidgetItem(str(row[4])))
			self.tableWidget.setItem(i,5,QtGui.QTableWidgetItem(str(row[5])))
			self.tableWidget.setItem(i,6,QtGui.QTableWidgetItem(str(row[6])))
			self.tableWidget.setItem(i,7,QtGui.QTableWidgetItem(str(row[7])))
			self.tableWidget.setItem(i,8,QtGui.QTableWidgetItem(str(row[8])))
			i = i + 1;
       		db.close()       		
		self.tableWidget.setRowCount(i)

	#Function to launch Add.py gui which allows adding/deleting names from the database.
	def editdb(self):
		
		#stop countdown timer when opening the Add gui for adding/deleting names from the db
		self.timer.stop()
		addDialog = AddEntry()
		addDialog.show()
		addDialog.exec_()

#This is the gui that opens when you select "Add/Update/Delete" from the main window and is the easiest way to interact with the database
class AddEntry(QtGui.QDialog,Ui_Add):
	def __init__(self, parent=None):
		super(AddEntry, self).__init__(parent)
		self.setupUi(self)
		self.name.setFocus()

		QtCore.QObject.connect(self.AddBut, QtCore.SIGNAL("clicked()"), self.add)  
		QtCore.QObject.connect(self.Update, QtCore.SIGNAL("clicked()"), self.update)  
		QtCore.QObject.connect(self.Delete, QtCore.SIGNAL("clicked()"), self.delete)
		
		#location of the SQLite database to connect to
		self.dbloc = './names.db'

	def add(self):

		#Function to add an entry to the database.
	
       		db = sqlite3.connect(self.dbloc)
       		cursor = db.cursor()
       		
		name = str(self.name.text())
		office = str(self.office.text())
		cell = str(self.cell.text())
		home = str(self.home.text())
		pager = str(self.home.text())
		pref = str(self.pref.text())
		notes = str(self.notes.text())
		grop = str(self.grop.text())
		supervisor = str(self.supervisor.text())
		#Sanity check to make sure the user entered a name to be added
		if len(name)  < 3:
			msg = """Please enter a first and last name!"""
       			QtGui.QMessageBox.about(self, "Hold on!", msg.strip())
       		else:
			cursor.execute('''INSERT INTO names
				(name,office,cell,home,pager,pref,notes,grop,supervisor) values(?,?,?,?,?,?,?,?,?)''',
				(name, office, cell, home, pager,pref, notes, grop, supervisor))
		db.commit()
		db.close()
		
	
	def update(self):

		#Function replaces information in the database for a given name

		db = sqlite3.connect(self.dbloc)
       		cursor = db.cursor()
       		
       		name = str(self.name.text())
		office = str(self.office.text())
		cell = str(self.cell.text())
		home = str(self.home.text())
		pager = str(self.home.text())
		pref = str(self.pref.text())
		notes = str(self.notes.text())
		grop = str(self.grop.text())
		supervisor = str(self.supervisor.text())
		
		cursor.execute("UPDATE names SET name = ?, office = ?, cell = ?, home = ?, pager = ?, pref = ?, notes = ?, grop = ?, supervisor = ? WHERE name = ?",(name, office, cell, home, pager, pref, notes, grop, supervisor, name))
		
		db.commit()
		db.close()
		
	
	def delete(self):

		#This function deletes an entry from the database.  It only requires the name to be deleted
		name = str(self.name.text())
		#Sanity check to make sure the user entered a name to be added
		if len(name)  < 3:
			msg = """Please enter a first and last name!"""
       			QtGui.QMessageBox.about(self, "Hold on!", msg.strip())
       		else:
	       		db = sqlite3.connect(self.dbloc)
	       		cursor = db.cursor()		
			cursor.execute("DELETE FROM names WHERE name=?", (name,))
			db.commit()
			db.close()

app = QtGui.QApplication(sys.argv)
PhoneTool = PhoneTool()
PhoneTool.show()
sys.exit(app.exec_())
