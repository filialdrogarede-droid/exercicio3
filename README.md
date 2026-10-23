# 🛡️ DIO Agent - Especialista em Análise de Vulnerabilidades

## 📋 Descrição

Este projeto apresenta uma evolução do DIO Agent com foco em análise de vulnerabilidades de segurança.

A especialização foi desenvolvida para que o agente atue como um consultor de segurança, coletando informações sobre o ambiente antes de sugerir ações, avaliando o impacto da vulnerabilidade encontrada e propondo correções alinhadas às boas práticas de segurança.

Diferente de um chatbot tradicional que apenas responde perguntas, o agente especializado busca compreender o contexto antes de fornecer orientações.

---

# 🎯 Objetivos

- Analisar vulnerabilidades em aplicações e infraestrutura.
- Avaliar risco com base em impacto e probabilidade.
- Indicar medidas de mitigação.
- Produzir respostas consistentes e estruturadas.
- Aplicar conceitos fundamentais de AppSec e Segurança da Informação.

---

# 🏗️ Estrutura do Projeto

```text
dio-agent/
│
├── AGENTS.md
│
├── agent/
│   ├── persona.md
│   └── knowledge/
│       └── security-basics.md
│
├── skills/
│   └── vulnerability-analysis/
│       ├── SKILL.md
│       └── README.md
│
└── examples/
    └── app.py
```

---

# 📁 Arquivos Criados e Alterados

## 1. Skill

Criada a skill:

```text
skills/vulnerability-analysis/
```

Arquivos:

```text
SKILL.md
README.md
```

Responsável por orientar o fluxo de análise.

---

## 2. Base de Conhecimento

Arquivo:

```text
agent/knowledge/security-basics.md
```

Conteúdo:

- Vulnerabilidade
- Ameaça
- Risco
- Tríade CIA
- Boas práticas de segurança
- Conceitos introdutórios de AppSec

---

## 3. Persona

Arquivo:

```text
agent/persona.md
```

Foi adicionada uma característica que orienta o agente a:

- Buscar contexto antes de responder.
- Avaliar risco.
- Priorizar recomendações defensivas.
- Evitar sugestões sem informações suficientes.

---

## 4. AGENTS.md

Adicionada uma nova entrada na tabela de skills:

```text
vulnerability-analysis
```

Permitindo que o agente selecione automaticamente a habilidade quando detectar temas relacionados à segurança.

---

# 🧠 Especialização Criada

## Vulnerability Analysis

Objetivo:

Analisar possíveis vulnerabilidades e retornar um resultado estruturado contendo:

- Contexto
- Ativo afetado
- Vetor de ataque
- Impacto
- Probabilidade
- Severidade
- Mitigação

---

## Fluxo da Skill

```text
Receber cenário
       ↓
Coletar contexto
       ↓
Identificar vulnerabilidade
       ↓
Avaliar impacto
       ↓
Avaliar probabilidade
       ↓
Determinar severidade
       ↓
Propor mitigação
```

---

# 🔍 Exemplo de Aplicação

## Código Vulnerável

Exemplo de login vulnerável a SQL Injection:

```python
user = input("Usuário: ")
password = input("Senha: ")

query = (
    "SELECT * FROM users "
    "WHERE username = '" + user +
    "' AND password = '" + password + "'"
)
```

---

## Resultado Esperado da Análise

### Vulnerabilidade

SQL Injection

### Impacto

Alto

Possibilidade de:

- Acesso indevido
- Exposição de dados
- Bypass de autenticação

### Probabilidade

Alta

Entrada do usuário utilizada diretamente na consulta.

### Severidade

Crítica

### Mitigação

Utilizar consultas parametrizadas.

---

# ✅ Validação Após Correção

Após a correção utilizando consultas parametrizadas:

```python
query = (
    "SELECT * FROM users "
    "WHERE username = ? "
    "AND password = ?"
)
```

O agente deve indicar:

```text
SQL Injection mitigado.
Persistem apenas riscos residuais relacionados ao armazenamento e validação das credenciais.
```

---

# 🖥️ Cenário de Infraestrutura

Pergunta enviada ao agente:

```text
Tenho um servidor Ubuntu exposto na internet.
Como posso protegê-lo?
```

Comportamento esperado:

Antes de responder, o agente solicita informações adicionais:

```text
Qual a finalidade do servidor?

Possui firewall configurado?

Quais portas estão expostas?

Existem serviços públicos hospedados?

O acesso remoto utiliza autenticação multifator?
```

Somente após obter contexto o agente apresenta recomendações.

---

# 🚀 Como Executar

## Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/dio-agent-security.git
```

---

## Entrar na Pasta

```bash
cd dio-agent-security
```

---

## Executar o Hermes

```bash
hermes
```

Importante:

O comando deve ser executado dentro da pasta do projeto para que o agente encontre corretamente os arquivos de skills e conhecimento.

---

# 📚 Conhecimentos Aplicados

Durante o desenvolvimento desta especialização foram utilizados conceitos como:

- Security by Design
- OWASP Top 10
- Defense in Depth
- Vulnerability Assessment
- Risk Analysis
- Secure Coding
- DevSecOps

---

# 🔐 Formato de Resposta Padronizado

Toda análise deve seguir:

```text
Vulnerabilidade:

Contexto:

Impacto:

Probabilidade:

Severidade:

Mitigação:

Recomendações adicionais:
```

Isso permite comparar diferentes vulnerabilidades de forma consistente.

---

# 📈 Possíveis Evoluções

- Integração com OWASP Top 10
- Skill para DevSecOps
- Skill para Pentest
- Skill para Infraestrutura Segura
- Skill para trilhas de aprendizado em Cibersegurança
- Priorização automática por CVSS

---

# 🎓 Aprendizados

Este projeto demonstrou que é possível especializar um agente sem treinar modelos de IA, apenas utilizando:

- Skills em Markdown
- Persona
- Base de conhecimento
- Regras de comportamento

A abordagem permite adaptar o agente a diferentes áreas da cibersegurança com baixo esforço e alta flexibilidade.

---

# 👨‍💻 Autor

**Carlos Vinicius Ribeiro**

Projeto desenvolvido para o desafio da DIO - Especialização 
