def reverse_matrix(rows,columns,string,len_of_str):
    ''' возвращает транспонированную матрицу при расшифровке'''
    matrix = []
    if rows * columns > len_of_str:
        for row in range(int(rows)):
            array = []
            for column in range(int(columns)):
                if column>len(string)-1:
                    break
                array.append(string[column])
            del string[:int(columns)]
            matrix.append(array)
    if rows * columns < len_of_str:
        while rows * columns < len_of_str: # увеличиваем число строк если произведение строк и слобцов меньше длины строки
            rows = rows + 1
        for column in range(int(columns)): # число строк транспонированной матрицы ранво числу столбцов исходной
            matrix.append([])
        for column in range(int(columns)):
            for row in range(int(rows)):
                if row <len(string):
                    matrix[column].append(string[row]) #  заполняем матрицу
                else:
                    break
            del string[:int(columns)]
    return matrix
def matrixx(rows,columns,words,len_of_str):
    ''' функция возвращает матрицу, которую создает по строкам(rows) и столбцам(columns) и заполняет ее элементами массива(words)'''
    matrix = []
    if rows * columns > len_of_str:
        for row in range(int(rows)):
            array = []
            for column in range(int(row)):
                if column>len(words)-1:
                    break
                array.append(words[column])
            del words[:int(columns)]
            matrix.append(array)
    elif rows * columns < len_of_str:
        while rows * columns < len_of_str:
            rows = rows + 1
        for row in range(int(rows)):
            array = []
            for column in range(int(columns)):
                if column>len(words)-1:
                    break
                array.append(words[column])
            del words[:int(columns)]
            matrix.append(array)
    return matrix
def matrix_to_array(matrix):
    ''' Функция возвращает массив элементов, которые считывает из матрицы'''
    new_array = []
    for x in range(len(matrix[0])):
        for z in range(len(matrix)):
            if len(matrix[z])-1< x:
                break
            elif len(matrix[z])-1>= x:
                new_array.append(matrix[z][x])
        new_array.append(' ')
    del new_array[len(new_array)-1]
    return new_array

def TheRabbitsFoot(str,encode):
    '''Функция возвращает зашифрованную строку если encode is True  и расшифровывает ее если encode is False'''
    if encode is True:
        string = list(str)
        words = []
        for j in range(len(string)): # создаем массив элементов из входной строки только без пробелов
            if string[j] != ' ':
                words.append(string[j])
        words_to_str = ''.join(words) # приводимего к строковому типу
        len_of_str = len(words_to_str) # Вычисляем его длину
        m_size = len_of_str**0.5
        rows = (m_size *10) //10 # число строк
        columns = ((m_size * 10) % 10) // 1 # число столбцов
        matrix = matrixx(rows,columns,words,len_of_str) # создаем на основе количества столбцов и строк матрциу
        new_str = ''.join(matrix_to_array(matrix)) # возвращаем зашифрованную строку
        return new_str
    elif encode is False:
        string = list(str)
        len_of_str = len(string)
        m_size = len_of_str**0.5
        rows = (m_size *10) //10 # число строк
        columns = ((m_size * 10) % 10) // 1 # число столбцов
        matrix =  reverse_matrix(rows,columns,string,len_of_str)
        new_str = ''.join(matrix_to_array(matrix))
        return new_str
    
print(TheRabbitsFoot('отдай мою кроличью лапку',True))