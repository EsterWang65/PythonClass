
import pyinputplus as pyip
import tools



if __name__ == "__main__":
    stuNum:int = pyip.inputInt("請輸入學生的人數(1~50)：",min = 1,max = 50)
    students = tools.getStudents(stuNum)
    fileName = pyip.inputFilename("請輸入檔案名稱(不用輸入副檔名稱)：")
    tools.save_to_csv(students,fileName)