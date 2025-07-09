#!/usr/bin/env python3
"""
Exemplo de uso do algoritmo de Sequence Alignment
Demonstra como funciona a distância de Levenshtein com múltiplos idiomas
"""

from sequence_alignment import levenshtein_distance, calculate_similarity, get_feedback, shuffle_string
from constants import PHRASES
import random

def demonstrate_sequence_alignment():
    """Demonstra o funcionamento do algoritmo de Sequence Alignment"""
    
    print("=" * 60)
    print("DEMONSTRAÇÃO DO ALGORITMO SEQUENCE ALIGNMENT")
    print("=" * 60)
    
    # Exemplo 1: Frases em diferentes idiomas
    print("\n1. EXEMPLOS EM DIFERENTES IDIOMAS:")
    
    for language, phrases in PHRASES.items():
        print(f"\n{language}:")
        target = random.choice(phrases)
        # Criar uma versão com erro
        chars = list(target)
        if len(chars) > 3:
            # Trocar duas letras para criar um erro
            i, j = random.sample(range(len(chars)), 2)
            chars[i], chars[j] = chars[j], chars[i]
            current = ''.join(chars)
        else:
            current = target + "x"  # Adicionar caractere extra
        
        distance = levenshtein_distance(target, current)
        similarity = calculate_similarity(target, current)
        feedback, _, _ = get_feedback(target, current)
        
        print(f"  Alvo:     '{target}'")
        print(f"  Atual:    '{current}'")
        print(f"  Distância: {distance} operações")
        print(f"  Similaridade: {similarity:.1%}")
        print(f"  Feedback: {feedback}")
    
    # Exemplo 2: Embaralhamento por idioma
    print("\n2. DEMONSTRAÇÃO DE EMBARALHAMENTO POR IDIOMA:")
    
    for language, phrases in PHRASES.items():
        print(f"\n{language}:")
        target = random.choice(phrases)
        
        for difficulty in [0.3, 0.5, 0.7]:
            shuffled = shuffle_string(target, difficulty)
            distance = levenshtein_distance(target, shuffled)
            similarity = calculate_similarity(target, shuffled)
            
            print(f"  Dificuldade {difficulty:.0%}:")
            print(f"    Original:     '{target}'")
            print(f"    Embaralhada:  '{shuffled}'")
            print(f"    Distância:    {distance} operações")
            print(f"    Similaridade: {similarity:.1%}")
    
    # Exemplo 3: Progresso do jogador em diferentes idiomas
    print("\n3. SIMULAÇÃO DE PROGRESSO DO JOGADOR:")
    
    for language, phrases in PHRASES.items():
        print(f"\n{language}:")
        target = random.choice(phrases)
        shuffled = shuffle_string(target, 0.5)
        
        # Simular algumas tentativas
        current = shuffled
        for attempt in range(1, 4):
            # Simular uma melhoria
            if attempt < 3:
                # Fazer uma pequena melhoria
                chars = list(current)
                if len(chars) > 1:
                    # Trocar duas letras aleatórias
                    i, j = random.sample(range(len(chars)), 2)
                    chars[i], chars[j] = chars[j], chars[i]
                    current = ''.join(chars)
            
            distance = levenshtein_distance(target, current)
            similarity = calculate_similarity(target, current)
            feedback, _, _ = get_feedback(target, current)
            
            print(f"  Tentativa {attempt}: '{current}'")
            print(f"    Similaridade: {similarity:.1%} | {feedback}")
    
    print("\n" + "=" * 60)
    print("FIM DA DEMONSTRAÇÃO")
    print("=" * 60)

def test_algorithm_correctness():
    """Testa a correção do algoritmo com casos conhecidos"""
    
    print("\nTESTES DE CORREÇÃO DO ALGORITMO:")
    print("-" * 40)
    
    test_cases = [
        ("", "", 0),           # Strings vazias
        ("a", "", 1),          # Uma string vazia
        ("", "a", 1),          # Outra string vazia
        ("abc", "abc", 0),     # Strings idênticas
        ("abc", "abd", 1),     # Uma substituição
        ("abc", "abcd", 1),    # Uma inserção
        ("abcd", "abc", 1),    # Uma deleção
        ("kitten", "sitting", 3),  # Caso clássico
    ]
    
    for str1, str2, expected in test_cases:
        result = levenshtein_distance(str1, str2)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{str1}' -> '{str2}': {result} (esperado: {expected})")

def show_available_phrases():
    """Mostra todas as frases disponíveis por idioma"""
    
    print("\nFRASES DISPONÍVEIS NO JOGO:")
    print("=" * 60)
    
    for language, phrases in PHRASES.items():
        print(f"\n{language} ({len(phrases)} frases):")
        for i, phrase in enumerate(phrases, 1):
            print(f"  {i:2d}. {phrase}")

if __name__ == "__main__":
    demonstrate_sequence_alignment()
    test_algorithm_correctness()
    show_available_phrases() 