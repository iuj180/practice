Sub Show_Data()
    
    Dim rotEntry, guiApp, connection, session
    Dim i As Integer
    Dim k As Integer
    
    Call Delete_File
            
    'SAP 연결 부분
    Set rotEntry = GetObject("SAPGUI")
    Set guiApp = rotEntry.GetScriptingEngine
    Set connection = guiApp.Children(0)
    Set session = connection.Children(0)
    
    'ZPPR3028 실행
    session.findById("wnd[0]").resizeWorkingPane 193, 32, False
    session.findById("wnd[0]/tbar[0]/okcd").Text = "/nzcor0910"
    session.findById("wnd[0]").sendVKey 0

    '관리회계영역, 회계연도, 기간시작, 종료기간, 계획버전 입력
    session.findById("wnd[0]/usr/ctxt$1KOKRE").Text = Range("C4")
    session.findById("wnd[0]/usr/txt$1GJAHR").Text = Range("C5")
    session.findById("wnd[0]/usr/ctxt$1PERIV").Text = Range("C6")
    session.findById("wnd[0]/usr/ctxt$1PERIB").Text = Range("C7")
    session.findById("wnd[0]/usr/ctxt$1VERP").Text = Range("C8")
    session.findById("wnd[0]/usr/ctxt$1VERP").SetFocus
    session.findById("wnd[0]/usr/ctxt$1VERP").caretPosition = 1
    
    '코스트센터 복사
    Sheets("실행화면").Select
    Range("C9").Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.Copy
    
    '코스트센터 다중선택 버튼 클릭
    session.findById("wnd[0]/usr/btn%__1KOSET_%_APP_%-VALU_PUSH").press
    session.findById("wnd[1]/tbar[0]/btn[24]").press
    session.findById("wnd[1]/tbar[0]/btn[8]").press
    
    '계정 복사
    Sheets("실행화면").Select
    Range("C29").Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.Copy
    
    '계정 다중선택 버튼 클릭
    session.findById("wnd[0]/usr/btn%__1KSTAR_%_APP_%-VALU_PUSH").press
    session.findById("wnd[1]/tbar[0]/btn[24]").press
    session.findById("wnd[1]/tbar[0]/btn[8]").press
    
    '조회
    session.findById("wnd[0]/tbar[1]/btn[8]").press
    
    '리포트 호출
    session.findById("wnd[0]/usr/lbl[52,7]").SetFocus
    session.findById("wnd[0]/usr/lbl[52,7]").caretPosition = 7
    session.findById("wnd[0]").sendVKey 7
    session.findById("wnd[0]/shellcont/shell/shellcont[2]/shell").hierarchyHeaderWidth = 374

    session.findById("wnd[0]/usr/lbl[36,9]").SetFocus
    session.findById("wnd[0]/usr/lbl[36,9]").caretPosition = 0
    session.findById("wnd[0]").sendVKey 7

    session.findById("wnd[1]/usr/lbl[1,2]").SetFocus
    session.findById("wnd[1]/usr/lbl[1,2]").caretPosition = 20
    session.findById("wnd[1]").sendVKey 2
    
    '첫번째 레아아웃 선택
    session.findById("wnd[0]/tbar[1]/btn[33]").press
    session.findById("wnd[1]/usr/ssubD0500_SUBSCREEN:SAPLSLVC_DIALOG:0501/cntlG51_CONTAINER/shellcont/shell").currentCellColumn = "TEXT"
    session.findById("wnd[1]/usr/ssubD0500_SUBSCREEN:SAPLSLVC_DIALOG:0501/cntlG51_CONTAINER/shellcont/shell").firstVisibleRow = 0
    session.findById("wnd[1]/usr/ssubD0500_SUBSCREEN:SAPLSLVC_DIALOG:0501/cntlG51_CONTAINER/shellcont/shell").selectedRows = "0"
    session.findById("wnd[1]/usr/ssubD0500_SUBSCREEN:SAPLSLVC_DIALOG:0501/cntlG51_CONTAINER/shellcont/shell").clickCurrentCell
    session.findById("wnd[0]/tbar[1]/btn[45]").press
    
    '파일 다운로드
    session.findById("wnd[0]/tbar[1]/btn[45]").press
    session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[1,0]").Select
    session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[1,0]").SetFocus
    session.findById("wnd[1]/tbar[0]/btn[0]").press
    session.findById("wnd[1]/usr/ctxtDY_PATH").Text = Range("C2")
    session.findById("wnd[1]/usr/ctxtDY_FILENAME").Text = Range("C3")
    session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 8
    session.findById("wnd[1]/tbar[0]/btn[0]").press
    
    Call Totalizing
    
