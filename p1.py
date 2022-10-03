from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from PIL import ImageTk,Image
import requests ,json
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
global quote
global city
global temp
from sqlite3 import *

def f1():
	add_window.deiconify()
	main_window.withdraw()
def f2():
	main_window.deiconify()
	add_window.withdraw()
def f4():
	main_window.deiconify()
	view_window.withdraw()
def f5():
	main_window.deiconify()
	update_window.withdraw()
def f6():
	update_window.deiconify()
	main_window.withdraw()
	
def f7():
	delete_window.deiconify()
	main_window.withdraw()
def f8():
	main_window.deiconify()
	delete_window.withdraw()
def f9():
	if (add_window_ent_rno.get() == "" or add_window_ent_name.get() == "" or add_window_ent_marks.get() == ""):
		showerror("OOPS!", "Please fill all the details")
	elif (add_window_ent_rno.get().isdigit() == False):
		showerror("OOPS!", "Roll number can have integers only")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif (int(add_window_ent_rno.get()) <= 0) :
		showerror("OOPS!", "Roll number can't be negative")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif (len(add_window_ent_name.get()) < 2):
		showerror("OOPS!", "Name can't consist of only one alphabet")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif ((((add_window_ent_name.get()).replace(" ","")).isalpha()) == False):
		showerror("OOPS!", "Name can't consist of digits")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif (add_window_ent_marks.get().isdigit() == False):
		showerror("OOPS!", "Marks can be integers only")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif int(add_window_ent_marks.get()) < 0:
		showerror("OOPS!", "Marks can't be negative")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif int(add_window_ent_marks.get()) > 100:
		showerror("OOPS!", "Marks can't be greater than 100")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	else:
		con = None
		try:
			con = connect("sms.db")
			cursor = con.cursor()
			sql = "insert into student values('%d', '%s','%d')"
			rno = int(add_window_ent_rno.get())
			name = add_window_ent_name.get()
			marks = int(add_window_ent_marks.get())
			cursor.execute(sql % (rno, name, marks))
			con.commit()
			showinfo("success", "record added")
			add_window_ent_rno.delete(0,"end")
			add_window_ent_name.delete(0,"end")
			add_window_ent_marks.delete(0,"end")
		except Exception as e:
			showerror("Issue", e)
			con.rollback()
		finally:
			if con is not None:
				con.close()
#--------------------------------------------------------------------------------------------------------------------------------
 
