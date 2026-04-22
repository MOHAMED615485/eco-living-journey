from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Medium Publishing Guide - Eco Living Journey', 0, 1, 'C')
        self.ln(5)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Read the text content
with open('MEDIUM_PUBLISHING_GUIDE.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Create PDF
pdf = PDF()
pdf.add_page()
pdf.set_font('Courier', '', 9)

# Add content line by line
for line in content.split('\n'):
    # Handle special characters
    line = line.encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(0, 4, line)

# Save
pdf.output('MEDIUM_PUBLISHING_GUIDE.pdf')
print('PDF created: MEDIUM_PUBLISHING_GUIDE.pdf')
print('\nYour complete publishing guide is ready!')
