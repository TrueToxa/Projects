'''NRZI кодирование
NRZI код (Non Return to Zero Invertive) — один из способов линейного кодирования. Суть этого кодирования в том, что имея некоторое устройство, имеющее всего два состояния, мы строим диаграмму его состояний на каждом такте, и если состояние изменилось, то это расценивается как двоичная единица, если же состояние осталось неизменным, то записывается двоичный ноль.



Напишите программу, которая переводит NRZI код в двоичный.

Формат входных данных
На вход программе подается строка, содержащая NRZI код, составленный из символов _, ‾ и |. Длина строки не превышает 8500085000 символов.

Формат выходных данных
Программа должна преобразовать введенный NRZI код в двоичный код и вывести полученный результат.

Примечание 1. Обозначения:

_ – первое состояние устройства;
‾ – второе состояние устройства;
| – переключение устройства в другое состояние.
Примечание 2. Подробнее про NRZI код можно почитать по ссылке.

Примечание 3. Посмотреть все тесты к задаче можно по ссылке.'''

s = input()
nrzi = s.split('|')
print('0' if s[0]!='|' else '', end='')
print('0'*(len(nrzi[0])-1), end='')
for i in nrzi[1:]:
    print('1', end='')
    print('0'*(len(i)-1), end='')
        
