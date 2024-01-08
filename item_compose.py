from util import *
# 
def updateDatas_compose(srcDatas, itemNameArray):

    itemName="测试成绩"
    print(f"开始[{itemName}]检索")

    for data in srcDatas:
        totalScore = 0
        averageScore = 0
        if data['测试成绩'] == "60(免体)" or data['综合成绩'] == "60(免体)":
            data['测试成绩'] = "60(免体)"
            data['测试成绩评定'] = "免体"
            data['综合成绩'] = "60(免体)"
            data['综合评定'] = "免体"
            continue

        if len(itemNameArray) != 0:
            for item in itemNameArray:
                if f"{item}得分" in data:
                    curScore = data[f"{item}得分"]
                elif f"{item}成绩" in data:
                    curScore = data[f"{item}成绩"]


                if not curScore:
                    curScore = 0
                if isinstance(curScore, str):
                    curScore = float(curScore)

                curScore = float(curScore)
                totalScore = totalScore + curScore

            averageScore = float(totalScore/len(itemNameArray))

        data['测试成绩'] = averageScore
        data['测试成绩评定'] = getLevel_from_score(averageScore)
        data['综合成绩'] = averageScore + data['附加分']
        data['综合评定'] = getLevel_from_score(averageScore + data['附加分'])