import pyinputplus as pyip
import csv

def saveToCSV(fileName:str,data:list[list],subjectNum:int) -> bool:
    fileName += ".csv"
    subject = [f"科目{i+1}" for i in range(subjectNum)]
    fields = ["姓名"]
    fields.extend(subject)
    with open(fileName,mode = 'w',encoding = 'utf-8',newline='') as file:
        try:
            writer = csv.writer(file)
            # fields = None
            writer.writerow(fields)
            writer.writerows(data)
        except:
            return False
        else:
            return True
