from my_package.model import ImageCaptioningModel
from my_package.model import ImageClassificationModel
from tkinter import *
from functools import partial
from PIL import ImageTk, Image
from tkinter import filedialog

from tkinter.ttk import Combobox


def fileClick(clicked, my_image_label, filename_label):
    
    global my_image, filepath
    filepath = filedialog.askopenfilename(initialdir="./data/imgs", title="Select a file", filetypes=[("Image Files", ("*.jpg", "*.png", "*.gif"))])
    if not filepath :
        return
    filename_label.config(text=filepath.split("/")[-1])
    img = Image.open(filepath)
    clicked.set(True)
    my_image = ImageTk.PhotoImage(img)
    my_image_label.configure(image=my_image)
    
def process(clicked, captioner, classifier, root, output_label):
    if not clicked.get():
        print("Select an image first!!")
        output_label.configure(text="Select an image first!!")
        return
    if options.get() == "Captioning":
        print("Performing Image Captioning...")
        y = captioner(filepath, 3)
        caption_text = "Captions : \n" + "\n".join(y)
        output_label.configure(text=caption_text)
        # Call Image Captioning model here
    elif options.get() == "Classification":
        print("Performing Image Classification...")
        classes = classifier(filepath)
        class_text ="Classification : \n"
        for percentage, class_name in classes:
            class_text += class_name + ": " + str(round(percentage*100, 2)) + "%\n"
        output_label.configure(text=class_text)
        # Call Image Classification model here


def main():
    root = Tk()
    # Provide a title to the root window.
    root.title("Image Processing App")
    root.configure(bg='pale green')
    
    #file name label
    filename_label = Label(root, text="", bg='pale green', fg='black',font=("Arial", 10))
    filename_label.grid(row=0, column=0)
    #filename_label.pack()
    
    # Instantiate the captioner and classifier models.
    captioner = ImageCaptioningModel()
    classifier = ImageClassificationModel()
    #file opening button
    clicked = BooleanVar()
    clicked.set(False)
    my_image_label = Label(root)
    my_image_label.grid(row=1, column=0)
    #my_image_label.pack()
    fileButton = Button(root, text="Open file", bg='dodger blue',command=partial(fileClick, clicked, my_image_label, filename_label))
    fileButton.grid(row=0, column=1)
    #fileButton.pack()
    
    #combo box
    global options
    options  = StringVar()
    options.set("Captioning")
    combo = OptionMenu(root, options, "Captioning", "Classification")
    combo.config(bg="dodger blue", fg="black")
    combo.grid(row=0, column=2)
    #combo.pack()


    #output label
    output_label = Label(root, text="", font=("Arial", 12) , bg='#ADD8E6', fg='black',borderwidth=2, relief="solid")
    output_label.grid(row=1, column=1)
    #output_label.pack()

    #process button
    #process_label = Label(root)
    process_button = Button(root, text="process", bg='dodger blue',command=partial(process, clicked, captioner, classifier, root, output_label))
    process_button.grid(row=0, column=4)
    #process_button.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
