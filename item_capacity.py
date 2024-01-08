# 肺活量
from excelToJson import *


def checkBmiJsonExist():
    if not os.path.exists('standard/肺活量.json'):
        excel2json(u'standard/肺活量.xlsx', 'standard/肺活量.json')
    

checkBmiJsonExist()
jsonDatas = json.load(open('standard/肺活量.json'))

def getData_from_capacity(data):
     
    data_score = ""
    data_level = ""
    colName = "肺活量成绩"
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