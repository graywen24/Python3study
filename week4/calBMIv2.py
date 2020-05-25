#calculate bmi and print both international and Chiense one

try:
    height, weight = eval(input("输入身高（cm)和体重（kg）用逗号隔开:"))
    # print("身高是：",height*100,"cm")
    print("身高是：{:.2f}".format(height / 100), "cm")
    print("weight is:", weight, "kg")
    bmi = weight / pow(height / 100, 2)
    print("BMI IS: {:.2f}".format(bmi))
    int, chn = "", ""
    if bmi < 18.5:
        int, chn ="偏瘦","偏瘦"
    elif 18.5 <= bmi <24:
        int, chn ="ok", "ok"
    elif 24<= bmi < 25:
        int, chn = "ok","fat"
    elif 25 <= bmi <28:
        int, chn ="fat","fat"
    elif 28 <=bmi < 30:
        int, chn ="a bit fat","super fat"
    else:
        int, chn ="suerp fat","super fat"
    print("bmi指标为 国际:'{0}', 中国'{1}'".format(int, chn))
    print("bmi指标为 国际:{0}, 中国{1}".format(int, chn))
except:
    print("输入参数错误")
