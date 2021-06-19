"""
Window used for editing the edges.
"""
import tkinter as tk


def main():
    """
    Opens the edit window and returns edits needed.
    """
    root = tk.Tk()
    root.configure(width=500, height=150, bg="white")
    weight = []
    question_label = tk.Label(root, text="What is the new weight of each of the edges for this node?", bg='white')
    down_entry = tk.Entry(root, width=3, bd=3)
    up_entry = tk.Entry(root, width=3, bd=3)
    right_entry = tk.Entry(root, width=3, bd=3)
    left_entry = tk.Entry(root, width=3, bd=3)

    def submit(weight_list):
        """
        Appends the weight entry values to the list and closes the window
        :param weight_list: The list of weights(currently only one weight)
        """
        weight_list.append(int(down_entry.get()))
        weight_list.append(int(up_entry.get()))
        weight_list.append(int(right_entry.get()))
        weight_list.append(int(left_entry.get()))
        root.destroy()

    submitButton = tk.Button(root, text='Submit', bg='lime', command=lambda: submit(weight))
    question_label.pack()
    down_entry.pack()
    up_entry.pack()
    right_entry.pack()
    left_entry.pack()
    submitButton.pack()
    question_label.place(x=90, y=20)
    down_entry.place(x=150, y=70)
    up_entry.place(x=210, y=70)
    right_entry.place(x=270, y=70)
    left_entry.place(x=330, y=70)
    submitButton.place(x=227, y=120)
    root.mainloop()

    try:
        if len(weight) != 4:
            raise IndexError

        return weight

    except IndexError:
        pass


if __name__ == '__main__':
    main()
