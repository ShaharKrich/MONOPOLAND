from tkinter import *
import sqlite3
import PIL
import UserDATA
import con_and_var
from con_and_var import *

#root setup
root = Tk()
root.title('MONOPOLAND')
#importing all pics and such
logo = PhotoImage(file=con_and_var.LOGO)


#screen
x = root.winfo_screenwidth()
y = root.winfo_screenheight()
root.geometry("%dx%d" % (x, y)) #set the screen size to x and Y of the screen
canvas = Canvas(root , height = y ,width =x,bg='light blue')
canvas.pack()
users = UserDATA.Users()
#קלטים בעת ההתחברות וההרשמה
PASS_INPUT = Entry(root) # entry is  an object that gets input from the user
REPASS_INPUT = Entry(root) # entry is  an object that gets input from the user
USERNAME_INPUT = Entry(root)
EMAIL_INPUT = Entry(root) # entry is  an object that gets input from the user

def start_page():
    canvas.delete("all")
    canvas.create_image(200, 50, image=logo)
    START = Button(root, text='START', bd='5', padx=5, pady=7, command = home_page)
    START.pack()
    EXIT = Button(root, text='Jerome', bd='5', padx=5, pady=7, command = root.destroy)
    EXIT.pack()
    #place on the canvas
    canvas.create_text(x/2, 100, text="WELCOME TO MONOPOLAND, DONT GO BANKRUPT", font='Times 20 italic bold')
    canvas.create_window(x/2, y/2, window=START)#button location
    canvas.create_window(x/2, y/2+70, window=EXIT)#button location


def home_page():
    canvas.delete('all')
    canvas.create_image(200, 50, image=logo)
    LOGIN = Button(root, text='Login', bd='5', padx=5, pady=7, command=login_page)
    LOGIN.pack()
    REGISTER = Button(root, text='Register', bd='5', padx=5, pady=7, command=registration)
    REGISTER.pack()
    RULES = Button(root, text='Rules', bd='5', padx=5, pady=7,command=rule_page)
    RULES.pack()
    ABOUT = Button(root, text='ABOUT', bd='5', padx=5, pady=7)
    ABOUT.pack()
    BACK = Button(root, text='Back', bd='5', padx=5, pady=7, command = start_page)
    BACK.pack()

    canvas.create_window(x/2, y/2, window=LOGIN)#button location
    canvas.create_window(x/2, y/2+70, window=REGISTER)#button location
    canvas.create_window(x/2, y/2+140, window=RULES)#button location
    canvas.create_window(x/2, y/2+210, window=ABOUT)#button location
    canvas.create_window( 40,y-50, window = BACK)


def login_page():
    canvas.delete('all')
    canvas.create_image(200, 50, image=logo)

    PASSWORD_INPUT = Entry(root) # entry is  an object that gets input from the user
    PASSWORD_INPUT.pack()
    USERNAME_INPUT = Entry(root)
    USERNAME_INPUT.pack()
    LOGIN = Button(root, text='Login', bd='5', padx=5, pady=7,command = welcome_page)
    LOGIN.pack()
    RESET_PASS = Button(root, text='I forgot my password', bd='5', padx=5, pady=7,command = reset_password)
    RESET_PASS.pack()
    RULES = Button(root, text='Rules', bd='5', padx=5, pady=7, command=rule_page)
    RULES.pack()
    HOME = Button(root, text='HOME', bd='5', padx=5, pady=7, command=home_page)
    HOME.pack()

    canvas.create_text(x/2, y-800, text="Login", font=('Helvetica', 50), fill="black")
    canvas.create_text(x / 2-100, y / 2, text="password:",  font=("Helvetica", 12), fill="black")  # button location
    canvas.create_text(x / 2-100, y / 2+70, text="username:",  font=("Helvetica", 12), fill="black")  # button location
    canvas.create_window(x / 2, y / 2, window=PASSWORD_INPUT)#button location
    canvas.create_window(x/2, y/2+70, window=USERNAME_INPUT)#button location
    canvas.create_window(x/2, y/2+140, window=LOGIN)#button location
    canvas.create_window(x/2, y/2+210, window=HOME)#button location
    canvas.create_window(x / 2, y / 2+280, window=RESET_PASS)#button location


def rule_page():
    canvas.delete('all')
    canvas.create_image(200, 50, image=logo)
    TEXT_PASSAGE = Label(text="""In the game of MONOPOLAND the task of each player is to acquire as much wealth as possible, and to go bankrupt last.
                        The way to achieve that is through buying, renting and selling of property.In each turn, you roll the dice to move the number of blocks, 
                        but there is a risk, if you throw 3 doubles in a row, you will be sent to jail and unable to play for 3 turns.
                        Each time you go through the starting block you will be awarded with 200 dollars to use""", bg = "light blue")
    HOME = Button(root, text='HOME', bd='5', padx=5, pady=7,command=home_page)
    HOME.pack()
    canvas.create_window(x / 2, y / 2 + 100, window=HOME)
    canvas.create_window(x / 2, y / 2, window=TEXT_PASSAGE)  # button location

