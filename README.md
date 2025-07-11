# Sequence Alignment Game

**Número da Lista**:  <br>
**Conteúdo da Disciplina**: Programação dinâmica <br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 211042327  |  Carlos Gabriel Cardoso Ramos |
| 202016604  |  João Lucas Miranda de Sousa |

## Sobre

Um jogo educativo que utiliza o algoritmo de Sequence Alignment para avaliar o progresso do jogador na reorganização de frases embaralhadas em múltiplos idiomas.

##  Descrição

O jogo apresenta frases embaralhadas ao jogador, que deve reorganizar as letras para formar a frase original. O algoritmo de Sequence Alignment compara continuamente a frase do jogador com a frase alvo, fornecendo feedback em tempo real sobre o progresso.

##  Características

- **Interface com blocos**: Cada letra aparece em um bloco individual
- **Espaços visíveis**: Espaços são mostrados como blocos especiais
- **Múltiplos idiomas**: Português, Inglês e Francês
- **Feedback inteligente**: Baseado no algoritmo de Sequence Alignment
- **Sistema de pontuação**: Similaridade e distância em tempo real
- **Cronômetro**: Para com a vitória
- **Recordes**: Melhores tempos salvos

## Screenshots


##  Dependências

- Python 3.7+
- Pygame 2.0.0+

##  Instalação

1. Clone ou baixe o projeto
2. Navegue até a pasta do jogo:
```bash
cd game
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🚀 Como Executar

### Método 1: Execução Direta
```bash
python main.py
```

### Método 2: Script de Instalação
```bash
python run_game.py
```

### Método 3: Demonstração do Algoritmo
```bash
python example.py
```

### Método 4: Demonstração Visual
```bash
python visual_demo.py
```

## 🎮 Como Jogar

### Controles
- **Mouse**: Clique em duas letras para trocá-las
- **R**: Iniciar novo jogo
- **D**: Mudar nível de dificuldade
- **L**: Mudar idioma
- **ESC**: Sair do jogo

### Níveis de Dificuldade
- **Fácil**: 30% de embaralhamento
- **Médio**: 50% de embaralhamento 
- **Difícil**: 70% de embaralhamento

### Condições de Vitória/Derrota
- **Vitória**: Similaridade de 100% (frase completamente correta)
- **Derrota**: Tempo esgotado (5 minutos) ou muitas tentativas (50 movimentos)

## 🌍 Idiomas e Frases

### Português
- "Bom dia!"
- "Por favor."
- "Muito obrigado."
- "Permissão concedida."
- "Com licença."

### English
- "Good morning!"
- "Thank you."
- "Please proceed."
- "Excuse me."
- "Of course."

### Français
- "Bonjour!"
- "Merci beaucoup."
- "S'il vous plaît."
- "Excusez-moi."
- "Bien sûr."

## 🔧 Estrutura do Projeto

```
game/
├── main.py              # Ponto de entrada do jogo
├── core.py              # Lógica principal do jogo
├── constants.py         # Configurações e frases
├── sequence_alignment.py # Implementação do algoritmo
├── example.py           # Demonstração do algoritmo
├── visual_demo.py       # Demonstração visual
├── run_game.py          # Script de instalação
├── requirements.txt     # Dependências
└── README.md           # Este arquivo
```

##  Algoritmo de Sequence Alignment

O jogo utiliza a **Distância de Levenshtein** para:
- Calcular o número mínimo de operações para transformar uma string em outra
- Operações: inserções, deleções e substituições
- Fornecer feedback baseado na similaridade
- Determinar quando o jogador completou o desafio

### Implementação
```python
def levenshtein_distance(str1, str2):
    # Implementação da distância de Levenshtein
    # Usa programação dinâmica para eficiência
```



## 🐛 Solução de Problemas

### Erro: "pygame module not found"
```bash
pip install pygame
```

### Erro: "No such file or directory"
Certifique-se de estar na pasta correta:
```bash
cd game
python main.py
```

### Jogo não inicia
Verifique se o Python está instalado:
```bash
python --version
```


##  Desenvolvido com

- **Python**: Linguagem principal
- **Pygame**: Biblioteca para interface gráfica
- **Algoritmo de Levenshtein**: Para comparação de strings


