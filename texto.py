def mudança (dados,sep_1:str, sep_2:str):
    lt_dados = list(dados)     
    flag = False

    for i in range (len(lt_dados)): 

        if not flag:
            
            if lt_dados[i] == '"':
                flag = True        
            
            elif lt_dados[i] == sep_1:                    
                lt_dados[i] = sep_2
        
        elif lt_dados[i] == '"' and flag:
            flag = False   
    
    #String
    return ''.join(lt_dados)


file = open('exemplo.txt','r')   
dados = file.read()       

print(dados)

#String
novo = mudança (dados,",",";")
print(novo)