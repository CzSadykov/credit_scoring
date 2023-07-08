{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOisUVpXt9L/Y3VLaetrs47"
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
      "execution_count": 52,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BT02iX3n3m_n",
        "outputId": "f5e3b6ea-34b6-4c52-f89f-5f7c6459069e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting pyngrok\n",
            "  Downloading pyngrok-6.0.0.tar.gz (681 kB)\n",
            "\u001b[?25l     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m0.0/681.2 kB\u001b[0m \u001b[31m?\u001b[0m eta \u001b[36m-:--:--\u001b[0m\r\u001b[2K     \u001b[91m━━━━━━━━━━━━━━\u001b[0m\u001b[91m╸\u001b[0m\u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m256.0/681.2 kB\u001b[0m \u001b[31m7.6 MB/s\u001b[0m eta \u001b[36m0:00:01\u001b[0m\r\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m681.2/681.2 kB\u001b[0m \u001b[31m10.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Requirement already satisfied: PyYAML in /usr/local/lib/python3.10/dist-packages (from pyngrok) (6.0)\n",
            "Building wheels for collected packages: pyngrok\n",
            "  Building wheel for pyngrok (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pyngrok: filename=pyngrok-6.0.0-py3-none-any.whl size=19867 sha256=4b2fd2da5087212da48a66e51c8b9f6f7cd0778e18aeae57583651d628151993\n",
            "  Stored in directory: /root/.cache/pip/wheels/5c/42/78/0c3d438d7f5730451a25f7ac6cbf4391759d22a67576ed7c2c\n",
            "Successfully built pyngrok\n",
            "Installing collected packages: pyngrok\n",
            "Successfully installed pyngrok-6.0.0\n"
          ]
        }
      ],
      "source": [
        "!pip install -q streamlit"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile credit_scoring_app.py\n",
        "import streamlit as st"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "353gb1_KWXPQ",
        "outputId": "7660b39a-c114-4d11-e97b-e049f413ae37"
      },
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting credit_scoring_app.py\n"
          ]
        }
      ]
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
      "execution_count": 43,
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
        "outputId": "80259a7f-d2a2-4479-f362-afed949edbe6"
      },
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 48
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