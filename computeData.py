
from excelToJson import *
from item_bmi import *
from item_capacity import *
from item_50m import *
from item_body_flexion import *
from item_body_rope_skipping import *
from item_body_sit_ups import *
from item_body_50_8 import *
from item_compose import *
import pandas as pd




def startComputeXls(inFilePath, outFilePath):
    dirname, filename = os.path.split(inFilePath)
    outDirName, outFileName = os.path.split(outFilePath)
    filename_without_ext = os.path.splitext(os.path.basename(filename))[0]
    tmpDataJsonFileName = f"{filename_without_ext}.json"
    tmpJsonFilePath = os.path.join(outDirName, tmpDataJsonFileName)
    # inputFileName = "五年级6班"
    excel2json(inFilePath, tmpJsonFilePath)


    srcData = json.load(open(tmpJsonFilePath))
    itemNameArray = []

    # bmi
    updateDatas_from_bmi(srcData, itemNameArray)

    # 肺活量
    updateDatas_from_capacity(srcData, itemNameArray)

    # 50米
    updateDatas_from_50m(srcData, itemNameArray)

    # 坐位体前屈
    updateDatas_from_body_flexion(srcData, itemNameArray)

    # 一分钟跳绳
    updateDatas_from_rope_skipping(srcData, itemNameArray)

    # 仰卧起坐
    updateDatas_from_sit_ups(srcData, itemNameArray)

    # 50×8
    updateDatas_from_50_8(srcData, itemNameArray)

    # 综合计算
    updateDatas_compose(srcData, itemNameArray)

        

    # with open(f"srcData/{outFilePath}_output.json", "w", encoding="utf-8") as f:
    #     json.dump(srcData, f, ensure_ascii=False, indent=4)

    df = pd.DataFrame(srcData)
    df.to_excel(outFilePath, index=False)

    print(f"完成, 输出文件 {outFilePath}")
