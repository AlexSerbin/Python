file = open('src_14.txt', 'rt', encoding="utf-8")
file_2 = open('homework.txt', 'wt', encoding='utf-8')
summ_class_average_mark = 0
num_stud = 0
while True:
    student = file.readline()
    if student == '':
        break
    else:
        num_stud += 1
        lst = student.split()
        lst[0], lst[1] = lst[1], lst[0][0] + '.'
        summ = 0
        for i in range(2, len(lst)):
            summ += int(lst[i])
        aref = round(summ / (len(lst) - 2), 2)
        summ_class_average_mark += aref
        if aref < 5:
            print('Средний бал ниже 5:', lst[0], lst[1])
        file_2.write("      {} {}{}{}\n".format(lst[0], lst[1], (30 - (len(lst[0]))) * " ", aref))
class_average_mark = round(summ_class_average_mark / num_stud, 2)
print('Средний бал по классу =', class_average_mark)
file.close()
file_2.close()
