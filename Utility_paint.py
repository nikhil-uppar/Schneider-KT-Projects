#Name: Nikhil Uppar
#description: Opening the MSPaint
#parameters:None
def open_paint():
  TestedApps.MSPaint.Run()
  choose_template = Sys.Process("Microsoft.MSPaint").UIAObject("Paint_3D").UIAObject("New")
  choose_template.Click()
  select_brush()
  Writing_pad()
####################################################################################################################################################  
#Name:Nikhil Uppar
#description:Selection of Brushes 
#Partameters: Brush
def select_brush():
  brush =Sys.Process("Microsoft.MSPaint").UIAObject("Paint_3D").UIAObject("Brushes").UIAObject("PrimarySidebar").UIAObject("ScrollViewer").UIAObject("Marker")
  brush.Click()
######################################################################################################################################################  
  
#Name:Nikhil Uppar
#description:Selection of Brushes 
#Partameters: InteractorFocusWrapper and ZoomInteractor

def Writing_pad():
  W_pad = Sys.Process("Microsoft.MSPaint").UIAObject("Paint_3D").UIAObject("InteractorFocusWrapper").UIAObject("ZoomInteractor")
  W_pad.Drag(762,414,200,0)
  W_pad.Drag(962,414,0,200)
  W_pad.Drag(962,614,-200,0)
  W_pad.Drag(762,614,0,-200)

 

  