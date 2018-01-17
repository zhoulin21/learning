def printInfo():
    print("="*30)
    print("  学生管理系统")
    print("1.添加学生信息\n2.修改学生信息\n3.删除学生信息\n4.显示全部学生信息\n5.退出")
    print("=" * 30)
printInfo()
studentInfo = []
while True:
    k = input("请输入相应数字进行功能选择")
    if k == "1":
        stuAdd = {}
        addName = input("输入添加学生姓名 ")
        addPhone = input("输入添加学生联系方式 ")
        addGrade = input("输入添加学生分数 ")
        stuAdd["name"] = addName
        stuAdd["phone"] = addPhone
        stuAdd["grade"] = addGrade
        studentInfo.append(stuAdd)
    elif k == "2":
        stuId=int(input("输入修改学生序号"))
        newName=input("修改名字")
        newPhone=input("修改修改联系方式")
        newGrade=input("修改分数")
        studentInfo[stuId-1]["name"] = newName
        studentInfo[stuId-1]["phone"] = newPhone
        studentInfo[stuId-1]["grade"] = newGrade
    elif k == "3":
        sId = int(input("输入删除学生序号"))
        del studentInfo[sId-1]

    elif k == "4":
        print("学生信息")
        print("序号    名字    电话    分数")
        i=1
        for tempInfo in studentInfo:
            print("%d  %s  %s  %s" %(i,tempInfo["name"],tempInfo["phone"],tempInfo["grade"]))
            i = i+1



























