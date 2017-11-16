from tkinter import *
import tkinter as tk
import tkinter.messagebox as msg
import tkinter.colorchooser as clr

class GetPointsDialog():
    DEFAULT_COLOR = 'black'

    def __init__(self, master, Wid_type):

        self.root = tk.Tk()
        """
        THIS METHOD SHOULD CONSTRUCT THE TOPLEVEL WINDOW AND INITIATLIZE THE MAIN LOGIC FOR TAKING INPUT FROM USER FOR THE CORDINATES OF CIRCLE, RETANGLE AND LINE
        """


        self.master = master

        self.root.title("Enter Cor-dinates Points")

        self.type = Wid_type
        self.color = "#000000"

        self.Line_type = tk.IntVar(self.root)
        self.X1 = tk.StringVar(self.root)
        self.X2 = tk.StringVar(self.root)
        self.Y1 = tk.StringVar(self.root)
        self.Y2 = tk.StringVar(self.root)
        self.Rad = tk.StringVar(self.root)

        self.frm = tk.Frame(self.root, padx=12, pady=12)
        self.frm.pack()

        tk.Label(self.frm, text="X1", width=10).grid(row=0, column=0, sticky=W)
        tk.Entry(self.frm, textvariable=self.X1).grid(row=0, column=1)

        tk.Label(self.frm, text="Y1", width=10).grid(row=0, column=2, sticky=W)
        tk.Entry(self.frm, textvariable=self.Y1).grid(row=0, column=3)

        if Wid_type == "Circle":

            tk.Label(self.frm, text="Enter Radius", width=10).grid(row=1, column=0, sticky=W)
            tk.Entry(self.frm, textvariable=self.Rad).grid(row=1, column=1)

        else:

            tk.Label(self.frm, text="X2", width=10).grid(row=1, column=0)
            tk.Entry(self.frm, textvariable=self.X2).grid(row=1, column=1)

            tk.Label(self.frm, text="Y2", width=10).grid(row=1, column=2)
            tk.Entry(self.frm, textvariable=self.Y2).grid(row=1, column=3)

        self.f1 = tk.Frame(self.root, padx=10, pady=10)
        self.f1.pack()

        tk.Radiobutton(self.f1, text="Dashed", variable=self.Line_type, value=1).pack(side=tk.LEFT, anchor=tk.W)
        tk.Radiobutton(self.f1, text="Un Dashed", variable=self.Line_type, value=2).pack(side=tk.LEFT, anchor=tk.W)
        tk.Button(self.f1, text="Color", padx=20, command=self.choose_color).pack(side=tk.LEFT, anchor=tk.W)

        self.f2 = tk.Frame(self.root, padx=10, pady=10)
        self.f2.pack(fill=tk.X)

        tk.Button(self.f2, text="Submit", command=self.submit).pack(expand=1, side=tk.LEFT)
        tk.Button(self.f2, text="Reset", command=self.reset).pack(expand=1, side=tk.LEFT)

        '''
        v = IntVar()
        """
         IT SHOULD GET THE INPUT FROM USER AND SHOULD CHECK ALL THE CONDITIONS GIVEN FROM USER AND VALIDATE, ONCE VALUES ARE GOOD SEND VALUES TO MAIN CLASS ELSE RESET THE VALUES.
        """
        top = self.top = Toplevel(self.root)
        #self.l = Label(top,text="Enter Coor-dinates Points")
        top.title("Enter Coor-dinates Points")
        top.geometry("500x200")

        Label(top, text="X1").grid(row=0,column=1, sticky=W)
        e1 = Entry(top)
        e1.grid(row=0, column=2)

        Label(top, text="Y1").grid(row=0,column=3, sticky=W)
        e1 = Entry(top)
        e1.grid(row=0, column=4)

        Label(top, text="Enter Radius").grid(row=1,column=1, sticky=W)
        e1 = Entry(top)
        e1.grid(row=1, column=2)

        Radiobutton(top,text="Dashed",padx=10,variable=v,value=1,command=self).grid(row=2,column=1,sticky=W)
        Radiobutton(top,text="Un Dashed",padx=10,variable=v,value=2,command=self).grid(row=2,column=2,sticky=W)
        btn1 = Button(top,text="Color",command=self).grid(row=3,column=3)
        btn2 = Button(top,text="Submit",command=self).grid(row=4,column=2)
        btn3 = Button(top, text="Reset", command=self).grid(row=4, column=4)

'''
    def choose_color(self):
        """
        SELECT THE COLOR FROM LIST OF COLOR'S AVAILABLE AND PASS THE COLOR TO MAIN WINDOW
        """
        self.get_color = clr.askcolor()

        self.color = self.get_color[1]
    pass


    def submit(self):

        if self.type == "Circle":

            X1=self.X1.get()

            Y1=self.Y1.get()

            Rad=self.Rad.get()

            Line_type=self.Line_type.get()

            check_error = [X1.isdigit(), Y1.isdigit(), Rad.isdigit(), Line_type != 0]
            msg_error = [("Value Error", "Coefficient of X1 can't be character or a Null"),
                          ("Value Error", "Coefficient of Y1 can't be character or a Null"),
                          ("Value Error", "Coefficient of Rad can't be character or a Null"),
                          ("Error", "Please select line type")]

            if False in check_error:
                msg.showerror(msg_error[check_error.index(False)][0], msg_error[check_error.index(False)][1],parent=self.root)
                return

            self.master.Create_Circle(int(X1), int(Y1), int(Rad), Line_type, self.color)
            self.master.prev.append(["circle", (int(X1), int(Y1), int(Rad), Line_type, self.color)])

        else:

            X1 = self.X1.get()

            Y1 = self.Y1.get()

            X2 = self.X2.get()

            Y2 = self.Y2.get()

            Line_type = self.Line_type.get()
            check_error = [X1.isdigit(), Y1.isdigit(), X2.isdigit(), Y2.isdigit(), Line_type != 0]
            msg_error = [("Value Error", "Coefficient of X1 can't be character or a Null"),
                          ("Value Error", "Coefficient of Y1 can't be character or a Null"),
                          ("Value Error", "Coefficient of X2 can't be character or a Null"),
                          ("Value Error", "Coefficient of Y2 can't be character or a Null"),
                          ("Error", "Please select line type")]

            if False in check_error:
                msg.showerror(msg_error[check_error.index(False)][0], msg_error[check_error.index(False)][1],
                              parent=self.root)
                return

            check_error = [int(X2) >= int(X1), int(Y2) >= int(Y1)]
            msg_error = [("Error", "Coefficient of X2 can't be less than X1"),
                          ("Error", "Coefficient of Y2 can't be less than Y1")]

            if False in check_error:
                msg.showerror(msg_error[check_error.index(False)][0], msg_error[check_error.index(False)][1],
                              parent=self.root)
                return

            if self.type == "Line":
                self.master.Create_Line(int(X1), int(Y1), int(X2), int(Y2), Line_type, self.color)
                self.master.prev.append(["line",(int(X1), int(Y1), int(X2), int(Y2), Line_type, self.color)])
            else:
                self.master.Create_Rect(int(X1), int(Y1), int(X2), int(Y2), Line_type, self.color)
                self.master.prev.append(["rectangle",(int(X1), int(Y1), int(X2), int(Y2), Line_type, self.color)])



    def reset(self):
        """
        SHOULD RESET THE VALUES IN THE ENTRY BOXES IF THERE ARE ANY ALPHANUMERIC ERRORS
        """
        self.X1.set("")
        self.X2.set("")
        self.Y1.set("")
        self.Y2.set("")
        self.Rad.set("")
        self.Line_type.set(0)

    pass


