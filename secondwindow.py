from tkinter import *

root = Tk()

#TITLE
root.title("Final Report")

#Class nameLabel 
classLabel = Label(root, text=" CourseEntry")
classLabel.grid(row=1, column=1)
#get commands need to be added

#Empty
emptyLabel = Label(root, text="")
emptyLabel.grid(row=1, column=2)

#Semester/year Label 
semesterLabel = Label(root, text="semester/season dateEntry")
semesterLabel.grid(row=1, column=3)
##get and IF to determine season and year

#Empty
emptyLabel = Label(root, text="")
emptyLabel.grid(row=1, column=4)


#dateLabel get
getdateLabel = Label(root, text="dateEntry")
classLabel.grid(row=1, column=5)
##simple  get command needs to be added

#Empty
emptyLabel = Label(root, text="")
emptyLabel.grid(row=3, column=1, columnspan=3)

#students report name
stunameLabel1 = Label(root, text="studentLabel , Last ")
stunameLabel1.grid(row=4, column=1)
##simple  get command needs to be added

#students report name
stunameLabel2 = Label(root, text="studentLabel , Last ")
stunameLabel2.grid(row=5, column=1)
##simple  get command needs to be added

#students report name
stunameLabel3 = Label(root, text="studentLabel , Last ")
stunameLabel3.grid(row=6, column=1)
##simple  get command needs to be added




root.mainloop()
