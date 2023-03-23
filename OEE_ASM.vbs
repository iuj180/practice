' 전역변수 지정
Dim xl
Dim myConnection
Dim xlBook
 
' 엑셀 실행
set xl = createobject("Excel.Application")
 
' 엑셀 Visible 설정
xl.Visible = true
	 
' BEX Analyzer Addin xla file 실행
xl.Workbooks.Open("C:\Program Files (x86)\Common Files\SAP Shared\BW\BExAnalyzer.xla")

' BEX Analyzer 안에 SetStart 매크로 실행
xl.Run ("BExAnalyzer.xla!SetStart")
 
' BW 로그인 정보 설정 (BEX Analyzer 안에 sapBEXgetConnection 매크로 사용)
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

' BW 서버 접속
' xl.Run("BExAnalyzer.xla!sapBEXinitConnection")

' 데이터 집계 파일 실행
Set xlBook = xl.Workbooks.Open("D:\Work\00_Production\02_Production_Data\2022\OEE\OEE_ASM.xlsm", 0, False)

' 데이터 새로고침 매크로 실행 (엑셀 모듈안에 매크로 사용)
xl.Application.run "Refresh_the_Data"

' 쿼리 조회 데이터 Title 수정
xl.Application.run "Paste_Title"

' 쿼리 조회 데이터 구분자 업데이트
xl.Application.run "Paste_QuerySheet"

' 엑셀 저장 및 활성화 파일 닫기
xlBook.save

' 쿼리 조회 데이터 구분자 업데이트
xl.Application.run "Show_Message"


' xl.ActiveWindow.close True
  
' ' 엑셀 프로그램 닫기
' xl.Quit
  
'할당된 메모리 정리하기  
Set xlBook = Nothing
Set xl = Nothing