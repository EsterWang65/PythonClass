import random  #注意記得匯入module
import pyinputplus as pyip
import csv

def getStudents(stuNum:int,scoreNum:int) -> list[list]:
    '''
    參數：stuNum代表學生人數；\n
    參數：scoreNum代表科目數。
    '''

    with open("names.txt","r",encoding = "utf-8") as f:
        name:str = f.read()
    nameList:list[str] = name.split('\n')

    students:list[list] = []
    names:list[str] = random.choices(nameList,k = stuNum)
    for name in names:
        stu:list[int|str] = []
        stu.append(name)
        for score in range(scoreNum):
            stu.append(random.randint(40,100))
        students.append(stu)

    return(students)

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

