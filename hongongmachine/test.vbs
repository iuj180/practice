Dim wsh
Set wsh = WScript.createObject("WScript.Shell")
wsh.Run "calc"	' 계산기 실행
WScript.Sleep 2000
wsh.SendKeys "1{+}2"	' 1+2 입력
WScript.Sleep 500
wsh.SendKeys "*3"	' *3 입력
WScript.Sleep 500
wsh.SendKeys "{enter}"	' 엔터 입력

set wsh = nothing