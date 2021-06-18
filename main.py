# Currency Converter GUI
import tkinter
from tkinter import *
import sound_module as snd
import time


# Convert from USD to CAD
def convertToCAD():
    try:
        numUSD = 0
        try:
            numUSD = float(userEntry.get())
        except:
            pass

    except ValueError:
        # clear the entry box
        userEntry.delete(0, 20)
    else:
        snd.sound_effect("click")
    if numUSD >= 0:
        numCAD = numUSD * 1.20
        # format to 2 decimal places
        numCAD = "{:.2f}".format(numCAD)
        msg = "$" + str(userEntry.get()) + " USD is $" + str(numCAD) + " CAD"
        outputLabel.configure(text=msg)
        status.configure(text="ok")
    elif numUSD < 0:
        numCAD = numUSD * 1.20
        # format to 2 decimal places
        numCAD = "{:.2f}".format(numCAD)
        msg = "$" + str(userEntry.get()) + " USD is $" + str(numCAD) + " CAD"
        outputLabel.configure(text=msg)
        status.configure(text="Looks like your in debt!")
    else:
        outputLabel.configure(text="Error! Please try again.")
        status.configure(text="Enter a valid number.")


# Convert from CAD to USD
def convertToUSD():
    try:
        numCAD = 0
        try:
            numCAD = float(userEntry.get())
        except:
            pass

    except ValueError:
        # clear the entry box
        userEntry.delete(0, 20)
    else:
        snd.sound_effect("click")
    if numCAD >= 0:
        numUSD = numCAD / 1.20
        # format to 2 decimal places
        numUSD = "{:.2f}".format(numUSD)
        msg = "$" + str(userEntry.get()) + " CAD is $" + str(numUSD) + " USD"
        outputLabel.configure(text=msg)
        status.configure(text="ok")
    elif numCAD < 0:
        numUSD = numCAD / 1.20
        # format to 2 decimal places
        numUSD = "{:.2f}".format(numUSD)
        msg = "$" + str(userEntry.get()) + " CAD is $" + str(numUSD) + " USD"
        outputLabel.configure(text=msg)
        status.configure(text="Looks like your in debt!")
    else:
        outputLabel.configure(text="Error! Please try again.")
        status.configure(text="Enter a valid number.")


# a function to quit the window
def quitWindow():
    snd.sound_effect("end")
    time.sleep(1.2)
    root.destroy()
    sys.exit(0)


######################### GUI SETUP ##########################
# GUI window.
root = tkinter.Tk()
root.title("Currency Converter")
root.geometry("450x500")
root["bg"] = "#659dbd"

# title
title = tkinter.Label(root, text="Currency Converter", font=('Trebuchet MS Bold', 14), bg="#4fb045")
title.grid(row=0, column=0, columnspan=2)

# label for input instruction
inchLabel = tkinter.Label(
    root, text="Please enter value to be converted:", font=('Trebuchet MS', 12), bg="#FBEEC1")
root.grid_rowconfigure(1, minsize=50)
inchLabel.grid(row=1)

# entry box
userEntry = Entry(root, bd=2)
userEntry.grid(row=1, column=1)

# 'convert to CAD' button
convertButton1 = tkinter.Button(text="$USD --> $CAD", command=convertToCAD)
convertButton1.grid(row=2, column=0)

# 'convert to USD' button
convertButton2 = tkinter.Button(text="$CAD --> $USD", command=convertToUSD)
convertButton2.grid(row=2, column=1, sticky=W)
root.grid_rowconfigure(2, minsize=50)

# result text label
outputLabel = tkinter.Label(root, text="Select conversion button above", font=('Trebuchet MS', 14))
outputLabel.grid(row=3, column=0, columnspan=2)
root.grid_rowconfigure(3, minsize=50)

# add a GIF (only a GIF!)
photo = PhotoImage(file="Media/cc2.gif")
photoLabel = Label(root, image=photo)
photoLabel.grid(row=5, column=0, columnspan=2)
root.grid_rowconfigure(5, minsize=210)

# progress bar
status = Label(root, text="Waiting for user input.", bd=5, relief=SUNKEN, anchor=W, bg="#DAAD86")
status.grid(row=6, column=0, sticky=N, columnspan=2, pady=4)
root.grid_rowconfigure(6, minsize=50)

# quit button
Button(root, text='Quit', command=quitWindow,).grid(
    row=8, column=0, rowspan=2, columnspan=2, sticky=N, pady=4)


# start the GUI --> Leave here at the end!
root.mainloop()
