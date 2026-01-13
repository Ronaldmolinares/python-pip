import matplotlib.pyplot as plt


def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f"./imgs/Population_{name}.png")
    plt.close()


def generate_pie_chart(values, labels, name=None):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct="%1.1f%%")
    path = f"./imgs/Population_{name}.png" if name is not None else "./imgs/pie.png"
    plt.savefig(path)
    plt.close()


if __name__ == "__main__":
    labels = ["a", "b", "c"]
    values = [100, 200, 300]
    # generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)