;ControlFocus("title","text",controlID) Edit1=Edit instance 1
ControlFocus("開啟", "","Edit1")

; Wait 10 seconds for the Upload window to appear
WinWait("[CLASS:#32770]","",10)

; Set the File name text on the Edit field
ControlSetText("開啟", "", "Edit1", "C:\Users\Han\selenium_test\ch04\upfile.txt")
Sleep(1000)

; Click on the Open button
ControlClick("開啟", "","Button1");
