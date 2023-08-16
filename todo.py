import tkinter as tk
from tkinter import messagebox


class Tarefa:
    def __init__(self, nome, status):
        self.nome = nome
        self.status = status


class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")

        self.tarefas = []

        self.criar_interface()

    def adicionar_tarefa(self):
        tarefa = self.entrada_tarefa.get()
        status = self.entrada_status.get()
        if tarefa:
            nova_tarefa = Tarefa(tarefa, status)
            self.tarefas.append(nova_tarefa)
            self.atualizar_lista()
            self.entrada_tarefa.delete(0, tk.END)
            self.entrada_status.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Digite uma tarefa.")

    def remover_tarefa(self):
        selecionado = self.lista_tarefas.curselection()
        selecionado = self.lista_tarefas_a_fazer.curselection()
        selecionado = self.lista_tarefas_em_execucao.curselection()
        selecionado = self.lista_tarefas_concluidas.curselection()
        if selecionado:
            indice = selecionado[0]
            self.tarefas.pop(indice)
            self.atualizar_lista()

    def atualizar_lista(self):
        self.lista_tarefas.delete(0, tk.END)
        self.lista_tarefas_a_fazer.delete(0, tk.END)
        self.lista_tarefas_em_execucao.delete(0, tk.END)
        self.lista_tarefas_concluidas.delete(0, tk.END)
        for tarefa in self.tarefas:
            self.lista_tarefas.insert(
                tk.END, f"{tarefa.nome}: {tarefa.status}")
            if tarefa.status == 'A fazer':
                self.lista_tarefas_a_fazer.insert(
                    tk.END, f"{tarefa.nome}")
            elif tarefa.status == 'Em execução':
                self.lista_tarefas_em_execucao.insert(
                    tk.END, f"{tarefa.nome}")
            elif tarefa.status == 'Concluída':
                self.lista_tarefas_concluidas.insert(
                    tk.END, f"{tarefa.nome}")

    def criar_interface(self):
        # Rótulos (títulos)
        label_tarefa = tk.Label(self.root, text="Nome da Tarefa:")
        label_status = tk.Label(
            self.root, text="Status- Informe se a tarefa está 'A fazer', 'Em execução' ou 'Concluída's")
        label_a_fazer = tk.Label(self.root, text="Tarefas a serem feitas:")
        label_em_execucao = tk.Label(
            self.root, text="Tarefas em execução:")
        label_concluidas = tk.Label(self.root, text="Tarefas concluídas:")

        # Entradas
        self.entrada_tarefa = tk.Entry(self.root)
        self.entrada_status = tk.Entry(self.root)

        # Botões
        botao_adicionar = tk.Button(
            self.root, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        botao_remover = tk.Button(
            self.root, text="Remover Tarefa Selecionada", command=self.remover_tarefa)

        # Posicionamento dos elementos
        label_tarefa.pack(padx=10, pady=5, anchor=tk.W)
        self.entrada_tarefa.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        label_status.pack(padx=10, pady=5, anchor=tk.W)
        self.entrada_status.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        botao_adicionar.pack(padx=10, pady=5)
        botao_remover.pack(padx=10, pady=5)

        self.lista_tarefas = tk.Listbox(self.root)
        self.lista_tarefas_a_fazer = tk.Listbox(self.root)
        self.lista_tarefas_em_execucao = tk.Listbox(self.root)
        self.lista_tarefas_concluidas = tk.Listbox(self.root)

        label_a_fazer.pack(padx=5, pady=5, anchor=tk.W)
        self.lista_tarefas_a_fazer.pack(
            padx=5, pady=1, fill=tk.BOTH, expand=True)
        label_em_execucao.pack(padx=5, pady=5, anchor=tk.W)
        self.lista_tarefas_em_execucao.pack(
            padx=5, pady=2, fill=tk.BOTH, expand=True)
        label_concluidas.pack(padx=5, pady=5, anchor=tk.W)
        self.lista_tarefas_concluidas.pack(
            padx=10, pady=2, fill=tk.BOTH, expand=True)

        self.lista_tarefas.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        self.atualizar_lista()


if __name__ == "__main__":
    root = tk.Tk()
    todo_list = ToDoList(root)
    root.mainloop()
