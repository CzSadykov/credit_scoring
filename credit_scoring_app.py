{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPUYxZ3AtHl6q45hSpsQfin"
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
      "cell_type": "code",
      "execution_count": 56,
      "metadata": {
        "id": "BT02iX3n3m_n"
      },
      "outputs": [],
      "source": [
        "!pip install -q streamlit"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st"
      ],
      "metadata": {
        "id": "353gb1_KWXPQ"
      },
      "execution_count": 57,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "x = st.slider('Select a value')\n",
        "st.write(x, 'squared is', x * x)"
      ],
      "metadata": {
        "id": "9pk62mZyWYqX"
      },
      "execution_count": 58,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "st.title('Test')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zrOFYgY-fJHE",
        "outputId": "d478cbb2-7ebd-4119-9958-ad67d022fd10"
      },
      "execution_count": 59,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 59
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "nRhjYrLAWztN"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}