End Sub







Sub Paste_Data()

    Dim 대상폴더 As String
    Dim 파일 As String
    Dim 통합시트 As Worksheet
    Dim 작업파일 As Workbook
    Dim 대상범위 As Range
    Dim 복사위치 As Range
    
    대상폴더 = ThisWorkbook.Path & "\"
    파일 = Dir(대상폴더 & Sheets("다운로드").Range("C3"))
    
    Application.ScreenUpdating = False
        
    Set 통합시트 = ThisWorkbook.Worksheets("Data")
        
    '파일열기
    Set 작업파일 = Workbooks.Open(Filename:=대상폴더 & 파일)
    Columns(1).Delete
    
    Set 대상범위 = 작업파일.Worksheets(1).UsedRange
                
    With 대상범위
        Set 대상범위 = .Offset(2).Resize(.Rows.Count - 2)
    End With
     
    Set 복사위치 = 통합시트.Cells(Rows.Count, "EM").End(xlUp).Offset(1)
        
    대상범위.Copy 복사위치
    작업파일.Close savechanges:=False
    파일 = Dir()
    
    '생산월 복사 붙여넣기
    Sheets("다운로드").Select
    Range("C7").Select
    Selection.Copy
    Sheets("Data").Select
    통합시트.Cells(Rows.Count, "EL").End(xlUp).Offset(1, 1).Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False
        
    Sheets("Data").Select
    Range(통합시트.Cells(Rows.Count, "B").End(xlUp), 통합시트.Cells(Rows.Count, "EL").End(xlUp)).Offset(-1).Select
    Selection.Copy
    통합시트.Cells(Rows.Count, "EL").End(xlUp).Offset(0, 1).Select
    Range(Selection, Selection.End(xlDown)).Offset(0, -141).Select
    ActiveSheet.Paste
       
    Calculate
    ActiveWorkbook.RefreshAll
    Sheets("월별-스크랩율").Select
    
    Application.ScreenUpdating = True

End Sub




Sub Delete_Sheet()

    Dim 시트 As Worksheet

    Application.DisplayAlerts = False
    
    For Each 시트 In ThisWorkbook.Worksheets
        
        If 시트.Name <> "기준" And 시트.Name <> "실적" And 시트.Name <> "정리" And 시트.Name <> "실행화면" Then
            시트.Delete
        End If
        
    Next 시트

Application.DisplayAlerts = True

End Sub





Sub Delete_Data()

    Dim 통합시트 As Worksheet
    Dim rngCnt As Integer
        
    On Error Resume Next
    
    Set 통합시트 = ThisWorkbook.Worksheets("Data")
    
    Sheets("Data").Select
    Columns("EM:EM").Select
    Selection.Replace What:=Sheets("다운로드").Range("c7"), Replacement:="", LookAt:=xlPart, _
        SearchOrder:=xlByColumns, MatchCase:=False, SearchFormat:=False, _
        ReplaceFormat:=False
        
    통합시트.Cells(Rows.Count, "EM").End(xlUp).Offset(0, -1).Select
    Range(Selection, Selection.End(xlDown)).Offset(1, 0).Select
    rngCnt = Selection.Rows.Count
    
    If rngCnt = 1 Then
    Else
        Selection.EntireRow.Delete
    End If
        
    Sheets("다운로드").Select
    
    
End Sub





Sub Show_Message()

    MsgBox "실적 조회 완료"
    
End Sub
