import gspread
from oauth2client.service_account import ServiceAccountCredentials
import nowTime

def writeGoogleSpreadSheet():
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name("matsuilab-counter-9af569808183.json", scope)
    gc = gspread.authorize(credentials)
    wks = gc.open("demo20180922").sheet1

    rf = open("nowRowNumber.txt")
    rf_list = rf.readlines()
    rf.close()
    if len(rf_list) >= 2:
        rf_list[-1] = rf_list[-1][:-1]
    print(rf_list)
    rowCount = int(float("".join(rf_list)))
    
    wf = open("nowRowNumber.txt", mode = "w")
    wf.write(str(rowCount + 1) + "\n")
    wf.close()
    
    strRowCount = str(rowCount)
    
    #write spreadsheet
    wks.update_acell("A" + strRowCount, nowTime.nowTime())
    wks.update_acell("B" + strRowCount, "1")
