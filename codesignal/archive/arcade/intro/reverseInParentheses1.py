# Reverse in parentheses
def reverse(s): 
    return s[::-1]

def reverseInParentheses1(inputString):
    output = ""
    d = {}
    key = 0
    i = 0
    while (i < len(inputString)):
        if inputString[i] == "(":
            i += 1
            key += 1
            d[key] = ""
            while (i < len(inputString)):
                if ((inputString[i] != ')') and (inputString[i] != '(')):
                    d[key] += inputString[i]
                    i += 1
                else:
                    break

        elif inputString[i] == ")":
            if len(d) != 0:
                rev_stackring = reverse(d[key])
                
                if len(d) != 1:
                    d[key-1] += rev_stackring

                else:
                    output += rev_stackring    

                del d[key]
                key -= 1
                i += 1
            
            else:
                i += 1

        else:
            while (i < len(inputString)):
                if ((inputString[i] != ')') and (inputString[i] != '(')):
                    output += inputString[i]
 
    return output

def reverseInParentheses2(inputString):
    output = ""
    stackack = []
    n = len(inputString)
    for i in range(n):
        if inputString[i] == "(":
            stackack.append(i)

        elif inputString[i] == ")":
            rev_stackr = reverse(inputString[stackack[-1]:i+1])
            inputString = inputString.replace(inputString[stackack[-1]:i+1], rev_stackr)
            stackack.pop()

    for i in range(n):
        if inputString[i] != "(" and inputString[i] != ")":
            output += inputString[i]

    return output

def reverseInParentheses(inputString):
    output = ""
    stack = [] 
    lenn = len(inputString)
    for i in range(lenn): 
  
        if (inputString[i] == '('): 
            stack.append(i) 
  
        elif (inputString[i] == ')'): 
            temp = inputString[stack[-1]:i + 1] 
            inputString = inputString[:stack[-1]] + temp[::-1] + inputString[i + 1:] 
            del stack[-1] 
  
    for i in range(lenn): 
        if (inputString[i] != ')' and inputString[i] != '('): 
            output += (inputString[i]) 
    return output 

# a5537's solution
# props to vanpet90 for his genious idea to use eval in the previous version of this task
def reverseInParentheses3(s):
    return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')


if __name__ == "__main__":
    a = "foo(bar(baz))blim"
    # print(a.replace("(ng)", ")gn("))
    print(reverseInParentheses(a))
