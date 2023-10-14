def swapcomma_dot(string):
    swap=""
    for i in string:
        if(i==","):
            swap+="."
        elif(i=="."):
            swap+=","
        else
            swap+=i