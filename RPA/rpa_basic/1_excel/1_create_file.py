from openpyxl import Workbook
wb = Workbook()  # 새 워크북 생성
ws = wb.active  # 현재 활성화된 워크시트를 가져옴
ws.title = "NadoSheet"  # 워크시트의 이름을 변경
wb.save("sample.xlsx")  # 파일 저장
wb.close()