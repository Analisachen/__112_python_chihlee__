import pyinputplus as piyp

scores = piyp.inputInt("請輸入學生分數(最高300分):", min=0,max=300)
isYes = piyp.inputMenu(['y', 'n'], prompt="學生是否符合加分條件(請選擇1或2)?\n", numbered=True)
if isYes=="y" :
    print ("加分")

else:
    print("減分")
        
name = "大球"

print()
print(f"學生{name}分數為{scores}")