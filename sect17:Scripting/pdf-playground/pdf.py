# import sys

import PyPDF2

# inputs = sys.argv[1:]
#
#
# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('super.pdf')
#
#
# pdf_combiner(inputs)
# # with open('dummy.pdf', 'rb') as file:
# #     reader = PyPDF2.PdfFileReader(file)
# #     print(reader.numPages)

# WATERMARK spreader
template = PyPDF2.PdfReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

    with open('watermarked.pdf', 'wb') as file:
        output.write(file)
