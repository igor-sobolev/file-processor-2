#from guizero import App, PushButton, TextBox
from docx_tools import compose_docx
from directories import find_files

# def do_nothing():
#     print(int(a.value) + int(b.value))

# app = App(title="Keypad example", width=500, height=190, layout="grid")
# processButton = PushButton(app, command=do_nothing, text="Add", grid=[0,0])
# a = TextBox(app, text="0", grid=[1,1])
# b = TextBox(app, text="0", grid=[1,0])

# app.display()

path_to_root = '/home/igor/workspace/awtg/documents_all/'
final_path = '/home/igor/workspace/awtg/processed/'

files_by_tech = find_files(path_to_root)

# for tech_plus_test in files_by_tech.keys():
#     compose_docx(final_path + str(tech_plus_test) + '.docx',
#         files_by_tech[tech_plus_test],
#         tech_plus_test)

compose_docx(final_path + str('2g') + '.docx', files_by_tech['2g'], '2g')
