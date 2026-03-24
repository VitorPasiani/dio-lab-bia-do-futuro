# Fin - Agente Financeiro Inteligente com IA Generativa

## Contexto

Os assistentes virtuais no setor financeiro estão evoluindo de simples chatbots reativos para **agentes inteligentes e proativos**. Neste projeto, desenvolvido como desafio final do bootcamp GenAI & Dados, foi criado o **Fin**: um agente financeiro que utiliza IA Generativa para auxiliar na gestão do fluxo de caixa de uma escola de danças. 

O Fin atua diretamente para:
- **Antecipar necessidades** calculando expectativas de déficit ou superávit em um cenário com muitas transações não programadas.
- **Personalizar** planos de ação com base no histórico de receitas e despesas da escola.
- **Cocriar soluções** financeiras de forma consultiva e acessível para os gestores.
- **Garantir segurança** limitando-se estritamente aos dados fornecidos pelo banco de dados, evitando alucinações.

---

## O Que Foi Entregue

### 1. Documentação do Agente

Definição clara do escopo e do comportamento do assistente:
- **Caso de Uso:** O Fin analisa o fluxo de caixa do SaaS da escola de dança e projeta cenários futuros (entradas e saídas) para organizar financeiramente o negócio e prever possíveis déficits.
- **Persona e Tom de Voz:** Consultivo, investigador e com linguagem técnica, porém acessível.
- **Arquitetura:** Interface construída em Streamlit, integração com LLM rodando localmente (Ollama) e consumo de dados tabulares.
- **Segurança:** O agente possui instruções severas para responder apenas com base nos dados internos (de no máximo 1 ano) e admitir limitações quando não possui informações suficientes.

---

### 2. Base de Conhecimento

Foi desenvolvido um banco de dados estruturado simulando o fluxo de caixa diário da escola.

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `data/banco_dados.py` | Python | Histórico de transações mockado (mensalidades, eventos, figurinos, cancelamentos, custos fixos) de um período de 6 meses. |

**Estratégia de Integração:** Para evitar excesso de tokens e alucinações, a aplicação em Python filtra os dados e injeta apenas os totais consolidados e as categorias recentes diretamente no contexto do prompt, funcionando como um RAG tabular enxuto.

---

### 3. Prompts do Agente

O comportamento do Fin é guiado por um System Prompt robusto e mapeamento de cenários:
- **System Prompt:** Focado em análise de métricas, projeção financeira e restrição absoluta de inventar dados.
- **Exemplos de Interação:** Cenários mapeados para listagem pontual, apresentação de eventos e projeções de matrículas.
- **Tratamento de Edge Cases:** O agente bloqueia perguntas fora do escopo financeiro e nega educadamente pedidos de projeções de longuíssimo prazo que não possuem dados suficientes para embasamento.

---

### 4. Aplicação Funcional

Protótipo totalmente funcional executado de forma local, o que garante a privacidade total dos dados da escola:
- **Interface:** Chatbot web interativo desenvolvido com Streamlit.
- **LLM:** Modelo `gpt-oss:20b` gerenciado pelo Ollama.
- **Integração:** Pandas para estruturação do Dataframe e Requests para comunicação via API com o modelo.

📁 **Código Fonte:** [`src/app.py`](./src/app.py)

**Como rodar o projeto localmente:**
```bash
# 1. Instale as dependências
pip install streamlit pandas requests

# 2. Inicie o servidor do Ollama (requer modelo gpt-oss:20b)
ollama serve

# 3. Execute a aplicação web
python -m streamlit run src/app.py
```

### 5. Avaliação e Métricas
A qualidade do agente foi validada através de uma bateria de 5 cenários de teste reais:

Consulta de gastos específicos (Assertividade validada)

Geração de planos de ação para captar matrículas (Alta coerência e criatividade)

Perguntas fora do escopo (Segurança validada)

Informação inexistente no banco (Segurança anti-alucinação validada)

Projeções de longo prazo (Tratamento correto de insuficiência de dados)

6. Pitch
Apresentação estilo elevador (3 minutos) abordando a dor dos gestores da escola, a solução que o Fin traz na prática, uma demonstração visual da ferramenta e o impacto que a automação gera na otimização de tempo.

🎥 Vídeo de Apresentação: (https://drive.google.com/file/d/1eugrOElp3u4qhIMSlUzoIVkmRLRPzDP1/view?usp=sharing)

📁 projeto-final/
│
├── 📄 README.md                      # Documentação principal
│
├── 📁 data/                          # Dados para o agente
│   └── banco_dados.py                # Histórico de transações em Python
│
└── 📁 src/                           # Código da aplicação
    └── app.py                        # Estrutura do Streamlit e integração Ollama
