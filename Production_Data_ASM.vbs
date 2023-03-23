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
		.Password = "INIT11"
		.Language = "KO"
		.system = "BW: Produktion"
		.systemnumber = "00"
		.ApplicationServer = "165.244.245.216"
		.SAProuter = ""
		.LogOn 0, True
	End with

xl.Run("BExAnalyzer.xla!sapBEXinitConnection")

Set xlBook = xl.Workbooks.Open("D:\Work\00_Production\02_Production_Data\2022\OEE\OEE_ASM.xlsm", 0, False)

xl.Application.run "Refresh_the_Data"
xl.Application.run "Paste_Title"
xl.Application.run "Paste_QuerySheet"
xlBook.save
' xl.ActiveWindow.close True

Set xlBook = xl.Workbooks.Open("D:\Work\00_Production\02_Production_Data\2022\Scrap_Rate\Scrap_Rate_ASM_(2022).xlsm", 0, False)
xl.Application.run "Delete_File2"
xl.Application.run "Show_Data"
xl.Application.run "Show_Message"
xlBook.save
' xl.ActiveWindow.close True
' xl.Quit

Set xlBook = Nothing
Set xl = Nothing


