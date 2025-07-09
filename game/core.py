import pygame
import random
import time
from constants import *
from sequence_alignment import calculate_similarity, get_feedback, shuffle_string

pygame.init()

FONT_LARGE = pygame.font.SysFont("arial", 32)
FONT_MEDIUM = pygame.font.SysFont("arial", 24)
FONT_SMALL = pygame.font.SysFont("arial", 18)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sequence Alignment Game")

class GameState:
    def __init__(self):
        self.target_phrase = ""
        self.current_phrase = ""
        self.shuffled_phrase = ""
        self.difficulty = "Médio"
        self.language = "Português"
        self.attempts = 0
        self.start_time = time.time()
        self.similarity = 0.0
        self.distance = 0
        self.feedback = ""
        self.game_won = False
        self.game_over = False
        self.selected_char_index = -1
        self.record_times = []
        self.show_language_menu = True
        self.victory_time = None
        
    def new_game(self):
        self.target_phrase = random.choice(PHRASES[self.language])
        difficulty_value = DIFFICULTY_LEVELS[self.difficulty]
        self.shuffled_phrase = shuffle_string(self.target_phrase, difficulty_value)
        self.current_phrase = self.shuffled_phrase
        self.attempts = 0
        self.start_time = time.time()
        self.game_won = False
        self.game_over = False
        self.selected_char_index = -1
        self.victory_time = None
        self.update_feedback()
        
    def update_feedback(self):
        self.feedback, self.similarity, self.distance = get_feedback(self.target_phrase, self.current_phrase)
        if self.similarity == 1.0 and not self.game_won:
            self.game_won = True
            self.victory_time = time.time() - self.start_time
        
    def swap_chars(self, index1, index2):
        if 0 <= index1 < len(self.current_phrase) and 0 <= index2 < len(self.current_phrase):
            chars = list(self.current_phrase)
            chars[index1], chars[index2] = chars[index2], chars[index1]
            self.current_phrase = ''.join(chars)
            self.attempts += 1
            self.update_feedback()
        
    def check_time_limit(self):
        if self.game_won and self.victory_time is not None:
            return self.victory_time
        elapsed_time = time.time() - self.start_time
        if elapsed_time > TIME_LIMIT:
            self.game_over = True
        return elapsed_time

game_state = GameState()

