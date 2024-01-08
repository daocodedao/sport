


def getLevel_from_score(score):
    if score < 60:
        return "不及格"
    elif score < 80:
        return "及格"
    elif score < 90:
        return "良好"
    elif score >= 90:
        return "优秀"
    
    return ""