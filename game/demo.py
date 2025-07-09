#!/usr/bin/env python3
"""
Demonstração completa do Sequence Alignment Game
Mostra todas as funcionalidades implementadas
"""

import time
from sequence_alignment import levenshtein_distance, calculate_similarity, get_feedback, shuffle_string
from constants import PHRASES, DIFFICULTY_LEVELS

def print_header(title):
    """Imprime um cabeçalho formatado"""
    print("\n" + "="*60)
    print(f" {title}")
    print("="*60)

def demo_language_selection():
    """Demonstra a seleção de idiomas"""
    print_header("SELECÇÃO DE IDIOMAS / LANGUAGE SELECTION")
    
    for i, language in enumerate(PHRASES.keys(), 1):
        print(f"{i}. {language}")
        print(f"   Frases disponíveis: {len(PHRASES[language])}")
        print(f"   Exemplo: '{PHRASES[language][0]}'")
        print()

def demo_difficulty_levels():
    """Demonstra os níveis de dificuldade"""
    print_header("NÍVEIS DE DIFICULDADE")
    
    test_phrase = "Hello, world!"
    print(f"Frase de teste: '{test_phrase}'")
    print()
    
    for difficulty_name, difficulty_value in DIFFICULTY_LEVELS.items():
        shuffled = shuffle_string(test_phrase, difficulty_value)
        distance = levenshtein_distance(test_phrase, shuffled)
        similarity = calculate_similarity(test_phrase, shuffled)
        
        print(f"{difficulty_name} ({difficulty_value:.0%} embaralhamento):")
        print(f"  Embaralhada: '{shuffled}'")
        print(f"  Distância: {distance} operações")
        print(f"  Similaridade: {similarity:.1%}")
        print()

def demo_gameplay_simulation():
    """Simula uma partida completa"""
    print_header("SIMULAÇÃO DE UMA PARTIDA")
    
    # Escolher idioma e frase
    language = "Português"
    target = PHRASES[language][0]  # "Olá, como vai?"
    difficulty = "Médio"
    difficulty_value = DIFFICULTY_LEVELS[difficulty]
    
    print(f"Idioma: {language}")
    print(f"Frase alvo: '{target}'")
    print(f"Dificuldade: {difficulty}")
    print()
    
    # Embaralhar a frase
    shuffled = shuffle_string(target, difficulty_value)
    print(f"Frase embaralhada: '{shuffled}'")
    print()
    
    # Simular tentativas do jogador
    current = shuffled
    attempts = 0
    max_attempts = 10
    
    print("Simulando tentativas do jogador:")
    print("-" * 40)
    
    while attempts < max_attempts and current != target:
        attempts += 1
        
        # Simular uma melhoria (trocar duas letras aleatórias)
        if current != target:
            chars = list(current)
            # Encontrar diferenças e tentar corrigir
            for i in range(len(chars)):
                if i < len(target) and chars[i] != target[i]:
                    # Procurar a letra correta na frase
                    for j in range(len(chars)):
                        if j < len(target) and chars[j] == target[i]:
                            chars[i], chars[j] = chars[j], chars[i]
                            break
                    break
            current = ''.join(chars)
        
        distance = levenshtein_distance(target, current)
        similarity = calculate_similarity(target, current)
        feedback, _, _ = get_feedback(target, current)
        
        print(f"Tentativa {attempts:2d}: '{current}'")
        print(f"           Similaridade: {similarity:.1%} | {feedback}")
        
        if current == target:
            print(f"\n🎉 VITÓRIA! Frase correta encontrada em {attempts} tentativas!")
            break
    
    if current != target:
        print(f"\n❌ Game Over! Frase correta: '{target}'")

def demo_algorithm_details():
    """Demonstra detalhes do algoritmo"""
    print_header("DETALHES DO ALGORITMO")
    
    print("O algoritmo de Sequence Alignment (Distância de Levenshtein) calcula:")
    print("• O número mínimo de operações para transformar uma string em outra")
    print("• Operações: inserções, deleções e substituições")
    print()
    
    examples = [
        ("kitten", "sitting", "Caso clássico"),
        ("hello", "world", "Strings diferentes"),
        ("python", "python", "Strings idênticas"),
        ("", "test", "String vazia"),
    ]
    
    for str1, str2, description in examples:
        distance = levenshtein_distance(str1, str2)
        similarity = calculate_similarity(str1, str2)
        
        print(f"{description}:")
        print(f"  '{str1}' -> '{str2}'")
        print(f"  Distância: {distance} operações")
        print(f"  Similaridade: {similarity:.1%}")
        print()

def demo_educational_benefits():
    """Demonstra os benefícios educacionais"""
    print_header("BENEFÍCIOS EDUCACIONAIS")
    
    benefits = [
        "🧠 Aprendizado de algoritmos de bioinformática",
        "🎯 Desenvolvimento de pensamento estratégico",
        "🔤 Exposição a múltiplos idiomas",
        "⚡ Feedback em tempo real",
        "🏆 Sistema de pontuação motivacional",
        "🎮 Interface lúdica e interativa",
        "📊 Estatísticas de progresso",
        "🌍 Aprendizado multicultural"
    ]
    
    for benefit in benefits:
        print(f"• {benefit}")
    
    print()
    print("O jogo é ideal para:")
    print("• Estudantes de programação")
    print("• Aprendizes de idiomas")
    print("• Entusiastas de algoritmos")
    print("• Qualquer pessoa que queira exercitar a mente")

def main():
    """Função principal da demonstração"""
    print("🎮 SEQUENCE ALIGNMENT GAME - DEMONSTRAÇÃO COMPLETA")
    print("=" * 60)
    print("Este jogo combina algoritmos de bioinformática com aprendizado")
    print("de idiomas de forma lúdica e educativa.")
    
    # Executar demonstrações
    demo_language_selection()
    demo_difficulty_levels()
    demo_algorithm_details()
    demo_gameplay_simulation()
    demo_educational_benefits()
    
    print_header("COMO JOGAR")
    print("1. Execute: python main.py")
    print("2. Escolha o idioma desejado")
    print("3. Clique em duas letras para trocá-las")
    print("4. Tente formar a frase correta")
    print("5. Use R para novo jogo, D para mudar dificuldade, L para mudar idioma")
    
    print_header("FIM DA DEMONSTRAÇÃO")
    print("Obrigado por conhecer o Sequence Alignment Game!")
    print("Desenvolvido com Python e Pygame")

if __name__ == "__main__":
    main() 