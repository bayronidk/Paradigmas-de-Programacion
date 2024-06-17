#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int *generate_list_random(int n) {
    int *lista = (int *)malloc(n * sizeof(int));
    if (lista == NULL) {
        printf("Error de memoria.");
        exit(1);
    }

    srand(time(NULL));  // Inicializar la semilla del generador de numeros aleatorios

    for (int i = 0; i < n; i++) {
        lista[i] = rand() % 201 - 100; // Generar numeros aleatorios en el rango [-100, 100]
    }

    return lista;
}

int minv2(int *lista, int n) {
    int mini = lista[0];
    for (int i = 1; i < n; i++) {
        if (lista[i] < mini) {
            mini = lista[i];
        }
    }
    return mini;
}

int maxv2(int *lista, int n) {
    int maxi = lista[0];
    for (int i = 1; i < n; i++) {
        if (lista[i] > maxi) {
            maxi = lista[i];
        }
    }
    return maxi;
}

int *sumar_listas(int *lista1, int *lista2, int n) {
    int *suma_listas = (int *)malloc(n * sizeof(int));
    if (suma_listas == NULL) {
        printf("Error de memoria.");
        exit(1);
    }

    for (int i = 0; i < n; i++) {
        suma_listas[i] = lista1[i] + lista2[i];
    }

    return suma_listas;
}

void sumar_listas_v2(int *lista1, int *lista2, int n) {
    int *resultado = sumar_listas(lista1, lista2, n);

    printf("Listas sumadas: ");
    for (int i = 0; i < n; i++) {
        printf("%d, ", resultado[i]);
    }
    printf("\n");

    free(resultado);
}

int main() {
    int n = 10;
    int *lista1 = generate_list_random(n);
    int *lista2 = generate_list_random(n);

    printf("Lista 1: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", lista1[i]);
    }
    printf("\n");

    printf("Lista 2: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", lista2[i]);
    }
    printf("\n");

    printf("El minimo de lista 1 es: %d\n", minv2(lista1, n));
    printf("El minimo de lista 2 es: %d\n", minv2(lista2, n));
    printf("El maximo de lista 1 es: %d\n", maxv2(lista1, n));
    printf("El maximo de lista 2 es: %d\n", maxv2(lista2, n));

    sumar_listas_v2(lista1, lista2, n);

    // Liberar la memoria asignada para las listas
    free(lista1);
    free(lista2);

    return 0;
}