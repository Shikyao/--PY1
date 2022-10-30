def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
main_str = main_str.lower()

all_elements = []
letter_elements = []
dict = {}
dict_perc = {}
for i in main_str:
    all_elements.append(i)
for i in range(len(all_elements)):
    err = all_elements[i].isalpha()
    if err == True:
        letter_elements.append(all_elements[i])

for i in range(len(letter_elements)):
    if letter_elements[i] in dict:
        dict[letter_elements[i]] += 1
    else:
        dict[letter_elements[i]] = 1

print(dict)

for i in range(len(letter_elements)):
    if letter_elements[i] in dict_perc:
        dict_perc[letter_elements[i]] += 1/len(letter_elements)*100
    else:
        dict_perc[letter_elements[i]] = 1/len(letter_elements)*100

 #print(dict_perc)


