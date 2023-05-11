import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Editor")
        self.textarea = tk.Text(self.master)
        self.textarea.pack(fill=tk.BOTH, expand=True)
        self.menu = tk.Menu(self.master)
        self.filemenu = tk.Menu(self.menu, tearoff=0)
        self.filemenu.add_command(label="New", command=self.new_file)
        self.filemenu.add_command(label="Open", command=self.open_file)
        self.filemenu.add_command(label="Save", command=self.save_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.exit_app)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.editmenu = tk.Menu(self.menu, tearoff=0)
        self.editmenu.add_command(label="Cut", command=self.cut)
        self.editmenu.add_command(label="Copy", command=self.copy)
        self.editmenu.add_command(label="Paste", command=self.paste)
        self.menu.add_cascade(label="Edit", menu=self.editmenu)
        self.helpmenu = tk.Menu(self.menu, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.about)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)
        self.master.config(menu=self.menu)

    def new_file(self):
        self.textarea.delete('1.0', tk.END)

    def open_file(self):
        filename = filedialog.askopenfilename(defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filename:
            self.textarea.delete('1.0', tk.END)
            with open(filename, "r") as f:
                self.textarea.insert(tk.END, f.read())

    def save_file(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filename:
            with open(filename, "w") as f:
                f.write(self.textarea.get('1.0', tk.END))

    def exit_app(self):
        if messagebox.askyesno("Exit", "Do you really want to exit?"):
            self.master.destroy()

    def cut(self):
        self.textarea.event_generate("<<Cut>>")

    def copy(self):
        self.textarea.event_generate("<<Copy>>")

    def paste(self):
        self.textarea.event_generate("<<Paste>>")

    def about(self):
        messagebox.showinfo("About", "Simple Text Editor\nCreated by John Doe")

if __name__ == '__main__':
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
