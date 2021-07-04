from tkinter import *
import random

root = Tk();
root.title("Driving Licence");
root.geometry("500x500");

show_list = Label(root, text = "Listed Items:")
show_random_number = Label(root)

list_of_item = ["Camera", "Water Bottle", "Juice", "Pizza", "Tablet", "Chocolates", "Chips", "Hanky", "Blanket", "Car Keys", "Sunsceen", "Snacks", "Cold Drink", "Biscuit", "Basket"]

show_list['text'] = str(list_of_item)

def randomNumber():
    random_no = random.sample(range(0, 15),1)
    show_random_number['text'] = "Put This " + list_of_item[str(random_no)] + "in your bag"

btn = Button(root, text = "Which item to put in bag?", command = randomNumber)
btn.place(relx = 0.0, rely = 0.1, anchor = CENTER)
show_list.place(relx = 0.0, rely = 0.0, anchor = CENTER)
show_random_number.place(relx = 0.0, rely = 0.2, anchor = CENTER)

btn.pack()
show_list.pack()
show_random_number.pack()

root.mainloop()