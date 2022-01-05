import time
from tkinter import *
from tkinter import Toplevel

import cell_class

def create_cell():
        puzzle = [[27, 0, 25, 0, 3, 0, 5, 0, 7],
          [0, 29, 0, 23, 0, 11, 0, 9, 0],
          [33, 0, 0, 0, 0, 0, 0, 0, 15],
          [0, 35, 0, 0, 0, 0, 0, 17, 0],
          [39, 0, 0, 0, 0, 0, 0, 0, 49],
          [0, 41, 0, 0, 0, 0, 0, 51, 0],
          [59, 0, 0, 0, 0, 0, 0, 0, 75],
          [0, 63, 0, 67, 0, 71, 0, 81, 0],
          [61, 0, 65, 0, 69, 0, 79, 0, 77]]
        cell_list = []
        for r in range(9):
           row = []
           for c in range(9):
             x = cell_class.cell(r, c, puzzle)
             row.append(x)
           cell_list.append(row)
        return cell_list

def warning(ent, value):
    pop_up = Toplevel(window)
    pop_up.title("WARNING")
    pop_up.geometry("250x150")
    if value == 'valid':
        pop_label = Label(pop_up,
                          text="\n\n\n " + str(ent.get()) + "  IS INVALID ENTRY\nONLY ENTER INTEGERS!\nTRY AGAIN!!")
    elif value == 'repeat':
        pop_label = Label(pop_up, text="\n\n\n " + str(ent.get()) + "  IS ALREADY WRITTEN\n TRY OTHER VALUES!!")
    elif value == 'range':
        pop_label = Label(pop_up,
                          text="\n\n\n " + str(ent.get()) + "  IS INVALID ENTRY\nENTER NUMBERS IN RANGE OF 1 TO 81 !")
    elif value == 'hint':
        pop_label = Label(pop_up,
                          text="\n\n\nHints Exhausted")
    pop_label.pack()
        

def is_valid(label): #checks whether entry is an integer or not
    ent = label.get()
    if ent.isdigit():
        return True


def is_surrounded(cell): #checks if a cell is surrounded from all 4 sides
    if cell.value == 0:
        if cell.row == 0:
            if cell.down_cell_value != 0 and cell.left_cell_value != 0 and cell.right_cell_value != 0:
                return True
        if cell.row == 8:
            if cell.up_cell_value != 0 and cell.left_cell_value != 0 and cell.right_cell_value != 0:
                return True
        if cell.column == 0:
            if cell.down_cell_value != 0 and cell.up_cell_value != 0 and cell.right_cell_value != 0:
                return True
        if cell.column == 8:
            if cell.down_cell_value != 0 and cell.left_cell_value != 0 and cell.up_cell_value != 0:
                return True
        else:
            if cell.down_cell_value != 0 and cell.left_cell_value != 0 and cell.up_cell_value != 0 and cell.right_cell_value != 0:
                return True


def is_complete(cells): 
    count = 0
    for r in range(9):
        for c in range(9):
            if cells[r][c].value != 0:
                count += 1
    if count == 81:
        return True

def in_range(ent): # checks if the entry is between the ranges of 0 to 81
    val = int(ent.get())
    if 1 <= val <= 81:
        return True

def check_numbrix():
    count = 0
    for r in range(9):
        for c in range(9):
            if cells[r][c].value == lst[r][c]:
                count += 1
    return count


def win():
    total_time = int((final - initial))
    pop_up = Toplevel(root)
    pop_up.title("VICTORY")
    pop_up.geometry("250x150")
    pop_label = Label(pop_up, text="\n\n\n YOU WON!!\nCONGRATULATIONS!\nIT TOOK YOU " + str(total_time) + " seconds")
    pop_label.pack()


def lost():
    global pop_up
    total_time = int((final - initial))
    pop_up = Toplevel(root)
    pop_up.title("OOPS :(")
    pop_up.geometry("250x150")
    pop_label = Label(pop_up,
                      text="\n\n\nYOU LOST :( \nBETTER LUCK NEXT TIME!\nRESIGNED IN " + str(total_time) + " seconds")
    pop_label.pack()
    window.destroy()


def hint():
      for r in range(9):
        for c in range(9):
            if cells[r][c].value == 0:
                hint = Label(window, text=f"{lst[r][c]}")
                hint.grid(row=r, column=c)
                cells[r][c].value = lst[r][c]
                return
        

def start_time(): # to calculate time taken by the player
    global initial
    initial = time.time()
    return initial