def reset_password():
    canvas.delete('all')
    canvas.create_image(200, 50, image=logo)
    PASSWORD = Label(text="padsgsdg:", padx=8, pady=9, font=(25),bg ="light blue")
    REPASSWORD = Label(text="confirm password:", padx=8, pady=9, font=(25), bg="light blue")
    EMAIL_INPUT = Entry(root) # entry is  an object that gets input from the user
    EMAIL_INPUT.pack()
    PASS_INPUT = Entry(root) # entry is  an object that gets input from the user
    PASS_INPUT.pack()
    REPASSWORD_INPUT = Entry(root)
    REPASSWORD_INPUT.pack()
    LOGIN = Button(root, text='Login', bd='5', padx=5, pady=7)
    LOGIN.pack()
    RESET_PASS = Button(root, text='I forgot my password', bd='5', padx=5, pady=7)
    RESET_PASS.pack()
    RULES = Button(root, text='Rules', bd='5', padx=5, pady=7, command=rule_page)
    RULES.pack()
    HOME = Button(root, text='HOME', bd='5', padx=5, pady=7,command=home_page)
    HOME.pack()

    canvas.create_text(x / 2 - 90, y / 2-70, text="Email:", font=(25), fill ="black")  # button location
    canvas.create_text(x / 2-100, y / 2, text="password:", font=(25),bg ="light blue")#button location
    canvas.create_text(x / 2-130, y / 2+70, text="confirm password:", padx=8, pady=9, font=(25), bg="light blue")#button location
    canvas.create_window(x / 2, y / 2 -70, window=EMAIL_INPUT)  # button location
    canvas.create_window(x / 2, y / 2, window=PASS_INPUT)#button location
    canvas.create_window(x/2, y/2+70, window=REPASSWORD_INPUT)#button location
    canvas.create_window(x/2, y/2+140, window=LOGIN)#button location
    canvas.create_window(x/2, y/2+210, window=HOME)#button location

def registration():
    global PASS_INPUT, EMAIL_INPUT, USERNAME_INPUT, REPASS_INPUT
    canvas.delete('all')
    canvas.create_image(200, 50, image=logo)
    TITLE = Label(text="Register", font=('comic sans',50),bg ="light blue")
    PASSWORD = Label(text="password:", padx=8, pady=9, font=(25), bg ="light blue")
    REPASSWORD = Label(text="confirm password:", padx=8, pady=9, font=(25), bg ="light blue")
    USERNAME = Label(text="username:", padx=8, pady=9, font=(25), bg="light blue")
    EMAIL = Label(text="Email:", padx=8, pady=9, font=(25), bg="light blue")
    REGISTER = Button(root, text='Register', bd='5', padx=5, pady=7)
    REGISTER.pack()
    HOME = Button(root, text='HOME', bd='5', padx=5, pady=7,command=home_page)
    HOME.pack()
    register_button = Button(canvas, text="Register", font=("comic sans", 32, 'bold italic'), bg='#25003A',
                          activebackground='#25003A', fg='white',
                          activeforeground='white', bd=3, command=get_data)

    canvas.create_window(x / 2, y -800, window=TITLE) #text password
    canvas.create_window(x / 2-127, y / 2-70, window=REPASSWORD) #text password
    canvas.create_window(x / 2-100, y / 2, window=PASSWORD)
    canvas.create_window(x / 2-100, y / 2+70, window=USERNAME)
    canvas.create_window(x / 2-100, y / 2 - 140, window=EMAIL)  # blank input spot
    canvas.create_window(x / 2, y / 2-70, window=REPASS_INPUT)#blank input spot
    canvas.create_window(x / 2, y / 2, window=PASS_INPUT)
    canvas.create_window(x / 2, y / 2 -140, window=EMAIL_INPUT)
    canvas.create_window(x/2, y/2+70, window=USERNAME_INPUT)
    canvas.create_window(x/2, y/2+210, window=HOME)

