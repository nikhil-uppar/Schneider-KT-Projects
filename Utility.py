#Name:Nikhil uppar
#Description:opening the calculator
#Parameters:
def calculator():
  TestedApps.WindowsCalculator.Run()
#########################################################################################################################################################################
#Name:Nikhil uppar
#Description:closing the calculator
#def cal_close():
#   calc= Sys.Process("Microsoft.WindowsCalculator")
#   calc.Close()
#################################################################################################################################################
#name:Nikhil Uppar
#description:Addition of numbers 
#parameters:Children of Notepad and children of Operators
def numbers_add(param):
  
  number_pad = Sys.Process("Microsoft.WindowsCalculator",2).UIAObject("Calculator").UIAObject("NavView").UIAObject("LandmarkTarget").UIAObject("Number_pad")
  num_button = number_pad.FindAllChildren("ClassName","Button",10)
  for button in num_button:
    if button.ObjectIdentifier == param:
      button.Click()
      Log.Message(f'{button.ObjectIdentifier} is clicked')
      break
    else:
      Log.Warning("Button not clicked") 
       
def std_operators(para):
  operators = Sys.Process("Microsoft.WindowsCalculator",2).UIAObject("Calculator").UIAObject("NavView").UIAObject("LandmarkTarget").UIAObject("Standard_operators")
  op_button = operators.FindAllChildren("ClassName","Button",4)  
  for btn in op_button:
    if btn.AutomationId == para:
      btn.Click()
      Log.Message(f"{btn.AutomationId} is clicked")
      break
    else:
      Log.Warning("Button not clicked")
      
def some():
  calculator()
  numbers_add("One")
  numbers_add("Seven")
  std_operators("plusButton")
  numbers_add("Three")
  std_operators("equalButton")  
   
#def jasadfascx():
#  for btn in op_button:
#    #Log.Message(f'{btn.ObejectIdentifier}') AutomationId
#    if "plus" in btn.AutomationId:
#      btn.Click()
#      Log.Message(f'{btn.ObjectIdentifier} is clicked')
#      break

      
  