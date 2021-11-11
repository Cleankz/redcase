def TheRabbitsFoot(s,encode):
    if encode == True:
        string = list(s)
        words = []
        for j in range(len(string)):
            if string[j] != ' ':
                words.append(string[j])
        words_to_str = ''.join(words)
        N = len(words_to_str)
        m_size = N**0.5
        rows = (m_size *10) //10
        columns = ((m_size * 10) % 10) // 1
        matrix = []
        if rows * columns > N:
            for row in range(int(rows)):
                r = []
                for column in range(int(columns)):
                    if column>len(words)-1:
                        break
                    r.append(words[column])
                del words[:int(columns)]
                matrix.append(r)
        if rows * columns < N:
            #and rows<columns:
            while rows * columns < N:
                rows = rows + 1
            for row in range(int(rows)):
                r = []
                for column in range(int(columns)):
                    if column>len(words)-1:
                        break
                    r.append(words[column])
                del words[:int(columns)]
                matrix.append(r)
        #elif rows * columns < N and rows>columns:
            #while rows * columns < N:
                #columns = columns + 1
            #for row in range(int(rows)):
                #r = []
                #for column in range(int(columns)):
                    #if column>len(words)-1:
                        #break
                    #r.append(words[column])
                #del words[:int(columns)]
                #matrix.append(r)
        new_array = []
        diff = 0
        if columns > rows:
            diff = int(columns-rows)
        else:
            diff = int(rows-columns)
        for x in range(len(matrix[0])):
            for z in range(len(matrix)):
                if len(matrix[z])-1< x:
                    break
                elif len(matrix[z])-1>= x:
                    new_array.append(matrix[z][x])
            new_array.append(' ')
        del new_array[len(new_array)-1]
        new_str = ''.join(new_array)
        return new_str
    if encode == False:
        string = list(s)
        N = len(string)
        m_size = N**0.5
        rows= (m_size *10) //10
        columns= ((m_size * 10) % 10) // 1
        matrix = []
        if rows * columns > N:
            for row in range(int(rows)):
                r = []
                for column in range(int(columns)):
                    if column>len(string)-1:
                        break
                    r.append(string[column])
                del string[:int(columns)]
                matrix.append(r)
        if rows * columns < N:
            #and rows<columns:
            while rows * columns < N:
                rows = rows + 1
                
            for i in range(int(columns)):
                matrix.append([])  
            for x in range(int(columns)):
                for y in range(int(rows)):
                    if y <len(string):
                        matrix[x].append(string[y])
                    else:
                        break
                del string[:int(columns)]
                
            #for row in range(int(rows)):
                #r = []
                #for column in range(int(columns)):
                    #if column>len(string)-1:
                        #break
                    #r.append(string[column])
                #del string[:int(columns)]
                #matrix.append(r)
                
                
        #elif rows * columns < N and rows>columns:
            #while rows * columns < N:
                #columns = columns + 1
            #for row in range(int(rows)):
                #r = []
                #for column in range(int(columns)):
                    #if column>len(string)-1:
                        #break
                    #r.append(string[column])
                #del string[:int(columns)]
                #matrix.append(r)
        new_array = []
        for x in range(len(matrix[0])):
            for z in range(len(matrix)):
                if len(matrix[z])-1< x:
                    break
                elif len(matrix[z])-1>= x:
                    new_array.append(matrix[z][x])
            new_array.append(' ')
        del new_array[len(new_array)-1]
        new_str = ''.join(new_array)
        return new_str