def waiting_room():
    """after accepting a game the user gets here, he sees who else is connected and chooses a player"""
    canvas.delete('all')
    canvas.create_image(200, 50, image=logo)
    PASSWORD = Label(text="password:", padx=8, pady=9, font=(25), bg ="light blue")
    REPASSWORD = Label(text="confirm password:", padx=8, pady=9, font=(25), bg ="light blue")
    USERNAME = Label(text="username:", padx=8, pady=9, font=(25), bg="light blue")
    PASS_INPUT = Entry(root) # entry is  an object that gets input from the user
    PASS_INPUT.pack()
    REPASS_INPUT = Entry(root) # entry is  an object that gets input from the user
    REPASS_INPUT.pack()
    USERNAME_INPUT = Entry(root)
    USERNAME_INPUT.pack()
    RULES = Button(root, text='Rules', bd='5', padx=5, pady=7, command=rule_page)
    RULES.pack()
    Disconnect = Button(root, text='Disconnect', bd='5', padx=5, pady=7,command=home_page)
    Disconnect.pack()

    canvas.create_window(x / 2-127, y / 2-70, window=REPASSWORD) #text password
    canvas.create_window(x / 2-100, y / 2, window=PASSWORD)
    canvas.create_window(x / 2-100, y / 2+70, window=USERNAME)
    canvas.create_window(x / 2, y / 2-70, window=REPASS_INPUT)#blank input spot
    canvas.create_window(x / 2, y / 2, window=PASS_INPUT)
    canvas.create_window(x/2, y/2+70, window=Disconnect)
    canvas.create_window(x/2, y/2+210, window=RULES)

def welcome_page():
    """The user will arrive here after logging in"""
    canvas.delete('all')
    canvas.create_image(200, 50, image=logo)
    TITLE = Label(text="Good to see you f{name}", font=('comic sans',40),bg ="light blue")
    START = Button(root, text = 'Start', bd = '5', padx='6', pady='6', command = character_screen)#leads to the game hub
    DISCONNECT = Button(root, text = "Disconnect", bd = "5", padx='6', pady='6', command = start_page)
    START.pack()
    DISCONNECT.pack()
    canvas.create_window(x/2,y-1000, window = TITLE)
    canvas.create_window(x/2,y/2 ,window = START)
    canvas.create_window(x/2,y/2+70 ,window = DISCONNECT)

def character_screen():
    """The user will arrive to choose a character"""
    canvas.delete('all')
    canvas.create_image(200, 50, image=logo)
    TITLE = Label(text="Choose a character", font=('comic sans',40),bg ="light blue")
    HAT = Button(root, text = 'Hat', bd = '5', padx='6', pady='6')#leads to the game hub
    CAT = Button(root, text = 'Cat', bd = '5', padx='6', pady='6')#leads to the game hub
    IRON = Button(root, text = 'Iron', bd = '5', padx='6', pady='6')#leads to the game hub
    PENGUIN = Button(root, text = 'Penguin', bd = '5', padx='6', pady='6')#leads to the game hub
    CONTINUE = Button(root, text = 'Continue', bd = '5', padx='6', pady='6', command = game_hub)#leads to the game hub
    DISCONNECT = Button(root, text = "Disconnect", bd = "5", padx='6', pady='6', command = start_page)
    HAT.pack()
    CAT.pack()
    IRON.pack()
    PENGUIN.pack()
    canvas.create_window(x/2,y-1000, window = TITLE)
    canvas.create_window(30,y/2 - 50 ,window = HAT)
    canvas.create_window(30,y/2 - 100 ,window = CAT)
    canvas.create_window(30,y/2 - 150,window = IRON)
    canvas.create_window(30,y/2 ,window = PENGUIN)
    canvas.create_window(x/2, y/2, window = CONTINUE)
    canvas.create_window(x/2,y/2+70 ,window = DISCONNECT)

def game_hub():
    """The user will arrive here to see all other players"""
    canvas.delete('all')
    canvas.create_image(200, 50, image=logo)
    TITLE = Label(text="Choose a character", font=('comic sans',40),bg ="light blue")
    HAT = Button(root, text = 'Hat', bd = '5', padx='6', pady='6')#leads to the game hub
    CAT = Button(root, text = 'Cat', bd = '5', padx='6', pady='6')#leads to the game hub
    IRON = Button(root, text = 'Iron', bd = '5', padx='6', pady='6')#leads to the game hub
    PENGUIN = Button(root, text = 'Penguin', bd = '5', padx='6', pady='6')#leads to the game hub
    CONTINUE = Button(root, text = 'Continue', bd = '5', padx='6', pady='6', command = game_hub)#leads to the game hub
    DISCONNECT = Button(root, text = "Disconnect", bd = "5", padx='6', pady='6', command = start_page)
    HAT.pack()
    CAT.pack()
    IRON.pack()
    PENGUIN.pack()
    canvas.create_window(x/2,y-1000, window = TITLE)
    canvas.create_window(30,y/2 - 50 ,window = HAT)
    canvas.create_window(30,y/2 - 100 ,window = CAT)
    canvas.create_window(30,y/2 - 150,window = IRON)
    canvas.create_window(30,y/2 ,window = PENGUIN)
    canvas.create_window(x/2, y/2, window = CONTINUE)
    canvas.create_window(x/2,y/2+70 ,window = DISCONNECT)

def get_data():
        username = USERNAME_INPUT.get()
        password = PASS_INPUT.get()
        confirm_pass = REPASS_INPUT.get()
        email = EMAIL_INPUT.get()
        if password != confirm_pass:
            return False
        users.insert_user(username,password,email)
start_page()
mainloop()

