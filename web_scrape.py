from bs4 import BeautifulSoup
import requests
from fpdf import FPDF

# Input novel name with underline e.g. swallowed_star
novel_name = 'swallowed_star'

# Latest chapter of the novel
max_chapter = 5


pdf = FPDF()
pdf.add_page()

for i in range(1, max_chapter):
    url = f'https://fast.novelcenter.net/novel-book/{novel_name}/chapter-{i}'

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    raw_txt = soup.find_all('p')

    text_content = [p.get_text() for p in raw_txt]

    if i > 1:
        pdf.add_page()

    pdf.add_font('DejaVu', '', 'DejaVuSans.ttf')
    pdf.set_font('DejaVu', '', 12)

    for paragraph in text_content:
        pdf.multi_cell(0, 5, paragraph)
        pdf.ln(5)

    pdf.ln(50)

pdf_output_path = f'{novel_name}.pdf'
pdf.output(pdf_output_path)

print(f"PDF created successfully and saved as {pdf_output_path}")
