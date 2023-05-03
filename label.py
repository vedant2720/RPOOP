from tkinter import *
root = Tk()
root.geometry("744x133")
root.title("Labels")

l1 = Label(text =''' COEP's precursor, The Poona Engineering Class\n and Mechanical School was opened in July 1854,\n with an aim to provide suitable learning to the subordinate officers\n in the Public Works Department.\n The School was situated in Bhawani Peth, Poona ,\n and the accommodation consisted of three small detached houses\n for teaching purposes and a separate house for the Principal.\n

In June 1865 Mr. Theodore Cooke, M.A ,\n who held that appointment for 28 years was appointed Principal\n. The foundation stone of the new college was laid by\n His Excellency the Governor, Sir Bartle Frere, on the 5th August 1865.\n

College was affiliated to University of Bombay in 1866.\n In 1868 the College moved to the New Buildings.\n The college was divided into three departments\n for matriculated and unmatriculated students.\n''', bg ="red", fg="white", padx=13, pady=94, font="comicsansms,9,bold", borderwidth=3, relief=RAISED)

l1.pack(side=LEFT, fill=Y, padx=34, pady=34)

l2= Label(text ='''College of Engineering , Pune follows a semester pattern,\n wherein the academic year is divided into two terms, namely,\nthe Fall term and the Spring Term.
\n Each undergraduate student must complete a \n coursework of atleast 176 credits generally spread over 8 semesters.\n The college also allows students to take audit courses \n which allow them to earn extra credits.\n 
''', bg ="green", fg="white", padx=13, pady=94, font="comicsansms,9,bold", borderwidth=3, relief=RAISED)
l2.pack(side=LEFT, fill=Y, padx=34, pady=34)



# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE


# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady



root.mainloop()