def f10():
	view_window.deiconify()
	main_window.withdraw()
	info = ""
	view_window_st_data.delete(1.0, END)
	try:
		con = connect("sms.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)	
		data = cursor.fetchall()
		if data == []:
			showinfo("Message", "No record available")
			if con is not None:
				con.close()
			view_window.withdraw()
			main_window.deiconify()
		else:
			for d in data:
				info = info + "R_no = " + str(d[0]) + ", Name = " + str(d[1]) + ", Marks = " + str(d[2]) + "\n\n"
			view_window_st_data.insert(INSERT, info)
	except Exception as e:
		showerror("issue", e)
	finally:
		if con is not None:
			con.close()

#--------------------------------------------------------------------------------------------------------------------------------

def f11():
	if (update_window_ent_rno.get() == "" or update_window_ent_name.get() == "" or update_window_ent_marks.get() == ""):
		showerror("OOPS!", "Please fill all the details")
	elif (update_window_enter_rno.get().isdigit() == False):
		showerror("OOPS!", "Roll number can have integers only")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif int(update_window_ent_rno.get()) <= 0 :
		showerror("OOPS!", "Roll number can't be negative")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif (len(update_window_ent_name.get()) < 2):
		showerror("OOPS!", "Name can't consist of only one alphabet")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif ((((update_window_ent_name.get()).replace(" ","")).isalpha()) == False):
		showerror("OOPS!", "Name can't consist of digits")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif (update_window_ent_marks.get().isdigit() == False):
		showerror("OOPS!", "Marks can be integers only")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif int(update_window_ent_marks.get()) < 0:
		showerror("OOPS!", "Marks can't be negative")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif int(update_window_ent_marks.get()) > 100:
		showerror("OOPS!", "Marks can't be greater than 100")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	else:
		con=None
		try:
			rno = int(update_window_ent_rno.get())
			name = update_window_ent_name.get()
			marks = int(update_window_ent_marks.get())
			con = connect("sms.db")
			cursor = con.cursor()
			sql = "update student set name = '%s', marks = '%d' where rno = '%d'"
			cursor.execute(sql % (name,marks,rno))
			if cursor.rowcount>0:
				con.commit()
				showinfo("Success","Details updated Successfully")
				update_window_ent_rno.delete(0,END)
				update_window_ent_name.delete(0,END)
				update_window_ent_marks.delete(0,END)
			else:
				showwarning("OOPS !!","Roll no does not exist")
				update_window_ent_rno.delete(0,END)
				update_window_ent_name.delete(0,END)
				update_window_ent_marks.delete(0,END)
		except Exception as e:
			showerror("Issue",e)
			con.rollback()
		finally:
			if con is not None:
				con.close()

#--------------------------------------------------------------------------------------------------------------------------------

def f12():
	con=None
	try:
		con = connect("sms.db")
		cursor = con.cursor()
		rno = int(delete_window_ent_rno.get())
		sql = "delete from student where rno = '%d' "
		cursor.execute(sql % (rno))
		if cursor.rowcount > 0:
			con.commit()
			showinfo("Success", "Student deleted successfully :)")
			delete_window_ent_rno.delete(0, END)
		else:
			showerror("Failure", "Student does not exist")
			delete_window_ent_rno.delete(0, END)
	except Exception as e:
		showerror("OOPS!", e)
		delete_window_ent_rno.delete(0, END)
	finally:
		if con is not None:
			con.close()
#--------------------------------------------------------------------------------------------------------------------------------


def f13():
	list_marks = []
	list_names = []	
	con=None
	try:
		con=connect('sms.db')
		cursor=con.cursor()
		sql="select marks from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		# print(data)
		for d in data:	
			list_marks.append(int(str(d[0])))
			#print(list_marks)
	except Exception as e:
		showerror("OOPS!", e)
	finally:
		if con is not None:
			con.close()

	con=None
	try:
		con=connect('sms.db')
		cursor=con.cursor()
		sql="select name from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		#print(data)
		for d in data:	
			list_names.append(str(d[0]))
		#print(list_names)
	except Exception as e:
		showerror("OOPS!", e)
	finally:
		if con is not None:
			con.close()


	plt.bar(list_names, list_marks, width = 0.6, color = ['red', 'green', 'cyan', 'orange'])
	plt.title("Batch Information!")
	plt.xlabel("Students")
	plt.ylabel("Marks")

	plt.show()

#--------------------------------------------------------------------------------------------------------------------------------

splash = Tk()
splash.after(4000, splash.destroy)
splash.wm_attributes('-fullscreen', 'true')

msg = Label(splash, text = "Student\n" + "Management\n" + "System\n" + "by\nSaurav Wagh", height = 6, bg = 'snow', font = ('Calibri', 80, 'bold'), fg = 'blue2')
msg.pack()

splash.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------

# main window design
main_window = Tk()
main_window.title("Student information system")
main_window.geometry("500x600+400+25")
main_window.iconbitmap("st.ico")
main_window.configure(bg="lightGreen")
f = ("Helvetica", 20, "bold")
try:
	web_address = "https://ipinfo.io/"
	response = requests.get(web_address)
	print(response)

	data = response.json()

	city = data['city']
	print(city)
except Exception as e:
	showerror("issue", e)
try:
	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q=pune"
	a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
	wa = a1 + a2 + a3

	res = requests.get(wa)
	print(res)

	data = res.json()
	temp = data['main']['temp']
	print(temp)
except Exception as e:
	print("issue",e)

# wa = 
res = requests.get("http://api.quotable.io/random").json()
print(res)

# data = BeautifulSoup(res.text, "html.parser")
# print(data)

# for post in data.findAll():
# 	links = post.find(a)[href]
# 	print(links)
# info = data.find('img', {"class":"p-qotd"})
# print(info)

# quote = info['alt']
quote = res["content"]
print("aj ka shubh vichar", quote)

add_btn = Button( main_window,bd = 5, text="Add", font = f, width=10,  command=f1)
view_btn = Button(main_window,bd=5,font=f,text="View",width=10, command=f10)
update_btn = Button(main_window,bd = 5, text="Update", font = f, width=10, command=f6)
delete_btn = Button(main_window,bd = 5, text="Delete", font = f, width=10, command=f7)
charts_btn = Button(main_window,bd = 5, text="Charts", font = f, width=10, command=f13)
main_window_lbl_qotd = Label(main_window, text="QOTD: "+str(quote), bg="lightGreen", font=('helvetica',18,'bold'), wraplength=500, fg="dark blue")
main_window_lbl_location = Label(main_window, text="Location: "+city, bg="lightGreen", font=f)
main_window_lbl_temp = Label(main_window, text="Temperature: "+str(temp)+ "\u00B0" + "C", bg="lightGreen", font=f)

add_btn.pack(pady = 10)
view_btn.pack(pady = 10)
update_btn.pack(pady = 10)
delete_btn.pack(pady = 10)
charts_btn.pack(pady = 10 )
main_window_lbl_qotd.place(x=5, y=500)
main_window_lbl_location.place(x=5, y=450)
main_window_lbl_temp.place( x=5, y=400)

#--------------------------------------------------------------------------------------------------------------------------------

# add window ka design
add_window = Toplevel(main_window)
add_window.title("Add Student")
add_window.configure(bg="lightBlue")
add_window.geometry("500x500+400+100")
add_window.iconbitmap("st.ico")
add_window_lbl_rno = Label(add_window, text="enter rno",bg="lightBlue", font=f)
add_window_ent_rno = Entry(add_window, bd=5, font=f)
add_window_lbl_name = Label(add_window, text="enter name",bg="lightBlue", font=f)
add_window_ent_name = Entry(add_window, bd=5, font=f)
add_window_lbl_marks = Label(add_window, text="Enter Marks",bg="lightBlue", font=f)
add_window_ent_marks = Entry(add_window, bd=5, font=f)
add_window_btn_save = Button(add_window, text="Save", font=f, command=f9)
add_window_btn_back = Button(add_window, text="Back", font=f, command=f2)
add_window_lbl_rno.pack(pady=10)
add_window_ent_rno.pack(pady=10)
add_window_lbl_name.pack(pady=10)
add_window_ent_name.pack(pady=10)
add_window_lbl_marks.pack(pady=10)
add_window_ent_marks.pack(pady=10)
add_window_btn_save.pack(pady=10)
add_window_btn_back.pack(pady=10)
add_window.withdraw()

#--------------------------------------------------------------------------------------------------------------------------------

#view window ka design
view_window = Toplevel(main_window)
view_window.title("View Student")
view_window.geometry("500x500+400+100")
view_window.iconbitmap("st.ico")
view_window.configure(bg="#fed8b1")
view_window_st_data = ScrolledText(view_window, width=30, height=10, font=('helvetiva',18,'bold'))
view_window_btn_back = Button(view_window, text="Back", font=f, command=f4)
view_window_st_data.pack(pady=10)
view_window_btn_back.pack(pady=10)
view_window.withdraw()

#--------------------------------------------------------------------------------------------------------------------------------

# update window ka design
update_window = Toplevel(main_window)
update_window.title("Update Student")
update_window.configure(bg="#FFFF66")
update_window.iconbitmap("st.ico")
update_window.geometry("500x500+400+100")
update_window_lbl_rno = Label(update_window, text="enter rno",bg="#FFFF66", font=f)
update_window_ent_rno = Entry(update_window, bd=5, font=f)
update_window_lbl_name = Label(update_window, text="enter name",bg="#FFFF66", font=f)
update_window_ent_name = Entry(update_window, bd=5, font=f)
update_window_lbl_marks = Label(update_window, text="Enter Marks",bg="#FFFF66", font=f)
update_window_ent_marks = Entry(update_window, bd=5, font=f)
update_window_btn_save = Button(update_window, text="Save", font=f, command=f11)
update_window_btn_back = Button(update_window, text="Back", font=f, command=f5)
update_window_lbl_rno.pack(pady=10)
update_window_ent_rno.pack(pady=10)
update_window_lbl_name.pack(pady=10)
update_window_ent_name.pack(pady=10)
update_window_lbl_marks.pack(pady=10)
update_window_ent_marks.pack(pady=10)
update_window_btn_save.pack(pady=10)
update_window_btn_back.pack(pady=10)
update_window.withdraw()

#--------------------------------------------------------------------------------------------------------------------------------

# delete window ka design
delete_window = Toplevel(main_window)
delete_window.title("Delete Student")
delete_window.configure(bg="#87CEEB")
delete_window.iconbitmap("st.ico")
delete_window.geometry("500x500+400+100")
delete_window_lbl_rno = Label(delete_window, text="Enter rno",bg="#87CEEB", font=f)
delete_window_ent_rno = Entry(delete_window, bd=5, font=f)
delete_window_btn_save = Button(delete_window, text="Save", font=f, command=f12)
delete_window_btn_back = Button(delete_window, text="Back", font=f, command=f8)
delete_window_lbl_rno.pack(pady=10)
delete_window_ent_rno.pack(pady=10)
delete_window_btn_save.pack(pady=10)
delete_window_btn_back.pack(pady=10)
delete_window.withdraw()
#--------------------------------------------------------------------------------------------------------------------------------
def quit():
	if askokcancel("Quit", "Do you want to quit?"):
		main_window.destroy()	


main_window.protocol("WM_DELETE_WINDOW", quit)
#--------------------------------------------------------------------------------------------------------------------------------
 
main_window.mainloop()
