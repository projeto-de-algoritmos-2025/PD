import random

def levenshtein_distance(str1, str2):
    m, n = len(str1), len(str2)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1]
                )
    
    return dp[m][n]

def calculate_similarity(str1, str2):
    if not str1 and not str2:
        return 1.0
    if not str1 or not str2:
        return 0.0
    
    distance = levenshtein_distance(str1, str2)
    max_length = max(len(str1), len(str2))
    similarity = 1 - (distance / max_length)
    return similarity

def get_feedback(target, current):
    similarity = calculate_similarity(target, current)
    distance = levenshtein_distance(target, current)
    
    if similarity == 1.0:
        return "Perfeito! Frase correta!", similarity, distance
    
    if similarity >= 0.9:
        return f"Excelente! {distance} erro(s) restante(s)", similarity, distance
    elif similarity >= 0.7:
        return f"Muito bom! {distance} erro(s) para corrigir", similarity, distance
    elif similarity >= 0.5:
        return f"Bom progresso! {distance} erro(s) encontrado(s)", similarity, distance
    elif similarity >= 0.3:
        return f"Continue tentando! {distance} erro(s) para corrigir", similarity, distance
    else:
        return f"Você pode fazer melhor! {distance} erro(s) encontrado(s)", similarity, distance

def shuffle_string(text, difficulty=0.5):
    if difficulty <= 0:
        return text
    
    chars = list(text)
    n = len(chars)
    
    num_swaps = int(n * difficulty)
    
    for _ in range(num_swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        chars[i], chars[j] = chars[j], chars[i]
    
    return ''.join(chars) 