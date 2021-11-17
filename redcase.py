def TheRabbitsFoot(str,encode):
    no_sp_str = str.replace(" ","")
    list_str = list(no_sp_str)
    words = []
    len_of_str = len(no_sp_str)
    m_size = len_of_str**0.5
    columns= (m_size *10) //10 # число строк
    rows = ((m_size * 10) % 10) // 1 # число столбцов
    for i in range(len_of_str - int((rows*columns))):
        if rows * columns < len_of_str:
            columns = columns + 1
    if encode is True:
        for i in range(len(list_str)):
            if len(list_str) !=0:
                st= ''
                for j in range(int(rows)):
                    if len(list_str) !=0:
                        st = st + list_str[0]
                        del list_str[0]
                words.append(st)
                
        res_str = ''
        for i in range(int(rows)):
            st_2 = ''
            for j in range(int(columns)):
                if i <= len(words[j])-1 and words[j][i] != '':
                    st_2 = st_2 + words[j][i]
            res_str = res_str + ' ' + st_2
        res_str = res_str.replace(" ","",1)
        return res_str
    
    elif encode is False:
        result = []  
        for i in range(int(columns)):
            result.append([])
    
        if (rows*columns) - len_of_str !=0:
            diff = (rows*columns) - len_of_str
            for i in range(int(columns) - int(diff)):
                st_2 =''
                for j in range(int(columns)):
                    result[i].append(no_sp_str[0])
                    no_sp_str = no_sp_str.replace(no_sp_str[0],'',1)
            for ar in range(int(columns) - int(diff),len(result)):
                for j in range(int(diff)):
                    if len(no_sp_str) !=0:
                        result[ar].append(no_sp_str[0])
                        no_sp_str = no_sp_str.replace(no_sp_str[0],'',1)
        else:
            for i in range(int(columns)):
                st_2 =''
                for j in range(int(rows)):
                    result[i].append(no_sp_str[0])
                    no_sp_str = no_sp_str.replace(no_sp_str[0],'',1)
            
        result_str = ''
        for i in range(int(columns)):
            for j in range(int(rows)):
                if i <= len(result[j])-1 and result[j][i] != '':
                    result_str = result_str + result[j][i]
        
        return  result_str