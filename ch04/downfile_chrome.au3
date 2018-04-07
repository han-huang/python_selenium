#include <AutoItConstants.au3>

;ControlFocus("title","text",controlID) Edit1=Edit instance 1
ControlFocus("另存新檔", "","Edit1")

; Wait 2 seconds for the window to appear
WinWait("[CLASS:#32770]","",2)

;ControlFocus("title","text",controlID) Edit1=Edit instance 1
;ControlFocus("另存新檔", "","ToolbarWindow324")
;MouseClick($MOUSE_CLICK_LEFT)
;Send("^{A}")
;Send("{DEL}")

;FileSaveDialog('另存新檔',@DesktopDir, 'GZ 檔案 (*.gz)')

; Set the File name text on the Edit field
; ControlSetText("另存新檔", "", "ToolbarWindow324", "C:\Users\Han\selenium_test\")
Global $sText
$sText = ControlGetText("另存新檔", "", "Edit1")
ConsoleWrite($sText & @CRLF)
ConsoleWrite(@DesktopDir & "\" & $sText & @CRLF)
ControlSetText("另存新檔", "", "Edit1", @DesktopDir & "\" & $sText)
Sleep(1000)

; Click on the Open button
ControlClick("另存新檔", "","Button2");