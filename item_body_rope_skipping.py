# 肺活量
from excelToJson import *


itemName="一分钟跳绳"

def checkJsonExist():
    if not os.path.exists(f'standard/{itemName}.json'):
        excel2json(f'standard/{itemName}.xlsx', f'standard/{itemName}.json')
    
checkJsonExist()
jsonDatas = json.load(open(f'standard/{itemName}.json'))


######################### 跳绳加分 #########################
itemNameExt="跳绳加分"

def checkJsonExistExt():
    if not os.path.exists(f'standard/{itemNameExt}.json'):
        excel2json(f'standard/{itemNameExt}.xlsx', f'standard/{itemNameExt}.json')
    
checkJsonExistExt()
jsonDatasExt = json.load(open(f'standard/{itemNameExt}.json'))


def getData_from_rope_skipping(data):
     
    data_score = 0
    data_level = "不及格"
    # 加分
    diffScore = 0
    colName = f"{itemName}成绩"
    data_record = data[colName]
    dataSex = data["性别"]
    print(f"性别： {dataSex} {colName}:{data_record}")
    level = data["年级"]
    diffRecord = 0

    if not data_record or not level:
        data_score = ""
        data_level = ""
        return data_score, data_level, diffScore

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
            diffRecord = data_record - scoreScopeFloatMin
            data_score = step_data["得分"]
            data_level = step_data["等级"]
            print(f"{colName} data_score: {data_score} data_score: {data_level}")
            break

    if data_score == 100:
        print("跳绳加分")
        for step_data in jsonDatasExt:
            if data["性别"] != step_data["性别"]:
                continue
            
            if not level in step_data:
                continue

            scoreScope = step_data[level] 
            
            if diffRecord >= scoreScope:
                diffScore = step_data["加分"]
                break

        

    return data_score,data_level,diffScore 