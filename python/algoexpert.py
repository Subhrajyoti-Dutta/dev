def stringAnagram(dictionary, query):
    # Write your code here
    print("temp_dictionary")
    temp_dictionary=list(map(dict_conv,dictionary))
    print("temp_dictionary again: ",temp_dictionary)
    print("\ntemp_query")
    temp_query=list(map(dict_conv,query))
    print("\ntemp_query again: ",temp_query)
    
    print("\ntemp_temp_dictionary")
    temp_temp_dictionary=dict_conv(temp_dictionary)
    print("\ntemp_temp_dictionary again: ",temp_temp_dictionary)

    num=[]
    for i in temp_query:
        if i in temp_temp_dictionary:
            num+=[temp_temp_dictionary[i]]
        else:
            num+=[0]
    return num
            
    
def dict_conv(A):
    temp={}
    print("\nhell yeah")
    print(A)
    for i in A:
        if i not in temp:
            temp[i]=0
        for j in temp:
            if i == j:
                temp[i]+=1
        

    return temp


print(dict_conv("assistent"))

print(stringAnagram(["heater","cold","clod","reheat","docl"],["codl","heater","abcd"]))