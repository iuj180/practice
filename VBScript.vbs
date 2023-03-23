' Creating an Excel Object 
Set obj = createobject("Excel.Application") 
' Making an Excel Object visible 
obj.visible=True 
' Adding a Workbook to Excel Sheet 
Set obj1 = obj.Workbooks.Add() 
' Setting a value in the first-row first column 
obj1.Cells(1,1).Value="Hello!!"
' Saving a Workbook 
obj1.SaveAs "d:\ewexcelfile.xls"
' Closing a Workbook 
obj1.Close
' Exit from Excel Application  
obj.Quit 
' Releasing Workbook object 
Set obj1=Nothing 
' Releasing Excel object
Set obj=Nothing 



' ' Creating an Excel Object 
' Set obj = createobject("Excel.Application") 
' ' Making an Excel Object visible 
' obj.visible=True 
' ' Opening an Excel file 
' Set obj1 = obj.Workbooks.open("C:\ewexcelfile.xls") 
' ' Referring Sheet1 of excel file 
' Set obj2=obj1.Worksheets("Sheet1") 
' ' Value from the specified cell will be read and shown Msgbox 
' obj2.Cells(2,2).Value 
' ' Closing a Workbook 
' obj1.Close 
' ' Exit from Excel Application 
' obj.Quit 
' ' Releasing Workbook object 
' Set obj1=Nothing 
' ' Releasing Worksheet object 
' Set obj2 = Nothing
' ' Releasing Excel object 
' Set obj=Nothing 




' ' Creating an Excel Object 
' Set obj = createobject(“Excel.Application”) 
' ' Making an Excel Object visible 
' obj.visible=True 
' ' Opening an Excel file 
' Set obj1 = obj.Workbooks.open("C:\ewexcelfile.xls") 
' ' Referring Sheet1 of excel file 
' Set obj2=obj1.Worksheets("Sheet1") 
' ' Deleting 4th row from Sheet1 
' obj2.Rows("4:4").Delete 
' ' Saving the file with the changes 
' obj1.Save()
' ' Closing a Workbook  
' obj1.Close
' ' Exit from Excel Application  
' obj.Quit 
' ' Releasing Workbook object 
' Set obj1=Nothing 
' ' Releasing Worksheet object
' Set obj2 = Nothing 



' ' Creating an Excel Object 
' Set obj = createobject("Excel.Application") 
' ' Making an Excel Object visible 
' obj.visible=True 
' ' Opening an Excel file 
' Set obj1 = obj.Workbooks.open("C:\ewexcelfile.xls") 
' ' Adding a new sheet in the excel file 
' Set obj2=obj1.sheets.Add 
' ' Assigning a name to the sheet created above 
' obj2.name="Sheet1" 
' ' Accessing Sheet1 
' Set obj3= obj1.Sheets("Sheet1") 
' ' Deleting a sheet from an excel file 
' obj3.Delete
' ' Closing a Workbook  
' obj1.Close
' ' Exit from Excel Application  
' obj.Quit 
' ' Releasing Workbook object 
' Set obj1=Nothing 
' ' Releasing Worksheet object 
' Set obj2 = Nothing 
' ' Releasing Worksheet object 
' Set obj3 = Nothing 
' ' Releasing Excel object
' Set obj=Nothing 




' ' Creating an Excel Object 
' Set obj = createobject("Excel.Application") 
' ' Making an Excel Object visible 
' obj.visible=True 
' ' Opening an Excel file1 
' Set obj1 = obj.Workbooks.open("C:\ewexcelfile.xls") 
' ' Opening an Excel file2 
' Set obj2 = obj.Workbooks.open("C:\ewexcelfile1.xls") 
' ' Copying from an Excel File1 
' obj1.Worksheets("Sheet1").usedrange.copy 
' ' Pasting in Excel File2 
' obj2.Worksheets("Sheet1").usedrange.pastespecial 
' ' Saving Workbook1 
' obj1.Save 
' ' Saving Workbook2 
' obj2.Save 
' ' Closing a Workbook 
' obj1.Close 
' ' Exit from Excel Application 
' obj.Quit 
' ' Releasing Workbook1 object 
' Set obj1=Nothing 
' ' Releasing Workbook2 object 
' Set obj2 = Nothing 
' ' Releasing Excel object
' Set obj=Nothing 