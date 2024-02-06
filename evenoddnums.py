num1=int(input('Enter a num:'))
num2=int(input('Enter a num:'))
odd_list=[]
even_list=[]
while num1<=num2:
    
    if num1%2==0:
       even_list.append(num1)
    else:
        odd_list.append(num1)
    num1+=1

print('odd list:',odd_list)
print('even list:',even_list)
