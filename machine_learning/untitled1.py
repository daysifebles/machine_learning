{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Copia de Untitled1.ipynb",
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyPRpxQBWPfWchk56f78sbpv",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/daysifebles/machine_learning/blob/master/machine_learning/untitled1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "w9ujZyDUArsD",
        "colab_type": "text"
      },
      "source": [
        "# Listas"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ijeNw2zTAvUh",
        "colab_type": "code",
        "outputId": "957929b3-088c-4f89-b606-f491f5f5c471",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "lista = [1,'dos',3.2,5]\n",
        "lista"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 'dos', 3.2, 5]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 47
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "I-qBbtEQA7Oj",
        "colab_type": "text"
      },
      "source": [
        "### 1) `append(x)`\n",
        "\n",
        "Agregar un item al final de la lista."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3joNPm9xAwwJ",
        "colab_type": "code",
        "outputId": "c9e9ba58-903a-4986-9fd9-9567a3682cc1",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "lista.append('x') \n",
        "lista\n",
        "#equivalente a lista[len(lista):]=['x']"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 'dos', 3.2, 5, 'x']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jA2TWeG6BQu3",
        "colab_type": "text"
      },
      "source": [
        "### 2) `extend(iterable)`\n",
        "\n",
        "Extiende la lista agregando todos los elementos que se le agregen en el argumento iterable."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-7DLCtN0BnTn",
        "colab_type": "code",
        "outputId": "80d8c49c-2fbc-422d-8799-e8f270607691",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "lista.extend([1,2])\n",
        "lista\n",
        "#equivalente a lista[len(lista):]=['x']"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 'dos', 3.2, 5, 'x', 1, 2]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ze_boIoWCspS",
        "colab_type": "text"
      },
      "source": [
        "### 3) `insert(i,x)`\n",
        "\n",
        "Inserta un item en la posición dada. El primer argumento corresponde al índice del elemento donde se va a insertar el item."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "b6GG9q8bCs0r",
        "colab_type": "code",
        "outputId": "2672bcd7-2ca7-4c15-cb10-a65a6a19e96b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "lista.insert(1,'a')\n",
        "lista\n",
        "#lista.insert(len(lista),'a') es equivalente a lista.append('a') "
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 'a', 'dos', 3.2, 5]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 48
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "git8-_dgCtUL",
        "colab_type": "text"
      },
      "source": [
        "### 4) `remove(x)`\n",
        "Eliminia el primer item de la lista que es igual a el argumento x, y devuelve `ValueError` si no hay items iguales a dicho valor.\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CB0n2og7Ct-T",
        "colab_type": "code",
        "outputId": "9277227d-2a91-45f9-8e83-bbf431e54c9b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "lista.remove('a') \n",
        "lista"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 'dos', 3.2, 5, 'x', 1, 2]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 36
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ViJp3-qSCuTq",
        "colab_type": "text"
      },
      "source": [
        "### 5) `pop(i)`\n",
        "\n",
        "Elimina el item de la posición dada y devuelve dicho valor. Si no se específica la posición elimina y devuelve el último item de la lista."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nqiyVKXbCuhV",
        "colab_type": "code",
        "outputId": "a968d583-1eb6-46c0-b0c8-f5d136f35f07",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "lista.pop(2)\n",
        "lista"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 'dos', 'x', 1, 2]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 39
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "g_KKbqGXCu0k",
        "colab_type": "text"
      },
      "source": [
        "### 6) `clear()`\n",
        "\n",
        "Elimina todos los items de la lista."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_iVGzcIUCvAb",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "lista.clear()\n",
        "lista\n",
        "#equivalente a del lista[:]"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "oiE3SN8pJLFB",
        "colab_type": "text"
      },
      "source": [
        "### 7) `index(x[,start[,end]])`\n",
        "\n",
        "Devuelve el índice basado en cero de la lista cuyo primer valor es igual a x, devuelve un ValueError si no se encutra dicho valor. Los argumentos start y end son opcionales y se usan para limitar la busqueda en una subsecuencia de la lista."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hlHyL8PfKZo9",
        "colab_type": "code",
        "outputId": "a8c699ba-51fa-4731-f302-5c78b40288bb",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "lista = [1,'dos',3.2,5]\n",
        "lista.index('dos')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 53
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_n4U0NHuLWEM",
        "colab_type": "text"
      },
      "source": [
        "### 8) `count(x)`\n",
        "\n",
        "Revuelve el número de veces que se encuentra el elemento x en la lista."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rbHW5xQrLWQv",
        "colab_type": "code",
        "outputId": "aec5ff93-5e28-4aab-e09f-a8c9cf50fe27",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "lista.count('dos')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 54
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rDPqOqW6LWg5",
        "colab_type": "text"
      },
      "source": [
        "### 9) `sort(key=None, reverse=False)`\n",
        "\n",
        "ordena los items de la lista."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8QZLsbkPLWyD",
        "colab_type": "code",
        "outputId": "8fee8a7a-ebbe-4646-b6b2-b02cc6d5ce09",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "lista1 = [1,5,8,9,63.2,52.1,47.2]\n",
        "lista1.sort()\n",
        "lista1"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 5, 8, 9, 47.2, 52.1, 63.2]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 58
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7c2yeH7PCvQS",
        "colab_type": "text"
      },
      "source": [
        "### 10) `reverse()`\n",
        "Devuelve los elementos de la lista en forma reversa."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-do0zz8LCvcT",
        "colab_type": "code",
        "outputId": "c7fd2d11-cf8d-409e-e141-87e6971a3498",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "lista.reverse()\n",
        "lista"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[5, 3.2, 'dos', 1]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 51
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "a9VFj2jwIG8_",
        "colab_type": "text"
      },
      "source": [
        "### 11) `copy()`\n",
        "\n",
        "Devuelve una copia superficial de la lista."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MdNim_bRIHF1",
        "colab_type": "code",
        "outputId": "a0dd16cd-6bbd-4cf0-b69b-bc6bc2fb6c1d",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "lista2 = lista.copy()\n",
        "lista2"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[5, 3.2, 'dos', 1]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 59
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-QfozT2EIHOL",
        "colab_type": "text"
      },
      "source": [
        "## EJEMPLO\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fYYw9-5mIHW8",
        "colab_type": "code",
        "outputId": "0cb3870e-1b68-4062-b54b-a105b28dfe68",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']\n",
        "fruits\n",
        "#cuántas veces aparece 'apple en la lista'\n",
        "fruits.count('apple')\n",
        "#En qué indice se encuentra 'banana'\n",
        "fruits.index('banana')\n",
        "#Encuentre el indice después de la posicion 4 que se encuentre 'banana'\n",
        "fruits.index('banana',4)\n",
        "#Colocar en forma reversa la lista fruits\n",
        "fruits.reverse()\n",
        "fruits\n",
        "#Agregar en la última posición 'grape'\n",
        "fruits.append('grape')\n",
        "fruits\n",
        "#Ordenar los elementos de la lista\n",
        "fruits.sort()\n",
        "fruits\n",
        "#Eliminar el último item de la lista fruits\n",
        "fruits.pop()\n",
        "fruits"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 71
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4iZErjOKIHl1",
        "colab_type": "code",
        "outputId": "b41cdd3d-c8ac-4edc-9693-46c4d01a8380",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "stack = [3, 4, 5]\n",
        "#Agregar el número 6\n",
        "stack.append(6)\n",
        "#Agregar el número 7\n",
        "stack.append(7)\n",
        "stack\n",
        "\n",
        "# aplicar varias veces el comando pop\n",
        "stack.pop()\n",
        "stack.pop()\n",
        "stack.pop()\n",
        "stack"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[3, 4]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 1
        }
      ]
    }
  ]
}