# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 17:50:41 2024

@author: timho
"""

import tkinter as tk
from tkinter import ttk


property_list = [
    ["Mass", "Distance", "Volume", "Area", "Pressure", "Energy"],  # dont forget a comma
    ["Pound", "KG", "Gram", "Ounce", "Milligram", "Ton(US)"],  # Mass
    [
        "Centimeter",
        "Meter",
        "Kilometer",
        "Inch",
        "Feet",
        "Mile",
        "Light-Year",
    ],  # Distance
    [
        "Liter",
        "Cubic Feet",
        "Cubic Yard",
        "Cubic Inch",
        "MilliLiter",
        "Cubic Centmeter",
        "Gallon",
    ],  # Volume
    [
        "Square Meter",
        "Square Feet",
        "Square Cm",
        "Square Micron",
        "Square Mile",
        "Square Inch",
    ],  # Area
    ["Pascal", "KiloPascal", "Bar", "mmHg", "PSI", "Atmospheres", "Torr"],  # Pressure
    [
        "Joule",
        "BTU",
        "Calorie",
        "ElectronVolt",
        "Erg",
        "Foot-Pound",
        "Kw-Hour",
    ],  # Energy
]

uom_dictionary = {
    "Meter": 1.0,
    "Kilometer": 1000,
    "Centimeter": 0.01,
    "Inch": 0.0254,
    "Feet": 0.3048,
    "Mile": 1609.344,
    "Light-Year": 9.46e15,
    "Pound": 453.59,
    "KG": 1000,
    "Gram": 1,
    "Ounce": 28.35,
    "Milligram": 1000,
    "Ton(US)": 907184.74,
    "Liter": 1.0,
    "Cubic Feet": 28.3168,
    "Cubic Yard": 764.5549,
    "Cubic Inch": 0.0164,
    "MilliLiter": 0.001,
    "Cubic Centmeter": 1000.0,
    "Gallon": 3.7854,
    "Square Meter": 1.0,
    "Square Feet": 0.0929,
    "Square Cm": 0.00010,
    "Square Micron": 1.0e-12,
    "Square Mile": 2589988.1103,
    "Square Inch": 0.00064516,
    "Pascal": 1.0,
    "KiloPascal": 1000.0,
    "Bar": 100000,
    "mmHg": 133.3224,
    "PSI": 6894.7573,
    "Atmospheres": 101325,
    "Torr": 133.3224,
    "Joule": 1.0,
    "BTU": 1055.0559,
    "Calorie": 4.184,
    "ElectronVolt": 6.2415e18,
    "Erg": 1e-7,
    "Foot-Pound": 1.3558,
    "Kw-Hour": 3600000,
}


class Converter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientists's Unit Conversion App")

        # initiate styling for ttk objects, show a few examples
        # do this prior to Frame creation
        self.style = ttk.Style(
            self
        )  
    
        # style other tKinter/ttk widgets
        # relief options are: "flat", "raised", "sunken", "solid", "ridge", "groove"
        self.style.configure("Converter.TFrame", background="Sky Blue", relief="groove")
        self.style.configure(
            "BrightGreen.TLabel", background="#00FF00", foreground="green"
        )
        self.style.configure(
            "Custom.TButton",
            font=("Helvetica", 8, "bold"),
            foreground="red",
            padding=(0, 0),
        )
        self.style.configure(
            "Custom.TCombobox", font=("Helvetica", 6, "bold"), foreground="green "
        )

        # create a working frame
        self.upper_frame = ttk.Frame(style="Converter.TFrame", width=400, height=500)
        self.upper_frame.grid(row=0, column=0, padx=10, pady=10)

        # Configure the grid
        for i in range(20):
            self.upper_frame.rowconfigure(i, weight=1)
        for j in range(7):
            self.upper_frame.columnconfigure(j, weight=1)

        self.create_widgets()  # CREATE AND PLACE THEM ALL

    def create_widgets(self):
        self.c1 = ttk.Combobox(
            self.upper_frame,
            textvariable=tk.StringVar(),
            width=50,
            values=property_list[0],
            state="readonly",
            font=("instruction_text_font"),
            foreground="blue",
        )
        uom_1 = "Click The Down Arrow to Choose the Physical Quantity ===>"
        self.c1.set(uom_1.title())
        self.c1.grid(row=0, column=3, columnspan=1)
        self.c1.bind("<<ComboboxSelected>>", self.on_field_change1)

        self.c2 = ttk.Combobox(
            self.upper_frame,
            textvariable=tk.StringVar(),
            width=30,
            values=property_list[1],
            state="readonly",
        )
        self.c2.set("Click to Choose Source Unit")
        self.c2.grid(row=2, column=2)

        self.c3 = ttk.Combobox(
            self.upper_frame,
            textvariable=tk.StringVar(),
            width=30,
            values=property_list[1],
            state="readonly",
        )
        self.c3.set("Click To Choose Target Unit")
        self.c3.grid(row=2, column=4)

        self.my_value = ttk.Entry(self.upper_frame, width=10)  # number to convert
        self.my_value.grid(row=3, column=3, columnspan=1)
        self.my_value.insert(tk.END, "0.0")

        self.style.configure("BoldBlue.TLabel", foreground="blue")
        self.result_label2 = ttk.Entry(
            self.upper_frame, width=20, justify="center", style="BoldBlue.TLabel"
        )
        self.result_label2.grid(row=3, column=4, columnspan=1, sticky="nsew")
        converted_note = "Converted Unit"
        self.result_label2.insert(tk.END, converted_note.title())  # initialize

        uom_2 = "Convert Unit"
        self.convert = ttk.Button(
            self.upper_frame, text=uom_2.title(), width=15, command=self.convert_entry
        )
        self.convert.grid(row=4, column=3, pady=0)

        self.style.configure("Label1.TLabel", foreground="Blue", relief=tk.RIDGE)
        # options for relief are tk.FLAT, Tk.RAISED, tk.SUNKEN, tk.GROOVED, tk.RIDGE
        uom_3 = "Value----->"
        self.value_label = ttk.Label(
            self.upper_frame,
            text=uom_3.upper(),
            style="Label1.TLabel",
            width=12,
            anchor="e",
        )
        self.value_label.grid(
            row=3, column=3, columnspan=1, sticky="w", padx=(100, 5)
        )  # padx moves the entire label to the right

        self.copy_button = ttk.Button(
            self.upper_frame, text="Copy Result", command=self.uom_to_clipboard
        )
        self.copy_button.grid(row=9, column=3, padx=1, pady=10)

        self.copied_label = ttk.Label(
            self.upper_frame, text="Copied!", style="BrightGreen.TLabel"
        )
        self.copied_label.grid(
            row=9, column=3, sticky="e", padx=20, pady=10
        )  # , sticky= 'w')
        self.copied_label.grid_remove()  # allow deletion from frame after user is notifoed

        # Style the Quit button
        self.quit_button_font = ("Helvetica", 10, "bold")  # Define a custom font
        self.style.configure(
            "Quit.TButton",
            background="red",       #Box border color
            foreground="green",     #text color
            font=self.quit_button_font,
        )
        # Adding the Quit button
        self.quit_button = ttk.Button(
            self.upper_frame, text="Quit", style="Quit.TButton", command=self.quit
        )
        self.quit_button.grid(row=19, column=3, padx=10, pady=10)

        ############  Begin Temperature Conversion ######################

        self.sep = ttk.Separator(self.upper_frame, orient="horizontal").grid(
            row=10, sticky="nsew", columnspan=10
        )  # , padx=100, pady=20))

        # Conversion functions dictionary
        self.result = {
            1: lambda x: 5 / 9 * (x - 32),  # Fahrenheit to Celsius
            2: lambda x: 1.8 * x + 32,  # Celsius to Fahrenheit
            3: lambda x: 273.15 + x,  # Celsius to Kelvin
            4: lambda x: 273.15 + 5 / 9 * (x - 32),  # Fahrenheit to Kelvin
            5: lambda x: 32 + 9 / 5 * (x - 273.15),  # Kelvin to Fahrenheit
            6: lambda x: x - 273.15,  # Kelvin to Celsius
            7: lambda x: 1 / (273.15 + x) * 100,  # special for Arrhenius Equation plot
        }

        # widgets  for temperature
        self.button_index = tk.IntVar(
            value=-1
        )  # Initialize with a default value #keeps track of buttons

        self.style.configure(
            "Message.TLabel",
            font=("bold_button_font"),
            foreground="blue",
            padding=(0, 0),
        )
        temperature_instruction = (
            "Select a Conversion operation, enter value, then Convert"
        )
        self.instructions = ttk.Label(
            self.upper_frame,
            style="Message.TLabel",
            text=temperature_instruction.title(),
        )
        self.instructions.grid(row=12, column=3)

        conversions = [
            "F 2 C",
            "C 2 F",
            "C 2 K",
            "F 2 K",
            "K 2 F",
            "K 2 C",
            "C 2 (1/K)*100"
        ]

        spot=11             #helper to modify start row of the temperature conversion

        #create, style and locate the temperture conversion option buttons
        #configure the default style for radio buttons
        self.temperature_button_font = ("Helvetica", 9, "bold")    # Define a custom font
        self.style = ttk.Style()
        self.style.configure("Temperature_Conversion.TButton",
                             foreground="black",
                             padding=(5, 5),
                             font=self.temperature_button_font)
        
        # Map the style for the selected state 
        self.style.map("Temperature_Conversion.TButton",
                       foreground=[('active', 'blue'), ('selected', 'red')],
                       background=[('active', 'yellow'), ('selected', 'green')],
                       relief=[('selected', 'solid')])
        self.selected_var = tk.StringVar()
        
        


        for index, btn_text in enumerate(conversions):
            button = ttk.Radiobutton(self.upper_frame, text=btn_text, 
                    style="Temperature_Conversion.TButton",
                    value =  btn_text,
                    command=lambda idx=index: self.set_button_index(idx) )
            button.grid(row=index + spot, column=2, padx=10, pady=5)     
            
        # the result entry box
        self.temperature_value = ttk.Entry(
            self.upper_frame, width=10, justify="center", foreground="blue"
        )  # width was 15
        self.temperature_value.grid(row=11, column=3, sticky="ns")
        self.temperature_value.insert(tk.END, "0.0")

        self.temperature = ttk.Button(
            self.upper_frame,
            text="Convert Temperature",
            width=20,
            command=self.validate_entry2,
        )
        self.temperature.grid(row=13, column=3)

        # Frame to put box around entry widget
        entry_frame = ttk.Frame(self.upper_frame, borderwidth=2, relief="groove")
        entry_frame.grid(row=11, column=4, padx=10, pady=10)
        self.result_label3 = ttk.Entry(
            entry_frame, width=24, justify="center", foreground="blue"
        )  # a frame within a frame!
        temperature_1 = "Converted Temperature"
        self.result_label3.insert(
            tk.END, temperature_1.title()
        )  # initialize with all upper case
        self.result_label3.grid(row=11, column=4, columnspan=1, sticky="nsew")

        # duplicates from above onto new grid
        self.copy_button2 = ttk.Button(
            self.upper_frame, text="Copy Result", command=self.temperature_to_clipboard
        )
        self.copy_button2.grid(row=14, column=3, padx=1, pady=10)

        self.copied_label2 = ttk.Label(
            self.upper_frame, text="Copied!", style="BrightGreen.TLabel"
        )
        self.copied_label2.grid(row=14, column=3, sticky="e", padx=20, pady=10)
        self.copied_label2.grid_remove()  # Initially hide the label

        # Bind mouse click event to hide the label
        self.bind("<Button-1>", self.hide_label)

    def formatted_answer(self, answer):
        # Define the bounds and decimal places
        max_value = 90000
        min_value = 0.0001
        decimal1 = 4
        decimal2 = 6
        # determine formatting
        if min_value <= answer <= max_value:
            return f"{answer:.{decimal1}f}"
        else:
            return f"{answer:.{decimal2}e}"

    def hide_label(self, event):
        self.copied_label.grid_remove
        self.copied_label2.grid_remove

    # add the functions to communicate
    def on_field_change1(self, event=None):
        z = self.c1.current()  # get the row number of selected entry
        # note: the above is not essential,  'z' is assigned to make the code clear
        # put the same row number into the source and target boxes
        self.c2.set(self.c1.get())  # must have parentheses
        self.c3.set(self.c1.get())
        # below left in code is available to give hints if needed
        # print('Index of selected is:',self.c1.current(), type(self.c1.current()))
        self.c2["values"] = property_list[z + 1]  # index into the list
        self.c3["values"] = property_list[z + 1]  # both boxes have same list
        # clear off answers from prior conversion
        self.reset_uom

    def convert_entry(self):
        v = (
            self.my_value.get()
        )  # get the value to be converted from the my_value Entry box
        v = v.replace(",", "")  # remove any comma
        input_value = float(v)  # ensure as float
        source = uom_dictionary.get(self.c2.get())
        target = uom_dictionary.get(self.c3.get())
        answer = input_value * source / target
        final_answer = self.formatted_answer(answer)
        self.result_label2.delete(0, tk.END)  # Clear the current content
        self.result_label2.insert(0, str(final_answer))  # Insert the new value

    def uom_to_clipboard(self):
        self.clipboard_clear()  # ensure that it is empty
        value = self.result_label2.get()  # get value from the result_label2 tEntry box
        # option: format if desired
        self.clipboard_append(value)
        self.update()  # ensure the clipboard content is properly updated
        self.copied_label.grid()

    def temperature_to_clipboard(self):
        self.clipboard_clear()  # ensure that clipboard is empty
        value = self.result_label3.get()  # get value from the result_label2 tEntry box
        # option: format if desired
        self.clipboard_append(value)
        self.update()  # ensure the clipboard content is properly set
        self.copied_label2.grid()

    def validate_entry2(self):  # called after user requests conversion
        self.reset_temperature
        s = self.temperature_value.get()
        v = s.replace(",", "")  # remove any commas
        input_value = float(v)
        index = self.button_index.get()
        index = index + 1
        answer = self.result[index](input_value)
        final_answer = self.formatted_answer(answer)
        self.result_label3.delete(0, tk.END)
        self.result_label3.insert(0, final_answer)

    def reset_uom(self):
        self.copied_label.grid_remove()

    def reset_temperature(self):
        self.copied_label.grid2_remove()

        self.bind_all(
            "<Button-1>", self.hide_label
        )  # bind mouse click event to hide the label

    def hide_label(self, event):
        self.copied_label.grid_remove()
        self.copied_label2.grid_remove()

    def set_button_index(self, index):
        self.button_index.set(index)


if __name__ == "__main__":
    app = Converter()
    app.mainloop()