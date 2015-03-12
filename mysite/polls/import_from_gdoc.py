import gspread
import local

email = local.email
password = local.password

# Login with your Google account
gc = gspread.login(email, password)

# Open a worksheet from spreadsheet with one shot
wks = gc.open("Kombucha Tasting HyperCube").sheet1

wks.update_acell('F9', "it's down there somewhere, let me take another look.")

# Fetch a cell range
#cell_list = wks.range('A1:B7')