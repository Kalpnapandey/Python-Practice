# File Type Detector
# Ask for a filename (e.g., report.pdf).
# If the name ends with .pdf → “PDF file”
# If .docx → “Word document”
# If .xlsx → “Excel spreadsheet”
# If .jpg or .png → “Image file”
# (All these should be checked independently, using multiple if statements and
# endswith())
file=input("Enter a file name ")
if file.endswith('.docx'):
    print("It's a word document")
if file.endswith('.xlsx'):
    print("It's an Excel file")
if file.endswith('.jpg') or file.endswith('.png'):
    print("It's an image file")
# else:
#     print("No supported file")