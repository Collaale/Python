import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# Function to generate PDF with the analysis and graphs
def generate_pdf(dataframe, filename="fatura_analysis.pdf"):
    # Create a PDF document
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Add a page
    pdf.add_page()

    # Title
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, txt="Fatura Analysis Report", ln=True, align='C')

    # Analysis - Total Value of Purchases
    total_value = dataframe['ValorCompra'].sum()
    pdf.set_font('Arial', '', 12)
    pdf.cell(200, 10, txt=f"Total Value of Purchases: R$ {total_value:.2f}", ln=True)

    # Plot: Spending by Category
    plt.figure(figsize=(10, 5))
    category_summary = dataframe.groupby('categoria')['ValorCompra'].sum()
    category_summary.plot(kind='bar', color='skyblue')
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Spend (R$)")
    
    # Save plot as an image
    plot_image_path = "spending_by_category.png"
    plt.savefig(plot_image_path)
    plt.close()

    # Add the plot image to the PDF
    pdf.image(plot_image_path, x=10, y=50, w=180)

    # Save the PDF
    pdf.output(filename)
    messagebox.showinfo("Success", f"PDF generated: {filename}")

# Function to handle file upload and analysis
def upload_and_analyze():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if filepath:
        try:
            # Load the CSV file
            dataframe = pd.read_csv(filepath)
            
            # Perform the analysis and generate PDF
            generate_pdf(dataframe)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to process file: {e}")

# Create a Tkinter window
root = tk.Tk()
root.title("Fatura Analysis")
root.geometry("400x200")

# Add a button to upload the file
upload_button = tk.Button(root, text="Upload Fatura CSV", command=upload_and_analyze, padx=10, pady=5)
upload_button.pack(pady=50)

# Run the application
root.mainloop()
