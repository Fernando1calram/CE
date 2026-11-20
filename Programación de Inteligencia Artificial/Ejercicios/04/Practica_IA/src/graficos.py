import os

import matplotlib.pyplot as plt
import numpy as np


def crear_carpeta_graficos(ruta_carpeta):
    """Crea la carpeta de gráficos si todavía no existe."""
    os.makedirs(ruta_carpeta, exist_ok=True)


def grafico_distribucion_estados(y, ruta_archivo):
    """Genera un gráfico de barras con el número de registros por estado."""
    estados, recuentos = np.unique(y, return_counts=True)

    etiquetas = [
        "Funcionamiento\nnormal",
        "Desgaste\nmecánico",
        "Sobrecalentamiento"
    ]

    fig, ax = plt.subplots(figsize=(8, 5))
    barras = ax.bar(etiquetas, recuentos, color=["#4C9F70", "#E8B23A", "#D9534F"])

    for barra, recuento in zip(barras, recuentos):
        ax.text(
            barra.get_x() + barra.get_width() / 2,
            barra.get_height() + 2,
            str(recuento),
            ha="center",
            fontsize=11
        )

    ax.set_title("Distribución de registros por estado")
    ax.set_xlabel("Estado de la máquina")
    ax.set_ylabel("Número de registros")
    ax.set_ylim(0, max(recuentos) * 1.15)
    ax.grid(axis="y", alpha=0.3)

    fig.tight_layout()
    fig.savefig(ruta_archivo, dpi=300)
    plt.close(fig)


def grafico_metricas_por_estado(matriz, precisiones, recalls, f1_scores, ruta_archivo):
    """Genera un gráfico de barras con precisión, recall y F1 por estado."""
    estados = np.arange(3)
    ancho = 0.25

    etiquetas = [
        "Funcionamiento\nnormal",
        "Desgaste\nmecánico",
        "Sobrecalentamiento"
    ]

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(estados - ancho, precisiones, ancho, label="Precisión", color="#4C9F70")
    ax.bar(estados, recalls, ancho, label="Recall", color="#E8B23A")
    ax.bar(estados + ancho, f1_scores, ancho, label="F1-score", color="#4C7FBF")

    ax.set_title("Métricas de evaluación por estado")
    ax.set_xlabel("Estado de la máquina")
    ax.set_ylabel("Valor de la métrica")
    ax.set_xticks(estados)
    ax.set_xticklabels(etiquetas)
    ax.set_ylim(0, 1.1)
    ax.legend()
    ax.grid(axis="y", alpha=0.3)

    fig.tight_layout()
    fig.savefig(ruta_archivo, dpi=300)
    plt.close(fig)


def grafico_matriz_confusion(matriz, ruta_archivo):
    """Genera una representación visual de la matriz de confusión."""
    etiquetas = [
        "Funcionamiento\nnormal",
        "Desgaste\nmecánico",
        "Sobrecalentamiento"
    ]

    fig, ax = plt.subplots(figsize=(7, 6))
    imagen = ax.imshow(matriz, cmap="Blues")

    for fila in range(matriz.shape[0]):
        for columna in range(matriz.shape[1]):
            valor = matriz[fila, columna]
            ax.text(
                columna,
                fila,
                str(valor),
                ha="center",
                va="center",
                fontsize=14,
                color="white" if valor > matriz.max() / 2 else "black"
            )

    ax.set_title("Matriz de confusión")
    ax.set_xlabel("Estado predicho")
    ax.set_ylabel("Estado real")
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(etiquetas)
    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels(etiquetas)

    fig.colorbar(imagen, ax=ax, label="Número de registros")
    fig.tight_layout()
    fig.savefig(ruta_archivo, dpi=300)
    plt.close(fig)