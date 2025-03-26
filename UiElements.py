def calc():
  calci = Sys.Process("Microsoft.WindowsCalculator", 2).UIAObject("Calculator").UIAObject("NavView").UIAObject("LandmarkTarget").UIAObject("Number_pad")
  buttons = calci.FindAllChildren("ClassName","Button",10)
