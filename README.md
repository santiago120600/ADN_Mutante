# AND Mutante

Realizar un algoritmo que detecte si una persona tiene diferencias genéticas basándose en su secuencia de ADN. El algoritmo debe recibir como parámetro un arreglo de cadenas de caracteres que representan cada fila de una tabla de NxN con la secuencia del ADN y devolver un verdadero en caso que se encuentre una mutación o falso en caso de no tener mutación. Las letras de los caracteres solo pueden ser: A, T, C, G ; las cuales representan cada base nitrogenada del ADN.

![secuencia ADN](https://github.com/santiago120600/ADN_Mutante/blob/main/matris.png)

Sabrás sí existe una mutación si se encuentra más de una secuencia de cuatro letras iguales, de forma oblicua, horizontal o vertical. Ejemplo de caso con mutación:
String[] dna = [“ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG" ];
En este caso el algoritmo devuelve true . 

# Configuración Dev container Podman
VSCode User settings
```
{
    "dev.containers.executeInWSL": true,
    "dev.containers.dockerPath": "/usr/bin/podman"
}
```
Puedes revisando dónde está instalado podman usando comando
`which podman`

Habilita SystemD en WSL creando `/etc/wsl.conf` en tu distro
```
[boot]
systemd=true

```