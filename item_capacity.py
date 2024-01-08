# 肺活量
from excelToJson import *

itemName="肺活量"
def checkBmiJsonExist():
    if not os.path.exists(f'standard/{itemName}.json'):
        excel2json(f'standard/{itemName}.xlsx', f'standard/{itemName}.json')
    

checkBmiJsonExist()
jsonDatas = json.load(open(f'standard/{itemName}.json'))

def getData_from_capacity(data):
     
    data_score = ""
    data_level = ""
    colName = f"{itemName}成绩"
    data_record = data[colName]
    dataSex = data["性别"]
    print(f"性别： {dataSex} {colName}:{data_record}")
    level = data["年级"]
    if not data_record or not level:
        return data_score, data_level
    
    data_record = float(data_record)
    
    for step_data in jsonDatas:
        if data["性别"] != step_data["性别"]:
            continue


        if not level in step_data:
            continue

        scoreScope = step_data[level] 
        scoreScopeFloatMin = 0

        scoreScopeFloatMin = float(scoreScope)
        if data_record >= scoreScopeFloatMin:
            data_score = step_data["得分"]
            data_level = step_data["等级"]
            print(f"{colName} data_score: {data_score} data_score: {data_level}")
            break



    return data_score,data_level   


def updateDatas_from_capacity(srcDatas, itemNameArray):
    
    itemNameArray.append(itemName)
    print(f"开始[{itemName}]检索")
    for data in srcDatas:
        if not f"{itemName}成绩" in data:
            data[f"{itemName}得分"] = ""
            data[f"{itemName}等级"] = ""
            continue

        score, level = getData_from_capacity(data)
        data[f"{itemName}得分"] = score
        data[f"{itemName}等级"] = level
