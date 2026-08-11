# 🤖 Assistente Pessoal

Assistente pessoal inteligente desenvolvido para funcionar continuamente em um **Raspberry Pi**, utilizando IA para centralizar informações, automatizar tarefas e auxiliar no gerenciamento do dia a dia.

A principal interface será o **Telegram**, permitindo interagir com o assistente através de linguagem natural.

O projeto também será utilizado como experimento prático de **desenvolvimento de software assistido por Inteligência Artificial (AI-Assisted Development)**.

---

## Objetivos

- Criar um assistente pessoal sempre disponível.
- Centralizar agenda, tarefas, documentos e informações pessoais.
- Integrar serviços externos utilizados no dia a dia.
- Automatizar tarefas repetitivas.
- Monitorar computadores e infraestrutura.
- Utilizar LLMs para interpretar comandos em linguagem natural.
- Explorar desenvolvimento assistido por IA.

---

## Funcionalidades

### 📅 Agenda e lembretes

- Integração com Google Calendar.
- Criar, consultar, atualizar e remover eventos.
- Lembretes e notificações.
- Consulta da agenda do dia.
- Sincronização com tarefas.

### 📱 Telegram

- Interface principal do assistente.
- Conversação em linguagem natural.
- Comandos administrativos.
- Envio e recebimento de arquivos.
- Notificações.

### 🖥️ Controle do PC

- Verificar status.
- Wake-on-LAN.
- Desligar/reiniciar.
- Monitorar CPU, RAM, GPU e temperaturas.

### 📊 Monitoramento

- Raspberry Pi.
- PC e notebook.
- Docker e serviços.
- CPU, RAM, disco e temperatura.
- Rede e internet.
- Alertas automáticos.

### 📁 Arquivos + RAG

- Armazenamento de documentos.
- Busca tradicional e semântica.
- Indexação.
- RAG.
- Resumo e perguntas sobre documentos.

### 🧠 Memória pessoal

- Memória persistente.
- Memória explícita.
- Criar, consultar, atualizar e remover memórias.
- Memória temporária e permanente.

### ✅ Tarefas

- Criar e concluir tarefas.
- Prioridades e prazos.
- Categorias.
- Tarefas recorrentes.
- Integração com Google Calendar.

### 💰 Finanças

- Receitas e despesas.
- Categorias.
- Histórico.
- Resumos mensais.
- Relatórios e gráficos.

### ☀️ Resumo diário

Briefing automático com:

- Agenda.
- Tarefas.
- Lembretes.
- Notícias.
- Finanças.
- Infraestrutura.
- Outras informações relevantes.

### 🌐 Web Agent

Pesquisa e resumo de informações da internet, principalmente:

- ⚽ Futebol.
- 🎾 Tênis e João Fonseca.
- 💻 Tecnologia.
- 💰 Finanças e economia.
- 🎮 Games.

### 🔔 Notificações

- Eventos da agenda.
- Lembretes.
- Tarefas próximas do prazo.
- Alertas de infraestrutura.
- Notícias importantes.
- Eventos de automação.

### ⚙️ Automações

Permitir criar regras como:

```text
"Todo dia às 7h me envie o resumo diário."

"Se meu PC estiver ligado depois das 2h, me avise."

"Todo domingo faça backup dos meus documentos."
```

## Arquitetura

O Raspberry Pi 3 será responsável pela execução do assistente, integrações, armazenamento de dados, automações e execução das ferramentas.

O processamento de linguagem será realizado através de **APIs de LLM**, evitando a execução de modelos localmente no Raspberry Pi.

```text
                         🤖 ASSISTENTE
                               │
                         ┌─────▼─────┐
                         │  Telegram │
                         └─────┬─────┘
                               │
                         ┌─────▼─────┐
                         │   Agent   │
                         └─────┬─────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
           Memory             RAG             Tools
              │                │                │
              ▼                ▼          ┌─────┼──────┐
           Database        Documents      │     │      │
                                          ▼     ▼      ▼
                                      Calendar  PC    Web

                               │
                               ▼
                         ☁️ LLM API
```

O LLM será responsável por interpretar solicitações, raciocinar sobre o contexto e selecionar as ferramentas necessárias.

As ferramentas executarão as operações reais de forma controlada.

O Raspberry Pi funcionará como servidor e orquestrador, enquanto o processamento pesado de IA será realizado externamente através de APIs.

## Tecnologias

### Backend

- Python
- FastAPI
- SQLite
- Telegram Bot API
- Google Calendar API

### Inteligência Artificial

- LLMs via API
- Tool Calling
- RAG
- Embeddings
- Vector Database

### Infraestrutura

- Raspberry Pi 3
- Docker
- Wake-on-LAN
- SSH

### Monitoramento

- Prometheus
- Grafana

As tecnologias poderão ser alteradas conforme as necessidades do projeto, priorizando baixo consumo de recursos e simplicidade devido às limitações do Raspberry Pi 3.

---

## Roadmap

| Milestone | Objetivo                        |
| --------- | ------------------------------- |
| **M0**    | Fundação do projeto             |
| **M1**    | Telegram MVP                    |
| **M2**    | LLM + Agent                     |
| **M3**    | Google Calendar                 |
| **M4**    | Notificações + Agenda           |
| **M5**    | Tarefas                         |
| **M6**    | Memória pessoal                 |
| **M7**    | Arquivos + RAG                  |
| **M8**    | Controle do PC                  |
| **M9**    | Monitoramento de infraestrutura |
| **M10**   | Controle financeiro             |
| **M11**   | Web Agent                       |
| **M12**   | Resumo diário                   |
| **M13**   | Automações                      |
| **M14**   | Hardening e produção            |

---

## AI-Assisted Development

A IA será utilizada durante todo o desenvolvimento como ferramenta de apoio para:

- Planejamento
- Arquitetura
- Implementação
- Testes
- Debugging
- Refatoração
- Code review
- Documentação

Cada milestone será dividida em pequenas **Issues**, permitindo desenvolver, testar e validar cada funcionalidade de forma incremental.

---

## Status

**Em desenvolvimento — M0: Fundação do projeto**
