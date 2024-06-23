from bs4 import BeautifulSoup
import requests
from fpdf import FPDF

# Initialize PDF class instance
pdf = FPDF()

# Add an initial page
pdf.add_page()

for i in range(1, 1486):
    url = f'https://fast.novelcenter.net/novel-book/swallowed-star/chapter-{i}'

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    raw_txt = soup.find_all('p')

    text_content = [p.get_text() for p in raw_txt]

    if i > 1:
        pdf.add_page()

    pdf.add_font('DejaVu', '', 'DejaVuSans.ttf')
    pdf.set_font('DejaVu', '', 12)

    # Add text content to the PDF with 10 lines (50 units) of space between paragraphs
    for paragraph in text_content:
        pdf.multi_cell(0, 5, paragraph)
        pdf.ln(5)  # Add a new line with a height of 10 units

    # Add 10 lines of space between chapters
    pdf.ln(50)

# Save the PDF to a file
pdf_output_path = 'swallowed_star.pdf'
pdf.output(pdf_output_path)

print(f"PDF created successfully and saved as {pdf_output_path}")
