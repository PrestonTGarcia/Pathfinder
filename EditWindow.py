"""

"""
import tkinter as tk


def main():
    """
    Opens the edit window and
    """
    root = tk.Tk()
    root.configure(width=500, height=150, bg="white")
    weight = []
    questionLabel = tk.Label(root, text="What is the new weight of each of the edges for this node?", bg='white')
    weightEntry = tk.Entry(root, width=3, bd=3)

    def submit(weightList):
        """
        Appends the weight entry values to the list and closes the window
        :param weightList: The list of weights(currently only one weight)
        """
        weightList.append(int(weightEntry.get()))
        root.destroy()

    submitButton = tk.Button(root, text='Submit', bg='lime', command=lambda: submit(weight))
    questionLabel.pack()
    weightEntry.pack()
    submitButton.pack()
    questionLabel.place(x=90, y=20)
    weightEntry.place(x=240, y=70)
    submitButton.place(x=227, y=120)
    root.mainloop()

    try:
        return weight[0]  # Only returns the the 0th index for now because all edges have the same weight.
    except IndexError:
        pass

if __name__ == '__main__':
    main()
