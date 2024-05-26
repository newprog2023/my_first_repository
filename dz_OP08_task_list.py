# приложение для управления задачами, таск-трекер с функционалом
# добавления, удаления и отметки задач, управление через кнопки
# и горячие клавиши, возможность сохранения списка задач в файл
import tkinter as tk
from tkinter import filedialog
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
def on_enter(event):
    add_task()  # Вызываем функцию добавления задачи при нажатии Enter
def del_task():
    select_task = task_list.curselection()
    if select_task:
        task_list.delete(select_task)
def on_delete(event):
    del_task()  # Вызываем функцию удаления текста при нажатии Delete
def mark_task():
    select_task = task_list.curselection()
    if select_task:
        task_list.itemconfig(select_task, bg='chartreuse3')
def mark_space(event):
    mark_task()
def save_list():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filename:
        with open(filename, "w") as file:
            list_items = task_list.get(0, tk.END)
            for item in list_items:
                file.write(item + "\n")
def load_list():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filename:
        task_list.delete(0, tk.END)
        with open(filename, "r") as file:
            for line in file:
                task_list.insert(tk.END, line.strip())

root = tk.Tk()
root.title('Трекер')
root.configure(background='cornsilk3')
root.geometry("400x600")

label1 = tk.Label(root, text='Поле для ввода задач', bg='cornsilk3')
label1.pack(pady=5)

task_entry = tk.Entry(root, width=50, bg='cornsilk1')
task_entry.pack(pady=(1,10))
task_entry.bind("<Return>", on_enter)  # Связываем нажатие Enter с функцией on_enter

add_task_button = tk.Button(root, text='Добавить задачу (Enter)', bg='goldenrod1', command=add_task)
add_task_button.pack(pady=5)

delete_button = tk.Button(root, text='Удалить задачу (Delete)', bg='azure4', command=del_task)
delete_button.pack(pady=5)

mark_button = tk.Button(root, text='Отметить выполненную задачу (Пробел)', bg='chartreuse3', command=mark_task)
mark_button.pack(pady=5)

label = tk.Label(root, text='<<< СПИСОК ЗАДАЧ ЛИЗЫ>>>', bg='cornsilk3')
label.pack(pady=(15,5))

task_list = tk.Listbox(root, height=15, width=70, bg='beige')
task_list.pack()
task_list.bind("<Delete>", on_delete)
task_list.bind("<space>", mark_space)

save_button = tk.Button(root, text="Сохранить список", command=save_list)
save_button.pack(side=tk.LEFT, padx=10)

load_button = tk.Button(root, text='Загрузить список', command=load_list)
load_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()