def stop():
    global final
    final = time.time()

    if (is_complete(cells)):
        count = check_numbrix()
        if count == 81:
            win()
        else:
            lost()

    else:
        lost()


def entry(ent, r, c): 

    if not (is_valid(ent)):
        warning(ent, 'valid')

    elif not in_range(ent):
        warning(ent, 'range')

    else:
        val = int(ent.get())
        cells[r][c].value = val
        entries = window.grid_slaves()

        # updating up, down, right, left values and also if any value is surrounded we change its colour
        # updating up value
        if r > 0:
            cells[r - 1][c].down_cell_value = val
            if is_surrounded(cells[r - 1][c]):
                converted_position = 80 - (9 * (r - 1) + c)
                up_frame = entries[converted_position]  # finding frame that corresponds to the up cell
                up_entries = up_frame.pack_slaves()  
                up_entry = up_entries[0]  
                up_entry['bg'] = 'blue'  

        # updating down cell
        if r < 8:
            cells[r + 1][c].up_cell_value = val
            if is_surrounded(cells[r + 1][c]):
                entries[80 - (9 * (r + 1) + c)].pack_slaves()[0]['bg'] = 'blue'

        if c > 0:  # update left cell
            cells[r][c - 1].right_cell_value = val
            if is_surrounded(cells[r][c - 1]):
                entries[80 - (9 * r + (c - 1))].pack_slaves()[0]['bg'] = 'blue'

        if c < 8:  # update right cell
            cells[r][c + 1].left_cell_value = val
            if is_surrounded(cells[r][c + 1]):
                entries[80 - (9 * r + (c + 1))].pack_slaves()[0]['bg'] = 'blue'
        ent['bg'] = 'SystemButtonFace'


helper = lambda a, e, r, c: (lambda event: entry(e, r, c))


def grid():
    global cells
    global window
    cells=create_cell()
    start_time()

    window = Toplevel(root)
    window.title("NUMBRIX")
    for r in range(9):
        for c in range(9):
            frame = Frame(master=window, relief=RAISED, borderwidth=2)
            frame.grid(row=r, column=c)
            if is_surrounded(cells[r][c]):
                label = Entry(master=frame, bg="blue", width=2)
                label.bind("<Return>", (helper(0, label, r, c)))
            elif cells[r][c].value == 0:
                label = Entry(master=frame, width=2)
                label.bind("<Return>", (helper(0, label, r, c)))
            else:
                label = Label(master=frame, text=f"{cells[r][c].value}",width=2)
            label.pack()



#answers
lst = [[27, 26, 25, 24, 3, 4, 5, 6, 7],
       [28, 29, 30, 23, 2, 11, 10, 9, 8],
       [33, 32, 31, 22, 1, 12, 13, 14, 15],
       [34, 35, 36, 21, 20, 19, 18, 17, 16],
       [39, 38, 37, 44, 45, 46, 47, 48, 49],
       [40, 41, 42, 43, 54, 53, 52, 51, 50],
       [59, 58, 57, 56, 55, 72, 73, 74, 75],
       [60, 63, 64, 67, 68, 71, 80, 81, 76],
       [61, 62, 65, 66, 69, 70, 79, 78, 77]]

root = Tk()
root.title('NUMBRIX PUZZLE')

intro=Label(root, text="===WELCOME TO NUMBRIX PUZZLE===\nHOW TO PLAY?")
intro.pack()

instruction=Label(root,text="Click on the START Button.\n¬ Starting anywhere, fill in the blank squares with the missing numbers\
 so they make a path of consecutive numbers in sequence, 1 through 81. \n¬ You can work horizontally or vertically in any direction.\n¬ Diagonal \
paths are NOT ALLOWED.\n¬ When you're done with the puzzle or you don't think you can complete it, click the STOP button.",justify=LEFT)
instruction.pack()

end=Label(root,text="\n\nNeed help? Click the HINT button.\n\
That is all for the instructions!\n\nARE YOU READY?")
end.pack()

frame=Frame(root)
frame.pack(side=BOTTOM)
Start = Button(frame, text="START",fg="red", command=grid)
Start.pack(side=LEFT)
Stop = Button(frame, text="STOP",fg="blue", command=stop)
Stop.pack(side=LEFT)
Hint = Button(frame, text="HINT",fg="brown", command=hint)
Hint.pack(side=LEFT)
line=Label(frame,text='\n')
line.pack(side=BOTTOM)
root.mainloop()
