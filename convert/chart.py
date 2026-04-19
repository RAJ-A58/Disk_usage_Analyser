import matplotlib.pyplot as plt

def show_pie_chart(data):
    labels = []
    sizes = []

    for file_type, count in data:
        labels.append(file_type if file_type else "NO_EXT")
        sizes.append(count)

    plt.figure()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("File Type Distribution")
    plt.show()