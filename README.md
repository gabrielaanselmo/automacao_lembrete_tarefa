# 📆 Automação de Lembrete de Tarefas

Este repositório contém um script Python 🐍 para enviar automaticamente lembretes de tarefas por e-mail 📧. O script lê as tarefas de um arquivo CSV e envia e-mails de lembrete nas datas e horas especificadas.

## ✨ Características

- **📋 Leitura de Tarefas**: As tarefas são armazenadas em um arquivo CSV com os campos título, descrição e data/hora de vencimento.
- **📬 Envio Programado de E-mails**: O script envia e-mails com base nas datas e horários de conclusão definidos para cada tarefa.
- **📝 Logs de Atividades**: Todas as ações realizadas pelo script são registradas em um arquivo de log para fácil rastreamento e depuração.
- **🔒 Segurança**: As credenciais de e-mail são armazenadas de forma segura usando variáveis de ambiente.

## 🗂 Estrutura do Projeto
```
/
├── .github/workflows/ # GitHub Actions workflows
├── data/
│ └── tasks.csv # Arquivo CSV contendo as tarefas
├── src/
│ └── task_reminder.py # Script principal do lembrete de tarefas
└── README.md
```


## ⚙️ Configuração

1. **📝 Arquivo de Tarefas CSV**: Adicione suas tarefas ao arquivo `data/tasks.csv`. O formato deve ser o seguinte:

```csv
Title,Description,DueDate
"Tarefa 1","Descrição da Tarefa 1","AAAA-MM-DD HH:MM"
"Tarefa 2","Descrição da Tarefa 2","AAAA-MM-DD HH:MM"
```

2. **🔑 Variáveis de Ambiente**: Configure as seguintes variáveis de ambiente no seu ambiente de execução ou GitHub Secrets:
```
EMAIL_REMETENTE: Seu e-mail de remetente.
EMAIL_DESTINATARIO: O e-mail do destinatário.
SENHA: A senha do seu e-mail de remetente.
```
3. **🚀 GitHub Actions**: O arquivo .github/workflows/manual.yml está configurado para permitir a execução manual do script através do GitHub Actions.

## 🚀 Execução
Para executar o script manualmente:

```
Vá para a aba 'Actions' no seu repositório GitHub.
Encontre o workflow 'Manual Task Reminder Workflow'.
Clique em 'Run workflow', escolha a branch e clique em 'Run workflow' novamente.
O script será executado e os lembretes serão enviados de acordo com as tarefas configuradas no arquivo CSV.
```