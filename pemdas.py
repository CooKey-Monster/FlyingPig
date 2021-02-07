import time

def isNumber(s):
    #s must be a non-empty string
    #returns True if it's convertible to float, else False
    if (len(s) == 0 and not s == '') or not isinstance(s, str):
        print("type mismatch error: isNumber")
        return "type mismatch error: isNumber"

    try:
        s = float(s)
        return True

    except ValueError:
        return False

def cleanUp(s):
    priorSpace = True
    inDecimal = False
    ops = ["+","-","*","/","^"]
    s = s.replace("+", " + ").replace("-", " - ").replace("*", " * ").replace("/", " / ").replace("^", " ^ ")
    st = list(s)
    for i,c in enumerate(s):
        if (not isNumber(c) and c not in ops) and priorSpace:
            if c == "." and not inDecimal:
                inDecimal = True
            elif c == "." and inDecimal:
                st[i] = ""
            else:
                st[i] = ""
                inDecimal = False
        elif (not isNumber(c) and c not in ops) and not priorSpace:
            if c == "." and not inDecimal:
                inDecimal = True
            elif c == "." and inDecimal:
                st[i] = ""
            else:
                st[i] = " "
                priorSpace = True
                inDecimal = False
        else:
            priorSpace = False
    final = ''.join(st).strip().split(' ')
    if '-' in final[0]:
        del final[0]
        final[0] = '-' + final[0]
    newNumber, newOpr, oprPos = getNextNumber(final, 0)
    if oprPos == None:
        return newNumber
    cacheNum=newNumber
    pos=oprPos+1                #the new current position
    opr=newOpr
    while pos<(len(final)-1):
        newNumber, newOpr, oprPos = getNextNumber(final, pos)
        if (newOpr == None):
            break
        if (not isNumber(newNumber) and newNumber == '-'):
            del final[oprPos-1] #BOOKMARK
            final[oprPos-1] = '-' + final[oprPos-1]
        if (not isNumber(newNumber) and newNumber != '-'):
            print("error at line AB", newNumber)
            return "error at line AB"
        pos=oprPos+1
    return (final)


def getNextNumber(expr, pos):
    #expr is a given arithmetic formula in string
    temp = expr
    #pos = start position in expr
    #1st returned value = the next number (None if N/A)
    #2nd returned value = the next operator (None if N/A)
    #3rd retruned value = the next operator position (None if N/A)
    ops = ["+","-","*","/"]
    if len(expr)==0 or pos<0 or pos>=len(expr) or not isinstance(pos, int):
        print("type mismatch error: getNextNumber")
        return None, None, "type mismatch error: getNextNumber"
    #--- function code starts ---#
    res3 = 0
    res2 = 0
    if (pos+1) < len(temp):
        res3 = pos+1
        res2 = temp[pos+1]
    else:
        res3 = None
        res2 = None
    return ((temp[pos], res2, res3))



    #--- function code ends ---#


def exeOpr(num1, opr, num2):
    #This is a simple utility function skipping type check
    if opr == "+":
        return num1 + num2

    elif opr == "-":
        return num1 - num2
    
    elif opr == "*":
        return num1 * num2

    elif opr == "/":
        return num1 / num2

    elif opr == "^":
        return num1 ** num2

    else:
        return None

def calc(expr):
    #expr: nonempty string that is an arithmetic expression
    #the fuction returns the calculated result
    expr = cleanUp(expr)
    if len(expr)<=0:
        print("argument error: line A in eval_expr")        #Line A
        return "argument error: line A in eval_expr"
    #Hold two modes: "addition" and "multiplication"
    #Initializtion: get the first number
    newNumber, newOpr, oprPos = getNextNumber(expr, 0)
    ops = ["^","*","/","+","-"]
    if newNumber is None or not isNumber(newNumber):
        print("input formula error: line B in eval_expr")   #Line B
        return "input formula error: line B in eval_expr"
    elif newOpr is None or not newOpr in ops:
        return newNumber
    cacheNum=newNumber
    pos=oprPos+1                #the new current position
    opr=newOpr                  #the new current operator
    #start the calculation. Use the above functions effectively.
    new_expr = expr
    while True:
        newNumber, newOpr, oprPos = getNextNumber(new_expr, pos)
        #print(cacheNum, opr, newNumber, "The next opr however is", newOpr)
        if (not isNumber(newNumber)):
            print("input formula error: line C in eval_expr")   #Line C
            return "input formula error: line C in eval_expr"
        if (newOpr == None):
            break
        if(newOpr == "^"):
            temp = getNextNumber(new_expr, oprPos+1)[0]
            if (not isNumber(temp)):
                print("input formula error: line D in eval_expr")   #Line D
                return "input formula error: line D in eval_expr"
            #print("Weee", newOpr, newNumber, "with", temp)
            subs = exeOpr(float(newNumber), newOpr, float(temp))
            del new_expr[oprPos-1]
            del new_expr[oprPos-1]
            new_expr[oprPos-1] = str(subs)
            #print("The new expression to start calculating is: " + new_expr)
        elif((newOpr == "*" or newOpr == "/") and (opr not in ["^","*","/"])):
            temp, temp_Opr, temp_Pos = getNextNumber(new_expr, oprPos+1)
            #print("uhhh", temp_Opr)
            if temp_Opr == "^":
                temp2 = getNextNumber(new_expr, oprPos+3)[0]
                if (not isNumber(temp)):
                    print("input formula error: line D in eval_expr")   #Line D
                    return "input formula error: line D in eval_expr"
                #print("We", temp_Opr, temp, "with", temp2)
                subs = exeOpr(float(temp), temp_Opr, float(temp2))
                del new_expr[temp_Pos-1]
                del new_expr[temp_Pos-1]
                new_expr[temp_Pos-1] = str(subs)
                #print("The new expression to start calculating is: " + new_expr)
            else:
                if (not isNumber(temp)):
                    print("input formula error: line D in eval_expr")   #Line D
                    return "input formula error: line D in eval_expr"
                #print("Weee", newOpr, newNumber, "with", temp)
                subs = exeOpr(float(newNumber), newOpr, float(temp))
                del new_expr[oprPos-1]
                del new_expr[oprPos-1]
                new_expr[oprPos-1] = str(subs)
                #print("The new expression to start calculating is: " + new_expr)
        elif((newOpr == "+" or newOpr == "-") and opr not in ["+","-"]):
            subs = exeOpr(float(cacheNum), opr, float(newNumber))
            del new_expr[pos-2]
            del new_expr[pos-2]
            new_expr[pos-2] = str(subs)
            cacheNum=str(subs)
            opr=newOpr
            #print("The new expressionn to start calculating is: " + new_expr)
        else:
            subs = exeOpr(float(cacheNum), opr, float(newNumber))
            del new_expr[pos-2]
            del new_expr[pos-2]
            new_expr[pos-2] = str(subs)
            #print("The new expression to start calculating is: " + new_expr)
            cacheNum=str(subs)
            opr=newOpr
    subs = exeOpr(float(cacheNum), opr, float(newNumber))
    #print(new_expr)
    del new_expr[new_expr.index(cacheNum)]
    del new_expr[new_expr.index(opr)]
    new_expr[new_expr.index(newNumber)] = str(subs)
    return float(new_expr[0])