# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 12:35:31 2022

@author: lucas
"""
import os

valorMensalTotal = 67836.43 + 36678.66 + 29229.88 + 27165.48 + (19949.53*23)
perctSP = (67836.43*100)/valorMensalTotal
perctRJ = (36678.66*100)/valorMensalTotal
perctMG = (29229.88 *100)/valorMensalTotal
perctES = (27165.48*100)/valorMensalTotal
perctOutros = ((19949.53*23)*100)/valorMensalTotal
perctTotal = perctSP + perctRJ + perctMG + perctES + perctOutros

print(f'percentual de representação de SP {perctSP:.2f}', '%')
print(f'percentual de representação de RJ {perctRJ:.2f}', '%')
print(f'percentual de representação de MG {perctMG:.2f}', '%')
print(f'percentual de representação de ES {perctES:.2f}', '%')
print(f'percentual de representação dos Outros estados {perctOutros:.2f}', '%')
os.system('PAUSE')