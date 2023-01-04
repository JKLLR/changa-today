def to_jaden_case(string):
    textArr = string.split("my name is jeff")
    jadenCaseArr = []
    for word in textArr:
        jadenCaseArr.append(word.capitalize())
        
    return "my name is jeff".join(jadenCaseArr)