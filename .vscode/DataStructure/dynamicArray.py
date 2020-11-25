# 1
monthly_expenses = [2200, 2350, 2600, 2130, 2190]

print(monthly_expenses[1]-monthly_expenses[0])

first_quarter_sum = 0

for i in range(3) :
    first_quarter_sum += monthly_expenses[i]

print(first_quarter_sum)

print("Did I spend 2000$ in any month? " , 2000 in monthly_expenses)

monthly_expenses.append(1980)

print("Expenses at the end of Jun: ", monthly_expenses)

monthly_expenses[3] -= 200
print("Expenses after 200$ return in April: ", monthly_expenses)

#2 You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
print('Length of the list:', len(heros))

heros.append('black panther')
print(heros)

#You realize that you need to add 'black panther' after 'hulk',
#   so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(heros.index('hulk')+1, 'black panter')
print(heros)

#  Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3] =  ['dockter strange']
print(heros)

heros.sort()
print(heros)

#3 Create a list of all odd numbers between 1 and a max number. 
#  Max number is something you need to take from a user using input() function

max_number = input('I will list up all the odd numbers between 1 and the number you typed in: ')
odd_nums = []
for i in range(int(max_number)+1) :
    if i % 2 != 0 :
        odd_nums.append(i)

print(odd_nums)