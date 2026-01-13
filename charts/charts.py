import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ["Tecnología", "Salud", "Educación", "Entretenimiento", "Transporte"]
    values = [30, 25, 20, 15, 10]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Distribución del Presupuesto por Sector")
    plt.savefig("pie.png")
    plt.close()
    