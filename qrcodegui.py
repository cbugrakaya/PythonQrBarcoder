import pyqrcode
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from barcode import Code128
from barcode.writer import ImageWriter

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    label = Label(text="CODE TEXT : ", bg="steelblue")
    label.grid(row=0, column=1, padx=5, pady=5)

    root.entry = Entry(width=30, textvariable=QrBarcodeInput)
    root.entry.grid(row=0, column=2, padx=5, pady=5, columnspan=2)

    button = Button(width=10, text="GENERATE", command=QRCodeBarcodeGenerate)
    button.grid(row=0, column=4, padx=5, pady=5)

    label = Label(text="CODE TYPE : ", bg="steelblue")
    label.grid(row=1, column=1, padx=5, pady=5)

    qrRadio = Radiobutton(root, text="QRCode", variable=radioVariable,
                          value="qrcode", bg="steelblue")
    qrRadio.grid(row=1, column=2, padx=5, pady=5)

    bRadio = Radiobutton(root, text="Barcode", variable=radioVariable,
                         value="barcode", bg="steelblue")
    bRadio.grid(row=1, column=3, padx=5, pady=5)

    label = Label(text="CODE : ", bg="steelblue")
    label.grid(row=2, column=1, padx=5, pady=5)

    label = Label(text="Url of QRCODE : ",bg="steelblue")
    label.grid(row=3, column=1, padx=5, pady=5)

    root.entry = Entry(width=30, textvariable=QRBarcodeUrl)
    root.entry.grid(row=3, column=2, padx=5, pady=5, columnspan=2)    

    root.imageLabel = Label(root, background="steelblue")
    root.imageLabel.grid(row=4, column=1, columnspan=4, padx=5, pady=5)

# Defining QRCodeBarcodeGenerate() function to create QRCode or Barcode Images
def QRCodeBarcodeGenerate():
    # Storing user-input text in a variable
    QrBarcodeString = QrBarcodeInput.get()
    # Storing user-input url in a variable
    QrBarcodeUrl = QRBarcodeUrl.get()
    # Storing the radio-button selection
    QrBarcodeSelection = radioVariable.get()

    # Checking the radio button selection and generating the codes as per the selection
    if QrBarcodeSelection == "qrcode":
        # Checking if the user has entered some text then do the following
        if QrBarcodeString != '':
            # Setting destination path to save the QRCode Image
            QRCodePath = 'C:/Users/kaya_/Desktop/python/QrCode/'
            # Creating name with user-input text as the name and .png as the extension
            # Concatenating name with the path & qrcode keyword and storing in QRCodeName
            QRCodeName = QRCodePath + QrBarcodeString + ".png"

            # Generate object of QRCode with user-input text as the parameter
            qrGenerate = pyqrcode.create(QrBarcodeUrl)
            # Creating png image of QRCode using png(). To create png image pypng module
            # has to be installed. The png() takes the Filename & Scale Value as arguments
            qrGenerate.png(QRCodeName, scale = 10)

            # Opening the saved QRCode Image using the open() method of the Image module
            image = Image.open(QRCodeName)
            # Resizing the image using Image.resize()
            image = image.resize((400, 400), Image.ANTIALIAS)
            # Creating object of PhotoImage() class to display the frame
            image = ImageTk.PhotoImage(image)
            # Configuring the label to displaying the QRCode Image
            root.imageLabel.config(image=image)
            root.imageLabel.photo = image
        # If the user has not entered any text then error is shown
        else:
            messagebox.showerror("ERROR", "ENTER A TEXT.!")

    elif QrBarcodeSelection == "barcode":
        # Checking if the user has entered some text then do the following
        if QrBarcodeString != '':
            # Setting destination path to save the Barcode Image
            BarcodePath = 'C:/Users/kaya_/Desktop/python/QrCode/'
            # Creating name for the image with user-input text as the name
            # Concatenating name with path & barcode keyword and storing in BarcodeName
            BarcodeName = BarcodePath + QrBarcodeString + "-barcode"

            # Creating an object of Code128 class with user-input string as the parameter
            # and passing the ImageWriter() as the value of writer argument.
            barcodeOutput = Code128(QrBarcodeString, writer=ImageWriter())
            # Saving the barcode using the save() method of the object of class EAN13
            # with QrBarcodeName as the argument. Automatically saves image in png format.
            barcodeOutput.save(BarcodeName)

            # Opening the saved Barcode Image using the open() method of the Image module
            image = Image.open(BarcodeName+".png")
            # Resizing the image using Image.resize()
            image = image.resize((450, 300), Image.ANTIALIAS)
            # Creating object of PhotoImage() class to display the frame
            image = ImageTk.PhotoImage(image)
            # Configuring the label to displaying the Barcode Image
            root.imageLabel.config(image=image)
            root.imageLabel.photo = image
        # If the user has not entered any text then error is shown
        else:
            messagebox.showerror("ERROR", "ENTER A TEXT.!")

# Creating object root of tk
root = tk.Tk()

# Setting the title, window size, disabling the resizing property
# and setting the backgrounc color
root.title("QRCodeBarcode Generator")
root.geometry("600x530")
root.resizable(False, False)
root.config(background = "steelblue")

# Creating tkinter variable
QrBarcodeInput = StringVar()
radioVariable = StringVar()
QRBarcodeUrl = StringVar()
# Setting the default selection of Radio Button to qrcode
radioVariable.set("qrcode")

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()



