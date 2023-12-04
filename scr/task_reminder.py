import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import time
import csv
import os


def log_message(message):
    """Função para gravar logs no arquivo de log."""
    with open("../logs/reminder_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()}: {message}\n")


def read_tasks():
    """Função para ler tarefas do arquivo CSV."""
    tasks = []
    with open("../data/tasks.csv", "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Pular cabeçalho
        for row in csv_reader:
            tasks.append(row)
    return tasks


# Configurações do e-mail
sender_email = os.getenv('EMAIL_REMETENTE')  # Lê o e-mail do remetente do ambiente
receiver_email = os.getenv('EMAIL_DESTINATARIO')  # Lê o e-mail do destinatário do ambiente
password = os.getenv('SENHA')  # Lê a senha do e-mail do ambiente

smtp_server = "smtp.gmail.com"
port = 587

# Lê as tarefas do arquivo CSV
tasks = read_tasks()

# Verifica e envia lembretes para cada tarefa
for task in tasks:
    task_title, task_description, task_due_date = task
    reminder_time = datetime.datetime.strptime(task_due_date, '%Y-%m-%d %H:%M')

    # Verifica se é hora de enviar o lembrete
    if datetime.datetime.now() >= reminder_time:
        try:
            subject = f"Lembrete de Tarefa: {task_title}"
            body = f"Olá,\n\nLembrete para a tarefa: {task_title}\nDescrição: {task_description}\nData de Conclusão: {task_due_date}\n\nBoa sorte!"

            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))

            # Conectar ao servidor SMTP e enviar e-mail
            server = smtplib.SMTP(smtp_server, port)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            server.quit()

            log_message(f"Lembrete enviado para a tarefa '{task_title}'.")
        except Exception as e:
            log_message(f"Erro ao enviar o lembrete para '{task_title}': {e}")

    time.sleep(60)  # Pausa antes de verificar a próxima tarefa
