import os
from win32com import client

old_folder = 'D:\\folder_of_doc\\'
new_folder = 'D:\\folder_of_docx\\'

files = os.listdir(old_folder)

for file in files:
    old_path = os.path.join(old_folder, file)
    new_path = os.path.join(new_folder, file + 'x')
    w = client.Dispatch('Word.Application')
    doc = w.Documents.Open(old_path)
    doc.SaveAs(new_path, 16)
