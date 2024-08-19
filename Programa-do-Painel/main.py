import sqlite3
from datetime import date
import tkinter as tk
from tkinter import ttk, messagebox
from threading import Timer

# Adaptador para converter datetime.date para string
def adapt_date(iso_date):
    return iso_date.isoformat()

# Conversor para converter string para datetime.date
def convert_date(iso_str):
    return date.fromisoformat(iso_str)

# Registrar os adaptadores e conversores para o SQLite
sqlite3.register_adapter(date, adapt_date)
sqlite3.register_converter("date", convert_date)

# Função para obter uma conexão com o banco de dados
def obter_conexao():
    return sqlite3.connect(r'\\WIN-1M8KK7I9N31\htdocs\chamadas.db', detect_types=sqlite3.PARSE_DECLTYPES)

# Função para criar as tabelas
def criar_tabelas():
    with obter_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chamadas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_unidade TEXT,
                nome_paciente TEXT,
                data_chamada DATE,
                contador_chamadas INTEGER
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contador_diario (
                data DATE PRIMARY KEY,
                contador INTEGER
            )
        ''')
        conn.commit()

# Função para obter o contador do dia atual
def obter_contador(hoje):
    with obter_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT contador FROM contador_diario WHERE data = ?", (hoje,))
        return cursor.fetchone()

# Função para validar e limpar entrada do usuário
def validar_entrada(texto):
    return texto.strip() if texto else None

# Função para limpar as caixas de entrada
def limpar_campos():
    combobox_unidade.set('')  # Limpa a seleção da combobox
    entry_paciente.delete(0, tk.END)

# Função para registrar uma nova chamada
def registrar_chamada():
    global timer_started, time_elapsed, timer

    try:
        nome_unidade = validar_entrada(combobox_unidade.get())
        nome_paciente = validar_entrada(entry_paciente.get())

        if not nome_unidade or not nome_paciente:
            raise ValueError("Por favor, preencha todos os campos.")

        hoje = date.today()  # Agora estamos lidando com objetos data
        with obter_conexao() as conn:
            cursor = conn.cursor()
            
            # Atualizar contador diário
            resultado = obter_contador(hoje)
            if resultado:
                contador = resultado[0] + 1
                cursor.execute("UPDATE contador_diario SET contador = ? WHERE data = ?", (contador, hoje))
            else:
                cursor.execute("INSERT INTO contador_diario (data, contador) VALUES (?, ?)", (hoje, 1))
                contador = 1

            # Registrar a chamada
            cursor.execute('''
                INSERT INTO chamadas (nome_unidade, nome_paciente, data_chamada, contador_chamadas)
                VALUES (?, ?, ?, ?)
            ''', (nome_unidade, nome_paciente, hoje, contador))

            conn.commit()

        # Limpar as caixas de entrada após o registro
        limpar_campos()
        messagebox.showinfo("Registro de Chamada", "Chamada registrada com sucesso!")

        # Iniciar ou parar o timer
        if timer_started:
            if timer:
                timer.cancel()
            timer_started = False
            time_elapsed = 0
            label_timer.config(text="Tempo: 00:00")
        else:
            timer_started = True
            update_timer()
    except sqlite3.Error as e:
        messagebox.showerror("Erro no Banco de Dados", f"Ocorreu um erro: {e}")
    except ValueError as ve:
        messagebox.showwarning("Entrada Inválida", str(ve))

# Função para atualizar o timer
def update_timer():
    global time_elapsed, timer
    if timer_started:
        time_elapsed += 1
        minutes, seconds = divmod(time_elapsed, 60)
        label_timer.config(text=f"Tempo: {minutes:02}:{seconds:02}")
        timer = Timer(1, update_timer)
        timer.start()

# Função para mostrar o contador diário
def mostrar_contador():
    hoje = date.today()
    resultado = obter_contador(hoje)
    if resultado:
        messagebox.showinfo("Contador Diário", f"Contador de chamadas hoje: {resultado[0]}")
    else:
        messagebox.showinfo("Contador Diário", "Nenhuma chamada registrada hoje.")

# Configurar a interface gráfica
root = tk.Tk()
root.title("Sistema de Chamadas")
root.configure(bg="#2148C0")

# Criar frames para organizar a interface
frame_input = tk.Frame(root, bg='lightblue')  # Cor de fundo do frame_input
frame_input.pack(pady=10)

frame_buttons = tk.Frame(root, bg="#2148C0")  # Cor de fundo do frame_buttons
frame_buttons.pack(pady=10)

# Criar widgets

# Combobox para Nome da Unidade
label_unidade = tk.Label(frame_input, text="Nome da Unidade:", bg='lightblue')
label_unidade.grid(row=0, column=0, padx=5, pady=5)

unidades = ["Consultorio 1", "Consultorio 2", "Sala de Procedimentos", "Sala de Triagem"]

combobox_unidade = ttk.Combobox(frame_input, values=unidades, state="readonly")
combobox_unidade.grid(row=0, column=1, padx=5, pady=5)

# Entrada para Nome do Paciente
label_paciente = tk.Label(frame_input, text="Nome do Paciente:", bg='lightblue')
label_paciente.grid(row=1, column=0, padx=5, pady=5)

entry_paciente = tk.Entry(frame_input)
entry_paciente.grid(row=1, column=1, padx=5, pady=5)

# Label para mostrar o tempo do contador
label_timer = tk.Label(frame_input, text="Tempo: 00:00", bg='lightblue', font=("Arial", 12))
label_timer.grid(row=2, column=0, columnspan=2, pady=10)

# Botão para Registrar Chamada
button_registrar = tk.Button(frame_buttons, text="Registrar Chamada", command=registrar_chamada)
button_registrar.grid(row=0, column=0, padx=5, pady=5)

# Botão para Mostrar Contador Diário
button_contador = tk.Button(frame_buttons, text="Mostrar Contador Diário", command=mostrar_contador)
button_contador.grid(row=0, column=1, padx=5, pady=5)

footer_text = "© 2024 Leonan Matheus leyedecker, @ABOCH."
footer_label = tk.Label(root, text=footer_text, bg="#FAFAFA", fg="#000000", font=("Arial", 8))
footer_label.pack(side="bottom", fill="x", pady=2)

# Criar tabelas ao iniciar a aplicação
criar_tabelas()

# Inicializar variáveis do timer
timer_started = False
time_elapsed = 0
timer = None

# Iniciar o loop principal da interface gráfica
root.mainloop()
