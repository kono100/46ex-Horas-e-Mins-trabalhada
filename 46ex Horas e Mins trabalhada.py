


#46. Crie um programa que leia um valor inteiro referente a horas trabalhadas naquele dia. Em
#seguida, crie uma função que receba a quantidade em horas, mas exiba o valor em minutos e em segundos.






horas = float(input('Dite a quantidade de horas trabalhadas: '))
min = horas * 60
sec = horas * 60*60
print(f'Você trabalhou {min:,.0f} minutos')
print('ou')
print(f'Você trabalhou {sec:,.0f} minutos\n')