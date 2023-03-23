Dim xl
Dim myConnection
Dim xlBook
 
set xl = createobject("Excel.Application")
xl.Visible = true
	 

xl.Workbooks.Open("C:\Program Files (x86)\Common Files\SAP Shared\BW\BExAnalyzer.xla")
xl.Run ("BExAnalyzer.xla!SetStart")
 
Set myConnection = xl.Run("BExAnalyzer.xla!sapBEXgetConnection")
With myConnection
	.client = "100"
	.User = "C077701"
	.Password = "init11"
	.Language = "KO"
	.systemnumber = "00"
	.ApplicationServer = "165.244.245.216"
	.SAProuter = ""
	.Logon 0, True
end with

' xl.Run("BExAnalyzer.xla!sapBEXinitConnection")

Set xlBook = xl.Workbooks.Open("D:\Work\00_Production\02_Production_Data\2022\OEE\OEE_ASM.xlsm", 0, False)
xl.Application.run "Refresh_the_Data"
xl.Application.run "Paste_Title"
xl.Application.run "Paste_QuerySheet"
xlBook.save
' xl.ActiveWindow.close True

Set xlBook = xl.Workbooks.Open("D:\Work\00_Production\02_Production_Data\2022\OEE\OEE_PRE.xlsm", 0, False)
xl.Application.run "Refresh_the_Data"
xl.Application.run "Paste_Title"
xl.Application.run "Paste_QuerySheet"
xlBook.save
' xl.ActiveWindow.close True

Set xlBook = xl.Workbooks.Open("D:\Work\00_Production\02_Production_Data\2022\OEE\OEE_INJ.xlsm", 0, False)
xl.Application.run "Refresh_the_Data"
xl.Application.run "Paste_Title"
xl.Application.run "Paste_QuerySheet"
xlBook.save
xl.Application.run "Show_Message"

' xl.ActiveWindow.close True  
' xl.Quit

Set xlBook = Nothing
Set xl = Nothing