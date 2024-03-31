# from tkinter import *
# from tkinter import filedialog
# import tkinter as tk
# from PIL import Image,ImageTk
# import os
# from stegano import lsb

# root = Tk()
# root.title("Steganography - Hide a Secret Text Message In a Image")
# root.geometry("700x500+150+180")
# root.resizable(False,False)
# root.configure(bg="#000000")

# # All the Function

# def showimage():
#     global filename
#     filename= filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File ' , filetype=(("PNG file" ,  "*.png"), ("JPG file", "*.jpg"),("All file", "*.txt")))
#     img  = Image.open(filename)
#     img= ImageTk.PhotoImage(img)
#     lb1.configure(image=img, width=250 ,height=250)
#     lb1.image = img  

# def Hide():
#     global secret
#     message = text1.get(1.0 , END)
#     secret = lsb.hide(str(filename),message)


# def Show():
#     clear_message= lsb.reveal(filename)
#     text1.delete(1.0, END)
#     text1.insert(END , clear_message)


# def save():
#     secret.save("hidden.png")
# # Adding an image
# img = PhotoImage(file="logo.jpg")
# root.iconphoto(False,img)

# # Logo
# logo= PhotoImage(file="logo.png")
# Label(root,image=logo,bg="#000000").place(x=10,y=0)

# Label(root,text="CYBER SECURITY", bg="#000320" ,fg="Cyan", font="arial 25 bold").place(x=100,y=20)

# # first frame
# frame1 = Frame(root ,bd=3, bg="black" , width=340,height=280 , relief=GROOVE)
# frame1.place(x=10,y=80)

# lb1 = Label(frame1 , bg="black")
# lb1.place(x=40, y=10)

# # second frame
# frame2 = Frame(root ,bd=3, bg="white", width=340,height=280 , relief=GROOVE)
# frame2.place(x=350,y=80)

# text1 = Text(frame2 , font="Robote 20", bg="white", fg="black", relief=GROOVE , wrap=WORD)
# text1.place(x=0,y=0, width=320 , height=295)

# # Scrollbar
# scrollbar= Scrollbar(frame2)
# scrollbar.place(x=320, y=0, height=300)

# scrollbar.configure(command=text1.yview)
# text1.configure(yscrollcommand=scrollbar.set)

# # 3rd Frame
# frame3 = Frame(root, bd=3, bg="#2f4155", width=330,  height=100 ,relief=GROOVE)
# frame3.place(x=10, y=370)

# Button(frame3,text="Open Image",width=10, height=2 ,font="arial 14 bold", command=showimage).place(x=20,y=30)
# Button(frame3,text="Save Image",width=10, height=2 ,font="arial 14 bold", command=save).place(x=180,y=30)
# Label(frame3 , text="Picture ,  Image , Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

# # 4th frame
# frame4 = Frame(root, bd=3, bg="#2f4155", width=330,  height=100 ,relief=GROOVE)
# frame4.place(x=360, y=370)

# Button(frame4,text="Hide Data",width=10, height=2 ,font="arial 14 bold", command=Hide).place(x=20,y=30)
# Button(frame4,text="Show Data",width=10, height=2 ,font="arial 14 bold", command=Show).place(x=180,y=30)
# Label(frame4 , text="Picture ,  Image , Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)


# root.mainloop()

# from tkinter import *
# from tkinter import filedialog
# import tkinter as tk
# from PIL import Image, ImageTk
# import os
# from stegano import lsb

# root = Tk()
# root.title("Steganography - Hide a Secret Text Message In a Image")
# root.geometry("700x500+150+180")
# root.resizable(False, False)
# root.configure(bg="#000000")

# # All the Function

# def showimage():
#     global filename
#     filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File ',
#                                           filetype=(("PNG file", "*.png"), ("JPG file", "*.jpg"), ("All file", "*.*")))
#     img = Image.open(filename)
#     img = ImageTk.PhotoImage(img)
#     lb1.configure(image=img, width=250, height=250)
#     lb1.image = img

# def hide_file():
#     global filename
#     file_to_hide = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File to Hide',
#                                               filetype=(("All files", "*.*"),))
#     lsb.hide(filename, file_to_hide).save("hidden_image.png")
#     show_message("File hidden successfully!")

# def show_data():
#     global filename
#     hidden_file_path = lsb.reveal(filename)
#     if hidden_file_path:
#         try:
#             with open(hidden_file_path, "r") as file:
#                 hidden_data = file.read()
#             show_message("Hidden data: \n" + hidden_data)
#         except Exception as e:
#             show_message("Error reading hidden data: " + str(e))
#     else:
#         show_message("No hidden data found!")

# def show_message(message):
#     text1.delete(1.0, END)
#     text1.insert(END, message)

# # Adding an image
# img = PhotoImage(file="logo.jpg")
# root.iconphoto(False, img)

# # Logo
# logo = PhotoImage(file="logo.png")
# Label(root, image=logo, bg="#000000").place(x=10, y=0)

# Label(root, text="CYBER SECURITY", bg="#000320", fg="Cyan", font="arial 25 bold").place(x=100, y=20)

# # first frame
# frame1 = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
# frame1.place(x=10, y=80)

# lb1 = Label(frame1, bg="black")
# lb1.place(x=40, y=10)

# # second frame
# frame2 = Frame(root, bd=3, bg="white", width=340, height=280, relief=GROOVE)
# frame2.place(x=350, y=80)

# text1 = Text(frame2, font="Roboto 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
# text1.place(x=0, y=0, width=320, height=295)

