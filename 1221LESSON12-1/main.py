import pyinputplus as pyip
from tools import getStudents,saveToCSV


if __name__ == "__main__":
    stuNum:int = pyip.inputInt("請輸入學生人數(1~50)：",min = 1,max = 50)
    print(stuNum)
    scoreNum:int = pyip.inputInt("請輸入科目數(1~7)：",min = 1,max = 7)
    print(scoreNum)
    students:list[list] = getStudents(stuNum,scoreNum)
    print(students) 
    fileName = pyip.inputFilename("請輸入檔案名稱(不用輸入副檔名稱)：")
    print(fileName)
    if saveToCSV(fileName=fileName,data=students,subjectNum=scoreNum):
        print("存檔成功")
    else:
        print("存檔失敗")