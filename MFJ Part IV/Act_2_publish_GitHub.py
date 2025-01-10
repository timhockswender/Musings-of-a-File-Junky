#timhockswender@gmail.com 
#seems to work ok for buttons 12/10/2024
import tkinter as tk
from tkinter import ttk


class Converter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientists's Unit Conversion App")
        self.geometry("800x400")

        self.style = ttk.Style(self)  
        #collect fonts together
        self.temperature_button_font = ("Helvetica", 9, "bold")    # Define a custom font
        self.bold_button_font = ("Helvetica", 8, "bold")
        #self.instruction_text_font = ("Helvetica", 2, 'bold' )
        #set configurations
        self.style.configure('Converter.TFrame', background='Sky Blue', relief = 'groove')  
        self.style.configure("BrightGreen.TLabel", background="lime", foreground="green") 
        self.style.configure("Custom.TButton", font=("Helvetica", 8, "bold"), foreground="red", padding=(0,0) )  
        self.style.configure("Custom.TCombobox", font =('Helvetica', 6, 'bold'), foreground='green ')
        
        self.upper_frame = ttk.Frame(self, style='Converter.TFrame')
        self.upper_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        for i in range(20):
            self.upper_frame.rowconfigure(i, weight=1)
        for j in range(7):
            self.upper_frame.columnconfigure(j, weight=1)

        self.create_widgets()       

    def create_widgets(self):
        
        # the stage front and stage back created
        self.sep=ttk.Separator(self.upper_frame,orient='horizontal').grid(row=10, sticky='nsew', columnspan=10)#, padx=100, pady=20))
      
        # Conversion functions dictionary
        self.result = {
            1: lambda x: 5/9*(x-32),          # Fahrenheit to Celsius
            2: lambda x: 1.8 * x + 32,        # Celsius to Fahrenheit
            3: lambda x: 273.15 + x,          # Celsius to Kelvin
            4: lambda x: 273.15 + 5/9*(x-32), # Fahrenheit to Kelvin
            5: lambda x: 32 + 9/5*(x-273.15), # Kelvin to Fahrenheit
            6: lambda x: x - 273.15,          # Kelvin to Celsius
            #7: lambda x: 1/(273.15 +x ) * 1000   # special for Arrhenius Equation plot
        }

        #widgets  for temperature
        self.button_index = tk.IntVar(value=-1)  # Initialize with a default value #keeps track of buttons
        #self.style.configure("Message.TLabel", font=('instruction_text_font'), foreground="blue", padding=(0,0) )    
        self.style.configure("Message.TLabel", font= ("Helvetica", 12, 'normal' ) , foreground="blue", padding=(0,0) ) 
        temperature_instruction = 'Select a Conversion operation, enter value, then Convert '
        self.instructions=ttk.Label(self.upper_frame, style = "Message.TLabel" , text= temperature_instruction.title() )
        self.instructions.grid(row=12, column=3)

        conversions = ['F 2 C', 'C 2 F', 'C 2 K', 'F 2 K', 'K 2 F', 'K 2 C','C 2 (1/K)*1000']

        spot=11             #helper to modify start row of the temperature conversion
        
        #create, style and locate the temperture conversion option buttons

        self.style.configure("Temperature_Conversion.TButton",
                             foreground="black",       #text color to start 
                             background = "lightblue", #background button color
                             padding=(5, 5),
                             font=self.temperature_button_font)
        
        # Map the style for the selected state
        self.style.map("Temperature_Conversion.TButton",
                       foreground=[ ('active', 'black'), ('selected', 'red')],
                       background=[ ('active', 'lightblue'), ('selected', 'green')], 
                       relief=[('selected', 'raised')])      
        
        for index, btn_text in enumerate(conversions):
            button = ttk.Radiobutton(self.upper_frame, text=btn_text, 
                    style="Temperature_Conversion.TButton",
                    value =  btn_text,
                    command=lambda idx=index: self.set_button_index(idx) )
            button.grid(row=index + spot, column=2, padx=10, pady=5)

   
        #The result entry box
        self.temperature_value = ttk.Entry(self.upper_frame, width=10, justify = 'center', foreground = 'blue') #width was 15
        self.temperature_value.grid(row=11, column=3 ,sticky='ns') 
        self.temperature_value.insert(tk.END, '0.0')

        self.temperature = ttk.Button(self.upper_frame, text="Convert Temperature", width=20, command=self.validate_entry2 )
        self.temperature.grid(row=13, column=3)

        # Frame to put box around entry widget
        entry_frame = ttk.Frame(self.upper_frame, borderwidth=2, relief="groove")
        entry_frame.grid(row=11, column=4, padx=10, pady=10)
        self.result_label3 = ttk.Entry(entry_frame, width=24, justify = 'center', foreground = 'blue') # a frame within a frame!
        temperature_1 = 'Converted Temperature'
        self.result_label3.insert(tk.END,  temperature_1 .title() ) #initialize with all upper case
        self.result_label3.grid(row=11, column=4, columnspan=1,sticky='nsew')
        
        # duplicates from above onto new grid
        self.copy_button2 = ttk.Button(self.upper_frame, text="Copy Result", command=self.temperature_to_clipboard )
        self.copy_button2.grid(row=14, column=3, padx=1, pady=10)

        self.copied_label2 = ttk.Label(
            self.upper_frame, text="Copied!", style="BrightGreen.TLabel")
        self.copied_label2.grid(row=14, column=3, sticky="e", padx=20, pady=10)
        self.copied_label2.grid_remove()  #initially hide the label

        # Bind mouse click event to hide the label
        self.bind("<Button-1>", self.hide_label)	
        
    def hide_label(self, event):
        #self.copied_label.grid_remove()
        self.copied_label2.grid_remove()   
        
        
    def temperature_to_clipboard(self):
        self.clipboard_clear()  # ensure that clipboard is empty
        value = self.result_label3.get()  # get value from the result_label2 tEntry box
        # option: format if desired
        self.clipboard_append(value)
        self.update()  # ensure the clipboard content is properly set
        self.copied_label2.grid()

    def formatted_answer(self, answer):
    # Define the bounds and decimal places
        max_value = 90000
        min_value = 0.0001
        decimal1 = 4
        decimal2 = 6
    #determine formatting
        if min_value <= answer <= max_value:
            return f"{answer:.{decimal1}f}"
        else:
            return f"{answer:.{decimal2}e}"   

   
    def validate_entry2(self):                   # called after user requests temperature conversion
        s= self.temperature_value.get()
        v=(s.replace(',', '') )                  #remove any commas  
        input_value=float(v)
        index = self.button_index.get()
        index = index+1
        answer= self.formatted_answer(self.result[index](input_value) )
        self.result_label3.delete(0, tk.END)
        self.result_label3.insert(0, answer)
    

    def set_button_index(self, index):
        self.button_index.set(index)
        


if __name__ == "__main__":
    app = Converter()
    app.mainloop()
