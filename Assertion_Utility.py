#Name: Nikhil Uppar
#Description:Opens the Notepad
#Parameters: None
def launch_notepad():
  TestedApps.Notepad.Run()
##################################################################################################################################
#Name: Nikhil Uppar
#Description: Writes text in the Notepad
#Parameters: Notepad text box and text editor
def write_text():
  Edit = Sys.Process("Notepad").Window("Notepad", "Demo.txt - Notepad", 1).Window("NotepadTextBox", "", 1).Window("RichEditD2DPT", "", 1)
  Edit.SetText("Hello")
##################################################################################################################################
#Name: Nikhil Uppar
#Description: To verify the text in the editor is as same as enetered text 
#Parameters: Editor 
def Check():
  Editor = Sys.Process("Notepad").Window("Notepad", "*Demo.txt - Notepad", 1).Window("NotepadTextBox", "", 1).Window("RichEditD2DPT", "", 1)
  actual_text = Editor.wText
  expected_text = "Hello"

  if actual_text == expected_text:   
    Log.Message("The text is confirmed")
  else:
    Log.Error("The text is Different")
##################################################################################################################################
#Name: Nikhil Uppar
#Description: To verify the name of the file is as same as enetered name by user 
#Parameters: Title bar 


def title():
  main_title = Sys.Process("Notepad").Window("Notepad", "*Demo.txt - Notepad", 1).Window("Windows.UI.Composition.DesktopWindowContentBridge", "DesktopWindowXamlSource", 3)
  if main_title == "Demo.txt":
    Log.Message("The title is Demo.txt")
launch_notepad()
write_text()
Check()
