import openpyxl as op

wb=op.Workbook()

print(wb)

wb.save("openpyxl_test.xlsx")
ws=wb.active

print(ws)



# 엑셀 실행
import win32com.client
excel = win32com.client.Dispatch("Excel.Application")      # 엑셀 프로그램 실행
excel.Visible = True                                       # 앞으로 실행과정을 보이게

wb = excel.Workbooks.Add()                                 # 엑셀 프로그램에 Workbook 추가 (객체 설정)
ws = wb.Worksheets("sheet1")                               # Worksheet 설정


# wb = excel.Workbooks.Open(r"C:\Users\Desktop\data.xlsx") # 있는 엑셀 파일 불러오기


#셀 row, col 값 지정하여 값넣기(Range("A1")과 동일 함)
ws.cells(1,1).Value = "win32com excel test1"

#ragne로 값 넣기(Cell(1,2)와 동일함)
ws.Range("A2").Value = "win32com excel test2"

#range로 다중범위 지정해서 값 넣기1
ws.Range("A3:C3").Value = "win32com excel test3"

#range로 다중범위 지정해서 값 넣기2(위 코드와 동일 표현)
ws.Range(ws.cells(3,1), ws.cells(3,3)).Value = "win32com excel test3"

#엑셀의 자동 채우기 기능 - Autofill() 함수
ws.Range('A1:A3').AutoFill(ws.Range("A1:A10"))

ws.Range("A1:A10").Copy() # "A1:A10" 데이터 복사하기
ws.Range("B1").Select() # 붙여넣기 할 위치 선택
ws.Paste() #붙여넣기 실행

wb.Save()  #파일저장하기
wb.SaveAs(r"C:\Users\Desktop\VS CODE\Project\17. win32com\data.xlsx") #지정위치에 파일저장하기
excel.Quit() #엑셀닫기






import pyautogui

print(pyautogui.size())       # 현재 사용하는 모니터의 해상도 출력
print(pyautogui.position())   # 현재 마우스 커서의 위치 출력
pyautogui.mouseInfo()         # 마우스 현재 위치 & RGB 색상 실시간으로 얻기

# 절대 좌표로 이동
pyautogui.moveTo(100, 100)                 # 100, 100 위치로 즉시 이동
pyautogui.moveTo(200, 200, duration=0.5)   # 200, 200 위치로 0.5초간 이동


# 상대 좌표로 이동
pyautogui.move(100, 100, duration=1)    # 현재 위치 기준으로 100, 100만큼 1초간 이동


# 마우스 클릭
pyautogui.click()  # 해당위치에서 단순클릭
pyautogui.click(200, 200)    # 해당 위치로 가서 클릭
pyautogui.click(clicks=2, interval=0.2, button='right')        # 해당 위치에서 총 2번 클릭, 클릭간 시간은 0.2초, 마우스 오른쪽버튼


# 1초간 400, 400 위치로 이동 후, 절대 좌표 500, 500으로 2초간 드래그
pyautogui.click(400, 400, duration=1)
pyautogui.dragTo(500, 500, 2, button='left')

# 현재 마우스 위치 기준으로 300, 300 범위만큼 왼쪽 버튼으로 드래그
pyautogui.dragRel(300, 300, 2, button='left')

pyautogui.scroll(-100) # 스크롤 내리기
pyautogui.scroll(100)  # 스크롤 올리기