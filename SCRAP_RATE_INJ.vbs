Dim xl
Dim myConnection
Dim xlBook
 

set xl = createobject("Excel.Application")
xl.Visible = true

Set xlBook = xl.Workbooks.Open("D:\Work\00_Production\02_Production_Data\2022\Scrap_Rate\Scrap_Rate_INJ_(2022).xlsm", 0, False)
xl.Application.run "Delete_File2"
xl.Application.run "Show_Data"
xlBook.save
' xl.ActiveWindow.close True
' xl.Quit

Set xlBook = Nothing
Set xl = Nothing