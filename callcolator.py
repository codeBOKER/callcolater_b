'''
this program can callcolate any opration you want 
and, you can put your oprators in one line.

'''
# to make an auto loop
chain = True
while chain:
    # our input
    oper =  input("you can enter operation or more: ")

    # in this step we will callcolate all * oprators
    oper_mult = oper.replace("/", "_").replace("+", "_").replace("-", "_")
    parts = oper_mult.split("_")
    for part in parts:
        try:
            float(part)
        except:
            args = part.split("*")
            res_mult = float(args[0]) * float(args[1])
            p = part
    
    # in this step we will callcolate all / oprators
    try:
        new_oper = oper.replace(p,str(res_mult))
    except NameError:
        new_oper =oper
    oper_divi = new_oper.replace("+", "_").replace("-", "_")
    parts = oper_divi.split("_")
    for part in parts:
        try:
            float(part)
        except:
            args = part.split("/")
            res_divi = float(args[0]) / float(args[1])
            p = part
               
            
    # in this step we will callcolate all + oprators 
    try:
        new_oper_d = new_oper.replace(p,str(res_divi))
    except NameError:
        new_oper_d = new_oper
    oper_sum = new_oper_d.replace("-", "_")
    parts = oper_sum.split("_")
    for part in parts:
        try:
            float(part)
        except:
            args = part.split("+")
            res_sum = float(args[0]) + float(args[1])
            p = part
            
    # in this step we will callcolate all - oprators 
    try:
        new_oper_s = new_oper_d.replace(p,str(res_sum))
    except NameError:
        new_oper_s = new_oper_d
    args = new_oper_s.split("-")
    res_min = float(args[0]) - float(args[1])

    result = res_min
    print(result)
    oper =  input("q to quit any key to continue: ")
    if oper == "q":
        chain = False
