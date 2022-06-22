# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
 
menor = 100000
teste = 5.90867
maior = 0
soma = 0
cont = 0
faturamento = [22174.1664, 24537.6698, 26139.6134, 0.0, 0.0, 26742.6612,
                 0.0, 42889.2258, 46251.174, 11191.4722, 0.0, 0.0, 3847.4823, 373.7838,
                 2659.7563, 48924.2448, 18419.2614, 0.0, 0.0, 35240.1826, 43829.1667, 18235.6852,
                 4355.0662, 13327.1025, 0.0, 0.0, 25681.8318, 1718.1221, 13220.495, 8414.61
                 ]

for i in range(0,len(faturamento)):
    if faturamento[i] != 0:
        print(f'dia {i+1} - faturamento: R$ {faturamento[i]:.2f}')
        soma += faturamento[i]
        cont+=1
        if faturamento[i]> maior:
            maior = faturamento[i]
        if faturamento[i]<menor :
            menor = faturamento[i]
    
os.system("PAUSE");
os.system("cls");
media = soma/cont;
cont = 0;
for i in range(0,len(faturamento)):
   if faturamento[i] > media:
       cont+=1
      
print(f"media mensal: R$ {media:.2f}")
print(f"O menor valor de faturamento ocorrido em um dia do mes: R$ {menor:.2f}")
print(f"O maior valor de faturamento ocorrido em um dia do mes: R$ {maior:.2f}")
print(f"Numero de dias no mes em que o valor de faturamento diario foi superior a media mensal: {cont}");
os.system("PAUSE")
