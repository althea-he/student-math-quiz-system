import random
import re

student_ids = {}
all_ids = [i for i in range(100001, 1000000)]  # 生成所有学生id列表


def create_id():
    global all_ids
    # 取出学生id
    std_id = all_ids[0]
    # 删除id
    all_ids.remove(std_id)
    return std_id


def cale():
    # 生成两个随机小于100的数字
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    # 随机挑选加减乘除
    tmp = random.randint(0, 3)
    label = ["+", "-", "*", "/"][tmp]
    if label == "/":
        # 说明随机到了除法，此时需要保证能整除
        while True:
            if num2 == 0:  # 除数不可为零
                num2 = 1
            elif ((num1 % num2) != 0) or (num1 < num2):  # 取余数不为零,说明不是整除
                num1 = random.randint(1, 100)
                num2 = random.randint(1, 100)
                # 保证除数小于被除数，这样才有机会整除
                while num2 > num1:
                    num1 = random.randint(1, 100)
                    num2 = random.randint(1, 100)
                continue
            else:
                break
    # 计算结果
    if tmp == 0:
        res = num1 + num2
        while res >= 100:
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            res = num1 + num2
    elif tmp == 1:
        res = num1 - num2
        while res < 0:
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            res = num1 - num2
    elif tmp == 2:
        res = num1 * num2
        while res >= 100:
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            res = num1 * num2
    else:
        res = int(float(num1 / num2))
    print("请算术题：%s %s %s的结果" % (num1, label, num2))
    user_answer = input("请输入算术答案：")
    flag = 0
    if tmp == 3:
        try:
            user_answer = int(float(user_answer))
            if user_answer == res:
                print("答案正确!")
                flag = 1
            else:
                print("答案错误!")
        except Exception as e:
            flag = 0
            print("答案错误!")
    else:
        try:
            user_answer = int(user_answer)
            if user_answer == res:
                print("答案正确!")
                flag = 1
            else:
                print("答案错误!")
        except Exception as e:
            flag = 0
            print("答案错误!")

    return flag


# 校验字符串是否有特殊字符函数
def test_str(name):
    # 使用re模块
    res = re.findall(r"\W", str(name))
    if res != None:
        # 有特殊字符
        for i in res:
            if i != " ":
                return 1
        return 0
    else:
        # 没有特殊字符
        return 0


# 查询学生成绩信息
def search(name_id, search_type):
    student_info = []
    if search_type:
        try:
            with open("./record.txt", "r", encoding="utf-8") as f:
                line = f.readline()
                while line:
                    student = line.strip().split(",")
                    if name_id == student[0]:
                        student_info.append(student)
                    line = f.readline()
        except Exception as e:
            return []
    else:
        try:
            # 名字查询
            with open("./record.txt", "r", encoding="utf-8") as f:
                line = f.readline()
                while line:
                    student = line.strip().split(",")
                    if name_id == student[1]:
                        student_info.append(student)
                    line = f.readline()
        except Exception as e:
            return []
    return student_info


import os

try:
    os.remove("record.txt")
except Exception as e:
    pass
