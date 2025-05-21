# create_pdf.py

from fpdf import FPDF

def create_pdf(filename="clcoding.pdf"):
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt="My First PDF in Python", ln=True, align="C")

    # Body text
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt="This PDF is created using Python and the fpdf library.")

    # Save the PDF file
    pdf.output(filename)
    print(f"PDF created successfully! File saved as '{filename}'")

if __name__ == "__main__":
    create_pdf()