def draw_phrase_box(phrase, x, y, width, height, title, color=WHITE, selected_index=-1):
    pygame.draw.rect(WIN, DARK_GRAY, (x, y, width, height))
    pygame.draw.rect(WIN, color, (x, y, width, height), 2)
    
    title_surface = FONT_SMALL.render(title, True, WHITE)
    WIN.blit(title_surface, (x + 10, y + 10))
    
    if phrase:
        block_width = 25
        block_height = 35
        block_margin = 3
        
        total_width = len(phrase) * (block_width + block_margin) - block_margin
        start_x = x + (width - total_width) // 2
        start_y = y + (height - block_height) // 2 + 20
        
        for i, char in enumerate(phrase):
            char_x = start_x + i * (block_width + block_margin)
            char_y = start_y
            
            if i == selected_index:
                block_color = BLOCK_SELECTED
                text_color = BLACK
            elif char == ' ':
                block_color = BLOCK_SPACE
                text_color = GRAY
            else:
                block_color = BLOCK_NORMAL
                text_color = BLACK
            
            pygame.draw.rect(WIN, block_color, (char_x, char_y, block_width, block_height))
            pygame.draw.rect(WIN, WHITE, (char_x, char_y, block_width, block_height), 2)
            
            if char == ' ':
                char_surface = FONT_SMALL.render('_', True, text_color)
            else:
                char_surface = FONT_MEDIUM.render(char, True, text_color)
            
            text_rect = char_surface.get_rect(center=(char_x + block_width // 2, char_y + block_height // 2))
            WIN.blit(char_surface, text_rect)

def draw_language_menu():
    WIN.fill(BLACK)
    
    title = FONT_LARGE.render("Escolha o Idioma / Choose Language / Choisir la Langue", True, WHITE)
    title_rect = title.get_rect(center=(WIDTH // 2, 100))
    WIN.blit(title, title_rect)
    
    languages = list(PHRASES.keys())
    button_height = 60
    button_width = 300
    start_y = 200
    
    for i, language in enumerate(languages):
        y = start_y + i * (button_height + 20)
        x = (WIDTH - button_width) // 2
        
        color = GREEN if language == game_state.language else BLUE
        
        pygame.draw.rect(WIN, color, (x, y, button_width, button_height))
        pygame.draw.rect(WIN, WHITE, (x, y, button_width, button_height), 2)
        
        text = FONT_MEDIUM.render(language, True, WHITE)
        text_rect = text.get_rect(center=(x + button_width // 2, y + button_height // 2))
        WIN.blit(text, text_rect)
    
    instructions = [
        "Clique em um idioma para selecionar",
        "Click on a language to select",
        "Cliquez sur une langue pour sélectionner"
    ]
    
    for i, instruction in enumerate(instructions):
        text = FONT_SMALL.render(instruction, True, LIGHT_GRAY)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - 100 + i * 25))
        WIN.blit(text, text_rect)
    
    pygame.display.update()

def handle_language_menu_click(pos):
    languages = list(PHRASES.keys())
    button_height = 60
    button_width = 300
    start_y = 200
    
    for i, language in enumerate(languages):
        y = start_y + i * (button_height + 20)
        x = (WIDTH - button_width) // 2
        
        if (x <= pos[0] <= x + button_width and y <= pos[1] <= y + button_height):
            game_state.language = language
            game_state.show_language_menu = False
            game_state.new_game()
            return True
    return False

def draw_controls():
    instructions = [
        "Clique em duas letras para trocá-las",
        "R = Novo jogo | D = Mudar dificuldade | L = Mudar idioma",
        "ESC = Sair"
    ]
    
    y_offset = HEIGHT - 100
    for i, instruction in enumerate(instructions):
        text = FONT_SMALL.render(instruction, True, LIGHT_GRAY)
        WIN.blit(text, (20, y_offset + i * 25))

def draw_stats():
    elapsed_time = game_state.check_time_limit()
    
    stats = [
        f"Idioma: {game_state.language}",
        f"Dificuldade: {game_state.difficulty}",
        f"Tentativas: {game_state.attempts}/{MAX_ATTEMPTS}",
        f"Tempo: {elapsed_time:.1f}s/{TIME_LIMIT}s",
        f"Similaridade: {game_state.similarity:.1%}",
        f"Distância: {game_state.distance}"
    ]
    
    for i, stat in enumerate(stats):
        text = FONT_SMALL.render(stat, True, WHITE)
        WIN.blit(text, (20, 20 + i * 25))

def draw_feedback():
    if game_state.feedback:
        if game_state.similarity == 1.0:
            color = PERFECT_COLOR
        elif game_state.similarity >= 0.7:
            color = GOOD_COLOR
        elif game_state.similarity >= 0.4:
            color = OK_COLOR
        else:
            color = BAD_COLOR
            
        feedback_surface = FONT_MEDIUM.render(game_state.feedback, True, color)
        feedback_rect = feedback_surface.get_rect(center=(WIDTH // 2, 150))
        WIN.blit(feedback_surface, feedback_rect)

def draw_game():
    WIN.fill(BLACK)
    
    title = FONT_LARGE.render("Sequence Alignment Game", True, WHITE)
    title_rect = title.get_rect(center=(WIDTH // 2, 50))
    WIN.blit(title, title_rect)
    
    draw_phrase_box(
        game_state.current_phrase, 
        50, 200, WIDTH - 100, 120, 
        f"Reorganize as letras para formar a frase correta ({game_state.language})", 
        BLUE,
        game_state.selected_char_index
    )
    
    draw_stats()
    draw_feedback()
    draw_controls()
    
    pygame.display.update()

def handle_mouse_click(pos):
    phrase_box_x, phrase_box_y = 50, 200
    phrase_box_width, phrase_box_height = WIDTH - 100, 120
    
    if (phrase_box_x <= pos[0] <= phrase_box_x + phrase_box_width and
        phrase_box_y <= pos[1] <= phrase_box_y + phrase_box_height):
        
        block_width = 25
        block_height = 35
        block_margin = 3
        
        total_width = len(game_state.current_phrase) * (block_width + block_margin) - block_margin
        start_x = phrase_box_x + (phrase_box_width - total_width) // 2
        start_y = phrase_box_y + (phrase_box_height - block_height) // 2 + 20
        
        for i in range(len(game_state.current_phrase)):
            char_x = start_x + i * (block_width + block_margin)
            char_y = start_y
            
            if (char_x <= pos[0] <= char_x + block_width and 
                char_y <= pos[1] <= char_y + block_height):
                
                if game_state.selected_char_index == -1:
                    game_state.selected_char_index = i
                else:
                    if game_state.selected_char_index != i:
                        game_state.swap_chars(game_state.selected_char_index, i)
                    game_state.selected_char_index = -1
                break

def victory_screen():
    WIN.fill(BLACK)
    
    victory_text = FONT_LARGE.render("Parabéns! Você venceu!", True, GREEN)
    victory_rect = victory_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    WIN.blit(victory_text, victory_rect)
    
    correct_text = FONT_MEDIUM.render(f"Frase correta: {game_state.target_phrase}", True, WHITE)
    correct_rect = correct_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60))
    WIN.blit(correct_text, correct_rect)
    
    time_taken = game_state.victory_time if game_state.victory_time is not None else (time.time() - game_state.start_time)
    stats_text = FONT_MEDIUM.render(f"Tempo: {time_taken:.2f}s | Tentativas: {game_state.attempts}", True, WHITE)
    stats_rect = stats_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
    WIN.blit(stats_text, stats_rect)
    
    game_state.record_times.append(time_taken)
    game_state.record_times.sort()
    top_times = game_state.record_times[:5]
    
    records_text = FONT_MEDIUM.render("Melhores tempos:", True, WHITE)
    records_rect = records_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
    WIN.blit(records_text, records_rect)
    
    for i, t in enumerate(top_times):
        record_text = FONT_SMALL.render(f"#{i+1}: {t:.2f}s", True, WHITE)
        record_rect = record_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50 + i * 25))
        WIN.blit(record_text, record_rect)
    
    continue_text = FONT_SMALL.render("Pressione R para jogar novamente ou ESC para sair", True, LIGHT_GRAY)
    continue_rect = continue_text.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    WIN.blit(continue_text, continue_rect)
    
    pygame.display.update()

def game_over_screen():
    WIN.fill(BLACK)
    
    game_over_text = FONT_LARGE.render("Game Over!", True, RED)
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 80))
    WIN.blit(game_over_text, game_over_rect)
    
    correct_text = FONT_MEDIUM.render(f"Frase correta: {game_state.target_phrase}", True, WHITE)
    correct_rect = correct_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
    WIN.blit(correct_text, correct_rect)
    
    reason_text = FONT_MEDIUM.render("Tempo esgotado ou muitas tentativas", True, WHITE)
    reason_rect = reason_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    WIN.blit(reason_text, reason_rect)
    
    continue_text = FONT_SMALL.render("Pressione R para tentar novamente ou ESC para sair", True, LIGHT_GRAY)
    continue_rect = continue_text.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    WIN.blit(continue_text, continue_rect)
    
    pygame.display.update()

def change_difficulty():
    difficulties = list(DIFFICULTY_LEVELS.keys())
    current_index = difficulties.index(game_state.difficulty)
    next_index = (current_index + 1) % len(difficulties)
    game_state.difficulty = difficulties[next_index]

def change_language():
    game_state.show_language_menu = True

def game_loop():
    clock = pygame.time.Clock()
    running = True
    
    while running:
        clock.tick(60)
        
        if game_state.show_language_menu:
            draw_language_menu()
        elif game_state.game_won:
            victory_screen()
        elif game_state.game_over or game_state.attempts >= MAX_ATTEMPTS:
            game_state.game_over = True
            game_over_screen()
        else:
            draw_game()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    if not game_state.show_language_menu:
                        game_state.new_game()
                elif event.key == pygame.K_d:
                    if not game_state.show_language_menu:
                        change_difficulty()
                        game_state.new_game()
                elif event.key == pygame.K_l:
                    if not game_state.show_language_menu:
                        change_language()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_state.show_language_menu:
                    handle_language_menu_click(event.pos)
                elif not game_state.game_won and not game_state.game_over:
                    handle_mouse_click(event.pos)
    
    pygame.quit()