class Painter():
    def __init__(self):
        """
        SHOULD INITIALISE ALL THE ROOT ATTRIBUTES FOR BASE WINDOW.

        CAN ADD ANY NUMBER OF ATTRIBUTES REQUIRED FOR THE PROGRAM
        """

        self.root = tk.Tk()
        self.prev = []
        #self.root.config(menu=menu_bar)

        self.paint_Menu = tk.Menu(self.root)
        self.root.config(menu=self.paint_Menu)

        self.init_widgets()


    def init_widgets(self):


        self.name = "Rajendra gurjar"
        self.id = "1037946"

        self.root.geometry("800x800")
        self.root.title("python paint")



        file_menu = tk.Menu(self.paint_Menu, tearoff=False)
        self.paint_Menu.add_cascade(label="File", menu=file_menu)

        file_menu.add_command(label="New", command=self.create_New_Canvas)
        file_menu.add_command(label="Save", command=self.save_canvas)
        file_menu.add_command(label="Redraw", command=lambda: self.redraw())
        file_menu.add_separator()

        file_menu.add_command(label="Exit", command=self.root.quit)


        file_menu1 = Menu(self.paint_Menu,tearoff=False)

        file_menu1.add_command(label="Circle", command=lambda :GetPointsDialog(self, "Circle"))
        file_menu1.add_command(label="Line", command=lambda :GetPointsDialog(self, "Line"))
        file_menu1.add_command(label="Rectangle", command=lambda :GetPointsDialog(self, "Rectangle"))
        file_menu1.add_separator()

        file_menu1.add_command(label="Clear All", command=lambda :self.clear_canvas())

        self.paint_Menu.add_cascade(label="Options", menu=file_menu1)

        file_menu2 = Menu(self.paint_Menu,tearoff=False)

        self.paint_Menu.add_cascade(label="Help", menu=file_menu2)

        file_menu2.add_command(label="About", command=self.show_help_about)

        self.enabled = True

        self.enable_menu()

        self.root.protocol("WM_DELETE_WINDOW", self.exit)

        self.frm = tk.Frame(self.root)

        self.frm.pack(side=tk.TOP, anchor=tk.W)

        self.btn1 = tk.Button(self.frm, state="disabled",text="PEN", command=lambda: self.activate_button("BRUSH"))

        self.btn2 = tk.Button(self.frm, state="disabled",text="LINE",  command=lambda: self.activate_button("LINE"))

        self.btn3 = tk.Button(self.frm, state="disabled", text="CIRCLE", command=lambda: self.activate_button("CIRCLE"))

        self.btn1.pack(side=tk.LEFT), self.btn2.pack(side=tk.LEFT), self.btn3.pack(side=tk.LEFT)

        self.root.mainloop()

    def activate_button(self, Btn_Typ):
        """
        HANDLE THE BUTTONS ADDED ON THE FRAME FOR FREE PAINT BUTTONS
        """
        self.old_x = None
        self.old_y = None
        self.object = None

        if Btn_Typ == "LINE":
            self.cnvs.bind('<B1-Motion>', self.line_click)
            self.cnvs.bind('<ButtonRelease-1>', self.button_released)
            self.todraw = "LINE"

        elif Btn_Typ == "CIRCLE":
            self.cnvs.bind('<B1-Motion>', self.Circle_Click)
            self.cnvs.bind('<ButtonRelease-1>', self.button_released)
            self.todraw = "CIRCLE"

        else:
            self.cnvs.bind('<B1-Motion>', self.Brush)
            self.cnvs.bind('<ButtonRelease-1>', self.button_released)
            self.todraw = "BRUSH"

    def create_New_Canvas(self):
        """
        CREATE A NEW CANVAS OF SIZE 600x600 TO THE MAIN FRAME
        """
        if hasattr(self, 'cnvs'):
            self.clear_canvas()
            return

        self.btn1["state"] = "normal"
        self.btn2["state"] = "normal"
        self.btn3["state"] = "normal"

        self.frm1 = tk.Frame(self.root)

        self.frm1.pack(side=tk.BOTTOM, anchor=tk.SE)

        self.cnvs = tk.Canvas(self.frm1, width=600, height=600, bg='white')

        self.cnvs.pack()

        self.enable_menu()


    def Brush(self, event):
        """
        CAN USE THE BELOW GIVEN CODE FOR BRUSH OR CAN MODIFY ACCORDING TO YOUR INITIASED ATTRIBUTES.
        """
        if self.old_x and self.old_y:


            self.cnvs.create_line(self.old_x, self.old_y, event.x, event.y, width=2,
                      capstyle=tk.BUTT, fill='black', splinesteps=50)
            self.old_x = event.x
            self.old_y = event.y
    pass


    def redraw(self):
        """
        SHOULD ABLE TO SAVE ALL THE PREVIOUS CO-ORDINATE VALUES FOR OVAL(CIRCLE), LINE
        """
        for prev in self.prev:
            if prev[0] == "circle":
                self.Create_Circle(*prev[1])
            elif prev[0] == "line":
                self.Create_Line(*prev[1])
            else:
                self.Create_Rect(*prev[1])

    pass

    def button_released(self, event):
        """
        WHEN THE MOUSE BUTTON IS RELEASED SHOULD RESET THE CO-ORDINATES OF THE PREVIOUS BINDED VALUES.
        """
        x, y = event.x, event.y

        if  self.todraw == 'LINE':
            self.object = self.cnvs.create_line((x, y, x, y))
            self.old_x, self.old_y = x,y

        elif self.todraw == 'CIRCLE':
            self.object = self.cnvs.create_oval((x, y, x, y))
            self.old_x, self.old_y = x,y


        else:
            self.object = self.cnvs.create_line((x, y, x, y))
            self.old_x, self.old_y = x,y

    def line_click(self, event):
        """
        SHOULD ABLE TO HANDLE THE MOUSE CLICK EVENT AND PASS CO-ORDINATES TO THE CREATE_LINE EVENT FOR THE CANVASE AND PASS THE FILL COLOR AND SET WIDTH PROPERTIES AND SHOULD ABLE TO CLEAR THE PREVIOUS VALUES
        """
        if self.object is None: return
        x, y = self.old_x, self.old_y
        self.cnvs.coords(self.object, (x, y, event.x, event.y))



    pass


    def Circle_Click(self, event):
        """
        SAME AS THE LINE-CLICK METHOD BUT SHOULD CREATE A OVAL HERE
        """
        if self.object == None:
            return
        x, y = self.old_x, self.old_y
        self.cnvs.coords(self.object, (x, y, event.x, event.y))
        pass

    pass

    def enable_menu(self):
        """
        THIS METHOD SHOULD BE ABLE TO HANDLE THE MENUBAR STATUS AND CONFIGURE TO NORMAL STATUS WHEN NEW BUTTON IS SELECTED

        """

        if self.enabled:

            self.enabled = False
            self.paint_Menu.entryconfigure("Options", state=tk.DISABLED)
        else:
            enabled = True
            self.paint_Menu.entryconfigure(2, state="normal")

    def Get_Cordinate_Points(self, wid_typ):
        GetPointsDialog(self.root, wid_typ)

        """
        CALL THE TOPLEVEL WINDOW FROM THIS METHOD, SHOULD GET THE CO-ORDINATES AND COLOR AND STRIKE/UNSTRIKE PROPERTIES AND DECIDE TO CALL THE Create_Circle OR Create_OR Create_Rect Line METHODS
        """
    pass


    def Create_Circle(self, x1, y1, rad, Da_or_UDa, Colo):
        """
        CREATE CIRCLE ON THE CANVAS WITH THE CORDINATES AND VALUES RECEIVED FROM THE USER INPUT
        """

        if Da_or_UDa ==2:
            dash = None

            self.cnvs.create_oval(x1 - rad, y1 - rad, x1 + rad, y1 + rad, dash=dash, outline=Colo)

        else:
            dash = (2,4)

            self.cnvs.create_oval(x1 - rad, y1 - rad, x1 + rad, y1 + rad, dash=dash, outline=Colo)

    pass


    def Create_Line(self, x1, y1, x2, y2, Da_or_UDa, Colo):
        """
        CREATE LINE ON THE CANVAS WITH THE CORDINATES AND VALUES RECEIVED FROM THE USER INPUT
        """

        if Da_or_UDa == 2:
            dash=None
            self.cnvs.create_line(x1, y1, x2, y2, dash=dash, fill=Colo)
        else:
            dash = (2,4)
            self.cnvs.create_line(x1, y1, x2, y2, dash=dash, fill=Colo)

    pass


    def Create_Rect(self, x1, y1, x2, y2, Da_or_UDa, Colo):
        """
        CREATE RECTANGE ON THE CANVAS WITH THE CORDINATES AND VALUES RECEIVED FROM THE USER INPUT
        """

        dash = None if Da_or_UDa == 2 else (2, 2)
        self.cnvs.create_rectangle(x1, y1, x2, y2, dash=dash, outline=Colo)

    pass


    def clear_canvas(self):
        '''
        triggered when the menu command 'Clear' is clicked
        delete everything from the canvas and set the coefficients to 0's
        '''
        self.cnvs.delete("all")


    pass


    def save_canvas(self):
        '''
        triggered when the menu command 'Save plot as .PS' is clicked
        save the graph as '{your_student_id_number}.ps'
        '''
        self.cnvs.postscript(file="RAJENDRA_GURJAR_1037946.ps")


    pass


    def show_help_about(self):
        '''
        triggered when the menu command 'About' is clicked
        Show an information dialog displaying your name on one line and id number on the second
        '''
        msg.showinfo("About PY Paint", "Created by: %s\nID: %s" % (self.name, self.id))

        pass


    def exit(self):
        '''
        triggered when the menu command 'Exit' is clicked
        Ask if the user is sure about exiting the application and if the answer is yes then quit the main window
        '''

        if msg.askokcancel("Exit", "Are you sure?"):
            self.root.destroy()


        pass


p = Painter()
