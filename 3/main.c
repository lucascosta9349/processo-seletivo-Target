#include <stdio.h>
#include <stdlib.h>

int main()
{
    int cont = 0;
    float soma, media, menor = 100000, maior = 0, faturamento[30]={22174.1664, 24537.6698, 26139.6134, 0.0, 0.0, 26742.6612,
                                                                0.0, 42889.2258, 46251.174, 11191.4722, 0.0, 0.0, 3847.4823, 373.7838,
                                                                2659.7563, 48924.2448, 18419.2614, 0.0, 0.0, 35240.1826, 43829.1667, 18235.6852,
                                                                4355.0662, 13327.1025, 0.0, 0.0, 25681.8318, 1718.1221, 13220.495, 8414.61
                                                                };

    for(int i = 0; i<30; i++){
        if(faturamento[i] != 0){
            printf("dia %i - faturamento: R$ %.2f\n", i+1, faturamento[i]);
            soma += faturamento[i];
            cont++;
                if(faturamento[i]> maior){
                    maior = faturamento[i];
                }
                if(faturamento[i]<menor){
                    menor = faturamento[i];
                }
        }
    }
    system("PAUSE");
    system("cls");
    media = soma/cont;
    cont = 0;
    for(int i = 0; i<30; i++){
        if(faturamento[i] > media){
            cont++;
        }
    }
    printf("media mensal: R$ %.2f", media);
    printf("\nO menor valor de faturamento ocorrido em um dia do mes: R$ %.2f\n", menor);
    printf("O maior valor de faturamento ocorrido em um dia do mes: R$ %.2f\n", maior);
    printf("Numero de dias no mes em que o valor de faturamento diario foi superior a media mensal: %d", cont);
    return 0;
}
