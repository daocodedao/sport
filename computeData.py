
from excelToJson import *
from item_bmi import *
from item_capacity import *
from item_50m import *
from item_body_flexion import *
from item_body_rope_skipping import *
from item_body_sit_ups import *
from item_body_50_8 import *
import pandas as pd
from util import *

inputFileName = "五年级6班"
excel2json(f'srcData/{inputFileName}.xlsx', f'srcData/{inputFileName}.json')


srcData = json.load(open(f'srcData/{inputFileName}.json'))
itemNameArray = []

itemName="身高体重"
itemNameArray.append(itemName)
print(f"开始[{itemName}]检索")
for data in srcData:
    score, level = getData_from_bmi(data)
    data[f"{itemName}成绩"] = score
    data[f"{itemName}等级"] = level
    

itemName="肺活量"
itemNameArray.append(itemName)
print(f"开始[{itemName}]检索")
for data in srcData:
    score, level = getData_from_capacity(data)
    data[f"{itemName}得分"] = score
    data[f"{itemName}等级"] = level

itemName="50米跑"
itemNameArray.append(itemName)
print(f"开始[{itemName}]检索")
for data in srcData:
    score, level = getData_from_50m(data)
    data[f"{itemName}得分"] = score
    data[f"{itemName}等级"] = level

itemName="坐位体前屈"
itemNameArray.append(itemName)
print(f"开始[{itemName}]检索")
for data in srcData:
    score, level = getData_from_body_flexion(data)
    data[f"{itemName}得分"] = score
    data[f"{itemName}等级"] = level

itemName="一分钟跳绳"
itemNameArray.append(itemName)
print(f"开始[{itemName}]检索")
for data in srcData:
    score, level, addScore = getData_from_rope_skipping(data)
    data[f"{itemName}得分"] = score
    data[f"{itemName}等级"] = level
    data[f"附加分"] = addScore

itemName="仰卧起坐"
itemNameArray.append(itemName)
print(f"开始[{itemName}]检索")
for data in srcData:
    score, level = getData_from_sit_ups(data)
    data[f"{itemName}成绩"] = score
    data[f"{itemName}等级"] = level


itemName="50×8"
itemNameArray.append(itemName)
print(f"开始[{itemName}]检索")
for data in srcData:
    score, level = getData_from_50_8(data)
    data[f"{itemName}成绩"] = score
    data[f"{itemName}等级"] = level


itemName="测试成绩"
print(f"开始[{itemName}]检索")

for data in srcData:
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
    

with open(f"srcData/{inputFileName}_output.json", "w", encoding="utf-8") as f:
    json.dump(srcData, f, ensure_ascii=False, indent=4)

df = pd.DataFrame(srcData)
df.to_excel(f"srcData/{inputFileName}_output.xlsx", index=False)

print(f"完成, 输出文件  srcData/{inputFileName}_output.xlsx")
