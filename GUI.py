from tkinter import *
from tkinter import scrolledtext
import main
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt



def mat_ent():
    txt_matrix = txt.get("1.0", "end")

    matrix = [[int(x) for x in a.split()] for a in txt_matrix.split("\n")]
    matrix = matrix[:len(matrix)-1]
    answer = main.get_ans(matrix)
    messagebox.showinfo('Максимальные внутренне устойчивые подмножества', answer)

def show_matrix():
    txt_matrix = txt.get("1.0", "end")
    graph = nx.DiGraph()

    matrix = [[int(x) for x in a.split()] for a in txt_matrix.split("\n")]
    matrix = matrix[:len(matrix)-1]
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                graph.add_nodes_from([i, j])
                graph.add_edge(i, j)


    pos = nx.spring_layout(graph)
    labels = dict()
    for node in graph.nodes:
        labels[node] = 'V' + str(node + 1)
    nx.draw(graph, pos, with_labels=True, labels=labels)
    nx.draw_networkx_edges(graph, pos)
    plt.show()
    return

def clicked():
    res = "Введите матрицу смежности порядка {}".format(inpt.get())
    n = int(inpt.get())
    text.configure(text = res)

    text.pack()
    txt.pack()
    enter_mat.pack()
    show_matrix_button.pack()



window = Tk()
window.title("Метод Магу")

lbl = Label(window, text="Введите количество вершин графа:", font=("Arial Bold", 15))
lbl.pack()

inpt = Entry(window, width=15)
inpt.pack()


btn = Button(window, text="Ввести", command = clicked)
btn.pack()

text = Label(window, text=' ', font=("Arial Bold", 15))
global txt
txt = scrolledtext.ScrolledText(window, width=40, height=10)


enter_mat = Button(window, text="Вывести максимальные устойчивые подмножества", command=mat_ent)

show_matrix_button = Button(window, text="Визуализировать граф", command=show_matrix, width=25, height=2)


window.geometry('400x400')
window.mainloop()

