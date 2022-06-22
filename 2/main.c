#include <stdio.h>
#include <stdlib.h>

int main(){
  int n1, aux = 0, a=0, b=1;

  printf("digite um numero: ");
  scanf("%d", &n1);
  printf("\n0, ");

  do{
    aux = a+b;
    a = b;
    b = aux;
    printf("%i, ", a);

    if(a == n1){
        printf("\nO numero %d faz parte da sequencia de Fibonnaci!\n", a);
    }
  }while(aux<=n1);
  if(a != n1){
     printf("\nO numero digitado nao faz parte da sequencia de Fibonnaci!");
  }
  return 0;
}
