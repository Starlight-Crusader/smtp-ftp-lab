from ftp_func import FTPClient
from smtp_func import SMTPClient
from os import getenv

import tkinter
from tkinter import filedialog

def on_click():
    email_from = entry1.get()
    email_to = entry2.get()
    
    subject = entry3.get()
    body = entry4.get()
    
    file_path = filedialog.askopenfilename()

    ftp = FTPClient(getenv('APP_FTP_SERVER_HOST'), getenv('APP_FTP_SERVER_WD'), getenv('APP_CLIENT_FTP_USER'), getenv('APP_CLIENT_FTP_PASS'))
    url = ftp.upload(file_path)

    SMTPClient.send(subject, body, url, email_from, email_to)

    label_output.config(text=f"Email sent successfully!")

# Create the main window

root = tkinter.Tk()
root.title("LAB 9 - Email Client")

# Set the window size

window_width = 400
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

# Create the input fields

label1 = tkinter.Label(root, text="FROM:")
label1.pack(pady=10)
entry1 = tkinter.Entry(root, width=40)
entry1.pack()

label2 = tkinter.Label(root, text="TO:")
label2.pack(pady=10)
entry2 = tkinter.Entry(root, width=40)
entry2.pack()

label3 = tkinter.Label(root, text ="SUBJECT:")
label3.pack(pady=10)
entry3 = tkinter.Entry(root, width=40)
entry3.pack()

label4 = tkinter.Label(root, text ="TEXT:")
label4.pack(pady=10)
entry4 = tkinter.Entry(root, width=40)
entry4.pack()

# Create the "Send" button

display_button = tkinter.Button(root, text="Select an attach. and send", command=on_click)
display_button.pack(pady=20)

# Create a label to display the output

label_output = tkinter.Label(root, text="")
label_output.pack(pady=0)

# Start the main loop

root.mainloop()