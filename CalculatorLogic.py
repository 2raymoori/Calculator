class CalculatorLogic:
    def infixToPostFix(self, inputExp):
        operatorStack = []
        postFixStack = []
        expItems = []
        numberAccum = ""
        tracker = 0
        for i in inputExp:
            expItems.append(i)
        for curItem in expItems:
            tracker += 1
            if (curItem == "*" or curItem == "/" or curItem == "+" or curItem == "-" or curItem == "(" or curItem == ")"):
                if (numberAccum != ""):
                    # Operator found, End of Number Concatination.
                    postFixStack.append(numberAccum)
                    numberAccum = ""
                if len(operatorStack) == 0 or operatorStack[len(operatorStack) - 1] == "(":
                    operatorStack.append(curItem)
                elif ((operatorStack[len(operatorStack) - 1] == "*" or operatorStack[len(operatorStack) - 1] == "/") and (
                        curItem == "+" or curItem == "-")):
                    postFixStack.append(operatorStack.pop())
                    operatorStack.append(curItem)
                elif ((operatorStack[len(operatorStack) - 1] == "+" or operatorStack[len(operatorStack) - 1] == "-") and (
                        curItem == "/" or curItem == "*")):
                    operatorStack.append(curItem)
                elif (((operatorStack[len(operatorStack) - 1] == "*" or operatorStack[len(operatorStack) - 1] == "/") and (
                        curItem == "*" or curItem == "/")) or ((operatorStack[len(operatorStack) - 1] == "+" or
                                                                operatorStack[len(operatorStack) - 1] == "-") and (
                            curItem == "+" or curItem == "-"))):
                    postFixStack.append(operatorStack.pop())
                    operatorStack.append(curItem)
                elif (curItem == "("):
                    operatorStack.append(curItem)
                elif (curItem == ")"):
                    while (True):
                        top = operatorStack.pop()
                        if (top == "("):
                            break
                        else:
                            postFixStack.append(top)
            else:
                numberAccum += curItem
                if(tracker == len(expItems)):
                    postFixStack.append(numberAccum)
        if(len(operatorStack) > 0):
            while(True):
                postFixStack.append(operatorStack.pop())
                if(len(operatorStack) == 0):
                    break
        return postFixStack

    def doArith(self, _operator, _operand1, _operand2):
        result = 0
        if _operator == "*":
            result = _operand1 * _operand2
        elif _operator == "/":
            if _operand2 == 0:
                result = 0
            else:
                result = _operand2 / _operand1
        elif _operator == "+":
            result = _operand1 + _operand2
        else:
            result = _operand2 - _operand1

        return result

    def postFixEval(self, inputPostFixExp):
        expResultStack = []
        for curItem in inputPostFixExp:
            if(curItem == "*" or curItem == "/" or curItem == "+" or curItem == "-"):
                try:
                    actualOperand1 = expResultStack.pop()
                    actualOperand2 = expResultStack.pop()
                    operand1 = float(actualOperand1)
                    operand2 = float(actualOperand2)
                    if ((operand1 == 0 and actualOperand1 == "0") or (operand2 == 0 and actualOperand2 == "0")):
                        return None
                    curResult = self.doArith(curItem, operand1, operand2)
                    expResultStack.append(curResult)

                except Exception as e:

                    print(e)
                    return None
            else:
                expResultStack.append(curItem)
        if (len(expResultStack) == 1 and (isinstance(expResultStack[0], int) or isinstance(expResultStack[0], float))):
            return expResultStack[0]
        return None


# calculator = CalculatorLogic()
# print(calculator.infixToPostFix("9.1/6"))
# print(calculator.postFixEval(calculator.infixToPostFix("9.1/6")))
# print(type(4.5))
