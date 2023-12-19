import random
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
def saveToCSV(fileName:str,data:list[list]) -> None:
    fileName += ".csv"
    with open(fileName,mode = 'w',encoding = 'utf-8',newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


if __name__ == "__main__":
    stuNum:int = pyip.inputInt("請輸入學生人數(1~50)：",min = 1,max = 50) 
    scoreNum:int = pyip.inputInt("請輸入科目數(1~7)：",min = 1,max = 7)
    students:list[list] = getStudents(stuNum,scoreNum) 
    fileName = pyip.inputFilename("請輸入檔案名稱(不用輸入副檔名稱)：")
    saveToCSV(fileName=fileName,data=students)