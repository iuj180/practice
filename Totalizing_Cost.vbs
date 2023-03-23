Dim xl
Dim myConnection
Dim xlBook
 

set xl = createobject("Excel.Application")
xl.Visible = true

Set xlBook = xl.Workbooks.Open("D:\Work\00_Production\02_Production_Data\2022\Totalizing_Cost_2022_ZCOR0910_Rev00.xlsm", 0, False)
xl.Application.run "Show_Data"
xl.Application.run "Show_Data"
xlBook.save
' xl.ActiveWindow.close True
' xl.Quit

Set xlBook = Nothing
Set xl = Nothing