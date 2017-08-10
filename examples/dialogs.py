#Dialogs.py
#imports
from AGK.misc import dialog
from AGK.mainframe import window

#main
w = window.window("dialog example")
w.show()
dialog.dialog("This is some text.",type=2)
dlg = dialog.EntryDialog("Enter something.")
dialog.dialog("You entered " + dlg.string)
