#!/usr/bin/env python3
"""
Demonstração visual da nova interface com blocos
"""

from constants import PHRASES, BLOCK_NORMAL, BLOCK_SELECTED, BLOCK_SPACE
import random

def print_block_visualization():
    """Imprime uma visualização ASCII dos blocos"""
    
    print("=" * 80)
    print("VISUALIZAÇÃO DA NOVA INTERFACE COM BLOCOS")
    print("=" * 80)
    
    # Exemplo de frase
    phrase = "Hello, world!"
    selected_index = 4  # Selecionar a vírgula
    
    print(f"\nFrase: '{phrase}'")
    print("Interface com blocos individuais:")
    print()
    
    # Desenhar blocos em ASCII
    for i, char in enumerate(phrase):
        if i == selected_index:
            print(f"[{char:^3}]", end=" ")  # Bloco selecionado
        elif char == ' ':
            print(f"[_ ]", end=" ")     # Espaço visível
        else:
            print(f"[{char:^3}]", end=" ")  # Bloco normal
    print()
    
    # Legenda
    print("\nLegenda:")
    print("• Blocos azuis claros: Letras normais")
    print("• Blocos laranja: Letra selecionada")
    print("• Blocos cinza: Espaços (mostrados como '_')")
    print("• Borda branca: Todos os blocos")

def demonstrate_block_interaction():
    """Demonstra como funciona a interação com os blocos"""
    
    print("\n" + "=" * 80)
    print("DEMONSTRAÇÃO DA INTERAÇÃO COM BLOCOS")
    print("=" * 80)
    
    # Simular uma frase embaralhada
    original = "Python é incrível!"
    shuffled = "Pythno é icrível!"
    
    print(f"Frase original: '{original}'")
    print(f"Frase embaralhada: '{shuffled}'")
    print()
    
    print("Passo a passo da correção:")
    print()
    
    # Simular correções
    steps = [
        "Pythno é icrível!",  # Original embaralhada
        "Pythno é icrível!",  # Selecionar 'n'
        "Pythno é icrível!",  # Trocar 'n' com 'o'
        "Python é icrível!",  # Resultado da troca
        "Python é icrível!",  # Selecionar 'c'
        "Python é icrível!",  # Trocar 'c' com 'r'
        "Python é incrível!", # Resultado da troca
    ]
    
    for i, step in enumerate(steps):
        if i % 2 == 0:  # Mostrar estado
            print(f"Estado {i//2 + 1}: '{step}'")
        else:  # Mostrar ação
            print(f"  Ação: {step}")
        print()

def show_language_examples():
    """Mostra exemplos em diferentes idiomas"""
    
    print("\n" + "=" * 80)
    print("EXEMPLOS EM DIFERENTES IDIOMAS")
    print("=" * 80)
    
    for language, phrases in PHRASES.items():
        print(f"\n{language}:")
        phrase = phrases[0]  # Primeira frase de cada idioma
        
        print(f"Frase: '{phrase}'")
        print("Blocos:")
        
        # Mostrar blocos
        for char in phrase:
            if char == ' ':
                print(f"[_ ]", end=" ")
            else:
                print(f"[{char:^3}]", end=" ")
        print()
        print()

def explain_benefits():
    """Explica os benefícios da nova interface"""
    
    print("\n" + "=" * 80)
    print("BENEFÍCIOS DA NOVA INTERFACE")
    print("=" * 80)
    
    benefits = [
        "🎯 VISIBILIDADE CLARA: Cada letra tem seu próprio bloco",
        "👆 FÁCIL SELEÇÃO: Clique preciso em cada letra",
        "👁️ ESPAÇOS VISÍVEIS: Espaços são mostrados como '_'",
        "🎨 DESTAQUE VISUAL: Letra selecionada fica laranja",
        "📱 INTERFACE INTUITIVA: Similar a jogos de celular",
        "🎮 EXPERIÊNCIA MELHORADA: Mais fácil de jogar",
        "🔤 SUPORTE MULTILÍNGUE: Funciona com todos os idiomas",
        "🎯 PRECISÃO: Menos cliques acidentais"
    ]
    
    for benefit in benefits:
        print(f"• {benefit}")
    
    print()
    print("A nova interface torna o jogo muito mais:")
    print("• Acessível para todas as idades")
    print("• Intuitivo para novos jogadores")
    print("• Preciso para trocas de letras")
    print("• Visualmente atrativo")

def main():
    """Função principal"""
    print("🎮 NOVA INTERFACE COM BLOCOS - DEMONSTRAÇÃO")
    print("=" * 80)
    print("O jogo agora tem uma interface muito mais clara e intuitiva!")
    
    print_block_visualization()
    demonstrate_block_interaction()
    show_language_examples()
    explain_benefits()
    
    print("\n" + "=" * 80)
    print("COMO TESTAR:")
    print("1. Execute: python main.py")
    print("2. Escolha um idioma")
    print("3. Clique nos blocos para trocar letras")
    print("4. Observe como os espaços são visíveis")
    print("5. Veja a letra selecionada destacada em laranja")
    print("=" * 80)

if __name__ == "__main__":
    main() 