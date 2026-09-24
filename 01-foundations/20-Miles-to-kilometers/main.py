import tkinter as tk

# Window setup
window = tk.Tk()
window.minsize(300, 100)
window.title("Miles to Kilometers")

# Labels setup
miles_label = tk.Label(text="Miles", font=("Times New Roman", 12, "bold"))
miles_label.grid(row=0, column=3)

equal_label = tk.Label(text="is equal to", font=("Times New Roman", 12, "bold"))
equal_label.grid(row=1, column=0)

result_label = tk.Label(text="0", font=("Times New Roman", 12, "bold"))
result_label.grid(row=1, column=2)

km_label = tk.Label(text="kilometers", font=("Times New Roman", 12, "bold"))
km_label.grid(row=1, column=3)

# Bottom setup
def click():
    result_label.config(text=(int(entry.get()) * 1.609)) # Calculates the convertion

botton = tk.Button(text="Calculate", command=click, font=("Times New Roman", 12, "bold"))
botton.grid(row=2, column=2)

# Entry setup
entry = tk.Entry(width=10)
entry.grid(row=0, column=2)
print(entry.get())

window.mainloop()