import traceback
from t2 import t,s
try:
    s()
except:
    error=str(traceback.format_exc())
    
    errorList=error.split("\n")

    # print(error)
    errorType=errorList[-2]
    errorCmd=errorList[-3].replace("  ","")
    errorFile=errorList[-4].split(".py")[0].split("\\")[-1]
    errorFct=errorList[-4].split(", in ")[-1]
    errorLine=errorList[-4].split(", ")[1].replace("line ","")
    
    print("Type "+errorType)
    print("Cmd "+errorCmd)
    print("File "+errorFile)
    print("Fct "+errorFct)
    print("Line "+errorLine)
    