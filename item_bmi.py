

from excelToJson import *


itemName="身高体重"

def checkJsonExist():
    if not os.path.exists(f'standard/{itemName}.json'):
        excel2json(f'standard/{itemName}.xlsx', f'standard/{itemName}.json')

checkJsonExist()
jsonDatas = json.load(open(f'standard/{itemName}.json'))


def getData_from_bmi(data):
    
    data_score = ""
    data_level = ""
    data_record = data["身高体重指数"]
    dataSex = data["性别"]
    print(f"性别： {dataSex} 身高体重指数:{data_record}")
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
        scoreScopeFloatMax = 0
        if "≥" in scoreScope:
            scoreScope = scoreScope.replace("≥", "")
            scoreScopeFloatMin = float(scoreScope)
            if data_record >= scoreScopeFloatMin:
                data_score = step_data["得分"]
                data_level = step_data["等级"]
                print(f"身高体重1 data_score: {data_score} data_score: {data_level}")
                break


        elif "≤" in scoreScope:
            scoreScope = scoreScope.replace("≤", "")
            scoreScopeFloatMax = float(scoreScope)
            if data_record <= scoreScopeFloatMax:
                data_score = step_data["得分"]
                data_level = step_data["等级"]
                print(f"身高体重2 data_score: {data_score} data_score: {data_level}")
                break
        elif "~" in scoreScope:
            scoreList = scoreScope.split("~")
            scoreScopeFloatMin = float(scoreList[0])
            scoreScopeFloatMax = float(scoreList[1])

            if scoreScopeFloatMin <= data_record and data_record <= scoreScopeFloatMax:
                data_score = step_data["得分"]
                data_level = step_data["等级"]
                print(f"身高体重3 data_score: {data_score} data_score: {data_level}")
                break


    return data_score,data_level    