# # Scrollbar
# scrollbar = Scrollbar(frame2)
# scrollbar.place(x=320, y=0, height=300)

# scrollbar.configure(command=text1.yview)
# text1.configure(yscrollcommand=scrollbar.set)

# # 3rd Frame
# frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
# frame3.place(x=10, y=370)

# Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=showimage).place(x=20, y=30)
# Button(frame3, text="Hide File", width=10, height=2, font="arial 14 bold", command=hide_file).place(x=180, y=30)
# Label(frame3, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

# # 4th frame
# frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
# frame4.place(x=360, y=370)

# Button(frame4, text="Show Data", width=10, height=2, font="arial 14 bold", command=show_data).place(x=20, y=30)
# Label(frame4, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

# root.mainloop()

# Final code 1


from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

root = Tk()
root.title("Steganography - Hide a Secret Message/File In an Image")
root.geometry("700x500+150+180")
root.resizable(False, False)
root.configure(bg="#000000")

# Make the window fullscreen
root.attributes("-fullscreen", True)

# All the Functions

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File ',
                                          filetype=(("PNG file", "*.png"), ("JPG file", "*.jpg"), ("All file", "*.*")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lb1.configure(image=img, width=400, height=400)
    lb1.image = img

def hide_text():
    global filename
    message = text1.get(1.0, END)
    lsb.hide(filename, message).save("hidden_image.png")
    show_message("Text hidden successfully!")

def hide_file():
    global filename
    file_to_hide = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File to Hide',
                                              filetype=(("All files", "*.*"),))
    lsb.hide(filename, file_to_hide).save("hidden_image.png")
    show_message("File hidden successfully!")

def show_data():
    global filename
    hidden_data = lsb.reveal(filename)
    if hidden_data:
        # Check if hidden data is a file path
        if os.path.isfile(hidden_data):
            try:
                with open(hidden_data, "r") as file:
                    hidden_content = file.read()
                show_message("Hidden data from file: \n" + hidden_content)
            except Exception as e:
                show_message("Error reading hidden file data: " + str(e))
        else:
            # If hidden data is text
            show_message("Hidden text inside the image: \n" + hidden_data)
    else:
        show_message("No hidden data found!")


def save():
    global filename
    lsb.hide(filename, text1.get(1.0, END)).save("hidden_image.png")
    show_message("Text saved successfully!")

def show_message(message):
    text1.delete(1.0, END)
    text1.insert(END, message)

# Adding an image
try:
    img = Image.open("logo2.jpg")
    img = ImageTk.PhotoImage(img)
    # label = Label(root, image=img)
    # label.pack()
except Exception as e:
    print("Error loading image:", e)
# img = PhotoImage(file="img2.jpg")
root.iconphoto(False, img)

# Logo
# logo = PhotoImage(file="logo.png")
try:
    logo = Image.open("img2.jpg")
    logo = ImageTk.PhotoImage(logo)
    # label = Label(root, image=img)
    # label.pack()
except Exception as e:
    print("Error loading image:", e)
Label(root, image=logo, bg="#000000").place(relx=0.05, rely=0.05, relwidth=0.15, relheight=0.15)

Label(root, text="CYBER SECURITY", bg="#000320", fg="Cyan", font="arial 25 bold").place(relx=0.2, rely=0.05)

# first frame
frame1 = Frame(root, bd=3, bg="black", relief=GROOVE)
frame1.place(relx=0.05, rely=0.2, relwidth=0.55, relheight=0.7)

lb1 = Label(frame1, bg="black")
lb1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.85)

# second frame
frame2 = Frame(root, bd=3, bg="black", relief=GROOVE)
frame2.place(relx=0.62, rely=0.2, relwidth=0.33, relheight=0.2)

text1 = Text(frame2, font="Roboto 12", bg="black", fg="white", insertbackground="white", relief=GROOVE, wrap=WORD)

text1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)  

# Scrollbar
scrollbar = Scrollbar(frame2)
scrollbar.place(relx=0.95, rely=0.05, relheight=0.9)

scrollbar.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar.set)

# 3rd Frame
frame3 = Frame(root, bd=3, bg="#000000", relief=GROOVE)
frame3.place(relx=0.62, rely=0.45, relwidth=0.33, relheight=0.2)

Button(frame3, text="Open Image", font="arial 10 bold", bg="black", fg="white", command=showimage).place(relx=0.05, rely=0.2, relwidth=0.4, relheight=0.6)
Button(frame3, text="Hide Text", font="arial 10 bold", bg="black", fg="white", command=hide_text).place(relx=0.55, rely=0.2, relwidth=0.4, relheight=0.6)

Label(frame3, text="Picture, Image, Photo File", bg="#000000", fg="yellow").place(relx=0.05, rely=0.1, relwidth=0.9)

# 4th frame
frame4 = Frame(root, bd=3, bg="#000000", relief=GROOVE)
frame4.place(relx=0.62, rely=0.7, relwidth=0.33, relheight=0.2)

Button(frame4, text="Show Text", font="arial 10 bold", bg="black", fg="white", command=show_data).place(relx=0.05, rely=0.2, relwidth=0.4, relheight=0.6)
# Button(frame4, text="Save Text", width=10, height=2, font="arial 14 bold", command=save).place(relx=0.5, rely=0.3)
Button(frame4, text="Hide File", font="arial 10 bold", bg="black", fg="white", command=hide_file).place(relx=0.55, rely=0.2, relwidth=0.4, relheight=0.6)
Label(frame4, text="Picture, Image, Photo File", bg="#000000", fg="yellow").place(relx=0.05, rely=0.1, relwidth=0.9)

root.mainloop()