while True:
    print("----------欢迎使用小学生的算术测试系统----------")
    print("<<<<功能列表>>>>")
    print("1.算术题测试，一共十道")
    print("2.成绩记录查询")
    print("3.全部学生平均成绩")
    print("4.退出系统")
    func = input("请选择想要执行的功能：")
    if func == "1":
        name = input("请输入学生名字：")
        if test_str(name):
            print("名字中不可带有特殊字符哦！")
            continue
        try:
            int(name)
            print("名字不可为纯数字哦!")
            continue
        except Exception as e:
            pass
        # 检测该学生是否已有ID
        try:
            # 取出该学生ID
            std_id = student_ids[name]
        except Exception as e:
            # 找不到该学生信息，说明学生第一次注册使用，创建分配学生id
            std_id = create_id()
            # 储存学生信息
            student_ids[name] = std_id
        score = 0
        print("<<<<请完成如下算术题>>>>")
        for i in range(10):
            # 生成十道算术题
            integral = cale()
            score += integral
        print("测试完成，总得分为：%s" % score)
        # 将测试成绩写入record.txt中
        with open("./record.txt", "a", encoding="utf-8") as f:
            f.write("%s,%s,%s" % (std_id, name, score))
            f.write("\n")
            print("写入学生信息成功")
    elif func == "2":
        name_id = input("请输入学生名字或学生id：")
        search_type = 0
        # 判断是否是以ID查询
        try:
            int(name_id)
            search_type = 1
        except Exception as e:
            search_type = 0
        # 调用查询学生信息函数
        student_info = search(name_id, search_type)
        if student_info != []:
            total = 0
            name = ""
            print("<<<<成绩查询结果如下>>>>")
            for student in student_info:
                print("学生ID为：%s，学生名字为：%s，学生成绩为：%.2f" % (student[0], student[1], float(student[2])))
                total += float(student[2])
                name = student[1]
            print("学生：%s全部测试的平均分为：%.2f" % (name,(total/len(student_info))))
        else:
            print("目标学生信息为空！")

    elif func == "3":
        print("<<<<全部学生平均成绩结果如下>>>>")
        student_scores = {}
        # 使用try捕获异常，如果出错说明没有record.txt文件
        try:
            # 读取文件记录，遍历所有记录
            with open("./record.txt", "r", encoding="utf-8") as f:
                line = f.readline()
                while line:
                    student = line.strip().split(",")
                    std_id = student[0]
                    name = student[1]
                    score = int(student[2])
                    try:
                        student_scores[std_id]
                    except Exception as e:
                        student_scores[std_id] = []
                    if student_scores[std_id] == []:
                        student_scores[std_id] = [name, 1, score]
                    else:
                        student_scores[std_id][1] += 1
                        student_scores[std_id][2] += score
                    line = f.readline()
        except Exception as e:
            print("暂无学生成绩记录哦!")
        # print(student_scores)
        info = []
        # 计算平均分
        for std, v in student_scores.items():
            std_id = std
            name = v[0]
            number = v[1]
            total_score = v[2]
            # print("学生姓名：%s，平均成绩为：%.2f" % (name, (total_score / number)))
            info.append([name, total_score / number, std_id])
        # 使用冒泡排序，对平均成绩进行由大到小排序
        result = []
        lennum = len(info)
        for i in range(lennum):
            max_num = 0.0
            max_name = ""
            max_id = 10000000
            target = []
            for x in range(len(info)):
                # 如果成绩大于最大值时，则重置最大值
                # 如果等于最大值，则根据id大的就更大
                if float(info[x][1]) > max_num:
                    max_num = float(info[x][1])
                    max_name = info[x][0]
                    max_id = int(info[x][2])
                    target = info[x]
                elif  float(info[x][1]) == max_num and int(info[x][2]) < max_id:
                    max_num = float(info[x][1])
                    max_name = info[x][0]
                    max_id = int(info[x][2])
                    target = info[x]
            info.remove(target)
            result.append([max_name, max_num, max_id])
        ming = 0
        last_point = 1000
        last_ming = 0
        for k in result:
            ming += 1
            if last_point != k[1]:  # 说明分数不同
                last_point = k[1]
                last_ming = ming
                print("学生id为：%s，学生姓名为：%s，平均成绩为：%.2f，学生名次为：%s" % (k[2], k[0], k[1], ming))
            else:   # 说明跟上一个名次相同
                last_point = k[1]
                print("学生id为：%s，学生姓名为：%s，平均成绩为：%.2f，学生名次为：%s" % (k[2], k[0], k[1], last_ming))
        # print(result)
    elif func == "4":
        print("欢迎下次使用。")
        break
    else:
        print("请输入正确的指令！")
