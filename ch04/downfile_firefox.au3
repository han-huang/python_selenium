;ControlFocus("title","text",controlID) Edit1=Edit instance 1
ControlFocus("開啟中: selenium-3.11.0.tar.gz", "","")

; Wait 10 seconds for the Upload window to appear
;WinWait("[CLASS:#MozillaDialogClass]","",1)

; Set the File name text on the Edit field
;ControlSetText("上傳檔案", "", "Edit1", "C:\Users\Han\selenium_test\ch04\upfile.txt")
;Sleep(1000)

; Click on the Open button
;ControlClick("開啟中: selenium-3.11.0.tar.gz", "","Button1");
Send("{TAB}")
Send("{TAB}")
Send("{TAB}")
Send("{ENTER}")