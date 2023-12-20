import random

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

    return students