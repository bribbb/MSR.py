from tkinter import *


root = Tk()

#Define OPEN function to open 2nd window 

def open():
	global dateLabeltwo
	top = Toplevel()
	top.title('My Second Window')
	
##simple  get command needs to be added




#add a continue button 
btn = Button(root, text = "Open Second Window", command = open)
btn.grid(row=11, column=4, columnspan=3, padx=10, pady=10)



#TITLE
root.title("multiple student report")

#Label Boxes labeling entry Boxes

#instructor Label 
instructorLabel = Label(root, text="Please enter Instructor Name (First/Last)")
instructorLabel.grid(row=2, column=1)

#course Label 
courseLabel = Label(root, text="Please Enter Course Name")
courseLabel.grid(row=3, column=1)

#date Label 
dateLabel = Label(root, text="Please Enter Date")
dateLabel.grid(row=5, column=1)


#Empty
emptyLabel = Label(root, text="")
emptyLabel.grid(row=7, column=1)

#Student name Label 
studentLabel = Label(root, text="Please Enter 3 Student Names (First/Last)")
studentLabel.grid(row=8, column=1)




#define entry BOX’s

#instructor name entry box

instructorEntry= Entry(root, width=35, borderwidth=5)
instructorEntry.grid(row=2, column=4, columnspan=3, padx=10, pady=10)




#course name entry box

courseEntry = Entry(root, width=35, borderwidth=5)
courseEntry.grid(row=3, column=4, columnspan=3, padx=10, pady=10)
text = courseEntry.get()


#date entry box


dateEntry = Entry(root, width=35, borderwidth=5)
dateEntry.grid(row=5, column=5, columnspan=3, padx=10, pady=10)
text = dateEntry.get()

 



#Student name entry boxes

studentnameEntryone = Entry(root, width=35, borderwidth=5)
studentnameEntryone.grid(row=8, column=4, columnspan=3, padx=10, pady=10)
text = studentnameEntryone.get()


studentnameEntrytwo = Entry(root, width=35, borderwidth=5)
studentnameEntrytwo.grid(row=9, column=4, columnspan=3, padx=10, pady=10)
text = studentnameEntrytwo.get()


studentnameEntrythree = Entry(root, width=35, borderwidth=5)
studentnameEntrythree.grid(row=10, column=4, columnspan=3, padx=10, pady=10)
text = studentnameEntrythree.get()






root.mainloop()
