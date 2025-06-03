{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP2gOR3f2W0o0cyhXTbvF1t",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/JaoLuziario/python-estudos/blob/main/Exercicio01.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "diq89JoYFbd2",
        "outputId": "6db00748-9a03-4cbd-c428-e7368463a7ec"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Qual o seu nome?João\n",
            "Bem vindo(a) João\n"
          ]
        }
      ],
      "source": [
        "nome= input(\"Qual o seu nome?\")\n",
        "print (\"Bem vindo(a)\", nome)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dia= input(\"Qual o dia do seu nascimento?\")\n",
        "mes= input(\"Qual o mês do seu nascimento?\")\n",
        "ano= input(\"Qual o ano do seu nascimento?\")\n",
        "print(\"Você nasceu em:\",dia,\"/\",mes,\"/\",ano)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xspoDguO7uC2",
        "outputId": "eabddd63-7e41-4939-cc73-936e39da36d7"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Qual o dia do seu nascimento?7\n",
            "Qual o mês do seu nascimento?4\n",
            "Qual o ano do seu nascimento?01\n",
            "Você nasceu em: 7 / 4 / 01\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "numero1= int (input(\"Primeiro numero:\"))\n",
        "numero2= int (input(\"Segundo numero:\"))\n",
        "soma= (numero1+numero2)\n",
        "print (\"A soma destes numero é:\",soma)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qUHVC3dF8CYG",
        "outputId": "afef5ed8-1731-464c-cb48-f8a6056975d5"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Primeiro numero:10\n",
            "Segundo numero:67\n",
            "A soma destes numero é: 77\n"
          ]
        }
      ]
    }
  ]
}