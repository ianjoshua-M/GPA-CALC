import tkinter as tk
from tkinter import ttk, messagebox

class GPACalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("GPA Calculator")
        self.root.geometry("650x550")  # Increased window size
        
        # Style
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 10))
        self.style.configure("TButton", font=("Arial", 10))
        self.style.configure("Header.TLabel", font=("Arial", 12, "bold"))
        
        # Create main container with scrollbar support
        main_container = ttk.Frame(root)
        main_container.pack(fill="both", expand=True)
        
        # Create canvas with scrollbar
        canvas = tk.Canvas(main_container)
        scrollbar = ttk.Scrollbar(main_container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Main frame
        main_frame = ttk.Frame(scrollable_frame, padding="20")
        main_frame.pack(fill="both", expand=True)
        
        # Title
        ttk.Label(main_frame, text="GPA Calculator", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Create two-column layout
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill="both", expand=True)
        
        # Left column - Module entries
        left_column = ttk.LabelFrame(content_frame, text="Enter your module marks", padding="10")
        left_column.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        # Right column - Grading scale
        right_column = ttk.Frame(content_frame)
        right_column.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
        # Configure grid weights
        content_frame.columnconfigure(0, weight=1)
        content_frame.columnconfigure(1, weight=1)
        
        # Module entries
        self.entries = {}
        
        # Module 1 (10%)
        ttk.Label(left_column, text="Module 1 (10%)", style="Header.TLabel").grid(row=0, column=0, columnspan=2, sticky="w", pady=(5, 5))
        
        ttk.Label(left_column, text="Module 1.1:").grid(row=1, column=0, sticky="w", padx=5, pady=2)
        self.entries["1.1"] = ttk.Entry(left_column, width=10)
        self.entries["1.1"].grid(row=1, column=1, sticky="w", padx=5, pady=2)
        
        ttk.Label(left_column, text="Module 1.2:").grid(row=2, column=0, sticky="w", padx=5, pady=2)
        self.entries["1.2"] = ttk.Entry(left_column, width=10)
        self.entries["1.2"].grid(row=2, column=1, sticky="w", padx=5, pady=2)
        
        # Module 2 (20%)
        ttk.Label(left_column, text="Module 2 (20%)", style="Header.TLabel").grid(row=3, column=0, columnspan=2, sticky="w", pady=(10, 5))
        
        ttk.Label(left_column, text="Module 2.1:").grid(row=4, column=0, sticky="w", padx=5, pady=2)
        self.entries["2.1"] = ttk.Entry(left_column, width=10)
        self.entries["2.1"].grid(row=4, column=1, sticky="w", padx=5, pady=2)
        
        ttk.Label(left_column, text="Module 2.2:").grid(row=5, column=0, sticky="w", padx=5, pady=2)
        self.entries["2.2"] = ttk.Entry(left_column, width=10)
        self.entries["2.2"].grid(row=5, column=1, sticky="w", padx=5, pady=2)
        
        # Module 3 (30%)
        ttk.Label(left_column, text="Module 3 (30%)", style="Header.TLabel").grid(row=6, column=0, columnspan=2, sticky="w", pady=(10, 5))
        
        ttk.Label(left_column, text="Module 3.1:").grid(row=7, column=0, sticky="w", padx=5, pady=2)
        self.entries["3.1"] = ttk.Entry(left_column, width=10)
        self.entries["3.1"].grid(row=7, column=1, sticky="w", padx=5, pady=2)
        
        ttk.Label(left_column, text="Module 3.2:").grid(row=8, column=0, sticky="w", padx=5, pady=2)
        self.entries["3.2"] = ttk.Entry(left_column, width=10)
        self.entries["3.2"].grid(row=8, column=1, sticky="w", padx=5, pady=2)
        
        # Module 4 (40%)
        ttk.Label(left_column, text="Module 4 (40%)", style="Header.TLabel").grid(row=9, column=0, columnspan=2, sticky="w", pady=(10, 5))
        
        ttk.Label(left_column, text="Module 4.1:").grid(row=10, column=0, sticky="w", padx=5, pady=2)
        self.entries["4.1"] = ttk.Entry(left_column, width=10)
        self.entries["4.1"].grid(row=10, column=1, sticky="w", padx=5, pady=2)
        
        ttk.Label(left_column, text="Module 4.2:").grid(row=11, column=0, sticky="w", padx=5, pady=2)
        self.entries["4.2"] = ttk.Entry(left_column, width=10)
        self.entries["4.2"].grid(row=11, column=1, sticky="w", padx=5, pady=2)
        
        # Grading scale display
        grade_frame = ttk.LabelFrame(right_column, text="Grading Scale", padding="10")
        grade_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        grade_scale = [
            ("Mark Scale", "Grade", "Scale Point"),
            ("Above 73", "A", "4.0"),
            ("70-73", "A-", "3.7"),
            ("67-69", "B+", "3.3"),
            ("64-66", "B", "3.0"),
            ("60-63", "B-", "2.7"),
            ("57-59", "C+", "2.3"),
            ("54-56", "C", "2.0"),
            ("50-53", "C-", "1.7"),
            ("47-49", "D+", "1.3"),
            ("44-46", "D", "1.0"),
            ("40-43", "D-", "0.7"),
            ("Below 40", "F", "0.0")
        ]
        
        # Create grade scale table
        grade_table = ttk.Frame(grade_frame)
        grade_table.pack(fill="both", expand=True)
        
        # Configure grid columns
        grade_table.columnconfigure(0, weight=1)
        grade_table.columnconfigure(1, weight=1)
        grade_table.columnconfigure(2, weight=1)
        
        for i, (mark, grade, point) in enumerate(grade_scale):
            if i == 0:  # Header row
                ttk.Label(grade_table, text=mark, font=("Arial", 10, "bold")).grid(row=i, column=0, padx=5, pady=2, sticky="w")
                ttk.Label(grade_table, text=grade, font=("Arial", 10, "bold")).grid(row=i, column=1, padx=5, pady=2, sticky="w")
                ttk.Label(grade_table, text=point, font=("Arial", 10, "bold")).grid(row=i, column=2, padx=5, pady=2, sticky="w")
            else:
                ttk.Label(grade_table, text=mark).grid(row=i, column=0, padx=5, pady=1, sticky="w")
                ttk.Label(grade_table, text=grade).grid(row=i, column=1, padx=5, pady=1, sticky="w")
                ttk.Label(grade_table, text=point).grid(row=i, column=2, padx=5, pady=1, sticky="w")
        
        # Award classification
        award_frame = ttk.LabelFrame(main_frame, text="Award Classification", padding="10")
        award_frame.pack(fill="both", pady=10)
        
        ttk.Label(award_frame, text="First Class begins from 3.7").pack(anchor="w")
        ttk.Label(award_frame, text="Second Class - Upper Division begins from 2.7").pack(anchor="w")
        ttk.Label(award_frame, text="Second Class - Lower Division begins from 1.7").pack(anchor="w")
        ttk.Label(award_frame, text="Pass begins from 0.7").pack(anchor="w")
        
        # Results frame
        result_frame = ttk.LabelFrame(main_frame, text="Results", padding="10")
        result_frame.pack(fill="both", pady=10)
        
        result_grid = ttk.Frame(result_frame)
        result_grid.pack(fill="both")
        
        # Results display
        self.gpa_var = tk.StringVar(value="0.0")
        self.award_var = tk.StringVar(value="N/A")
        
        ttk.Label(result_grid, text="Final GPA:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        ttk.Label(result_grid, textvariable=self.gpa_var, font=("Arial", 10, "bold")).grid(row=0, column=1, sticky="w", padx=5, pady=5)
        
        ttk.Label(result_grid, text="Award Classification:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ttk.Label(result_grid, textvariable=self.award_var, font=("Arial", 10, "bold")).grid(row=1, column=1, sticky="w", padx=5, pady=5)
        
        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill="x", pady=10)
        
        # Calculate button
        calculate_button = ttk.Button(button_frame, text="Calculate GPA", command=self.calculate_gpa)
        calculate_button.pack(side="left", padx=5)
        
        # Clear button
        clear_button = ttk.Button(button_frame, text="Clear All", command=self.clear_entries)
        clear_button.pack(side="left", padx=5)
    
    def calculate_gpa(self):
        try:
            # Get the values from the entries and convert to floats
            module_values = {key: float(entry.get()) for key, entry in self.entries.items() if entry.get()}
            
            # Check if all entries are filled
            if len(module_values) != 8:
                messagebox.showerror("Error", "Please fill in all module marks.")
                return
            
            # Calculate the GPA according to the formula
            module1 = (module_values["1.1"] + module_values["1.2"]) / 2 * 0.10
            module2 = (module_values["2.1"] + module_values["2.2"]) / 2 * 0.20
            module3 = (module_values["3.1"] + module_values["3.2"]) / 2 * 0.30
            module4 = (module_values["4.1"] + module_values["4.2"]) / 2 * 0.40
            
            # Calculate the final GPA
            final_gpa = module1 + module2 + module3 + module4
            
            # Update the GPA display
            self.gpa_var.set(f"{final_gpa:.2f}")
            
            # Determine the award classification
            if final_gpa >= 3.7:
                award = "First Class"
            elif final_gpa >= 2.7:
                award = "Second Class - Upper Division"
            elif final_gpa >= 1.7:
                award = "Second Class - Lower Division"
            elif final_gpa >= 0.7:
                award = "Pass"
            else:
                award = "Fail"
            
            # Update the award display
            self.award_var.set(award)
            
            # Show success message
            messagebox.showinfo("Success", f"Your Final GPA is {final_gpa:.2f}\nClassification: {award}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for all module marks.")
    
    def clear_entries(self):
        # Clear all entry fields
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        
        # Reset result displays
        self.gpa_var.set("0.0")
        self.award_var.set("N/A")

def main():
    root = tk.Tk()
    app = GPACalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()