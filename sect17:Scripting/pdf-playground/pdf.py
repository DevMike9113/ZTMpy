import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    for pdf in pdf_list:
        print(pdf)

# with open('dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)

# template = PyPDF2.PdfReader(open('super.pdf', 'rb'))
# watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))
# output = PyPDF2.PdfWriter()

# for i in range(len(template.pages)):
#     page = template.pages[i]
#     page.merge_page(watermark.pages[0])
#     output.add_page(page)

#     with open('watermarked.pdf', 'wb') as file:
#         output.write(file)
