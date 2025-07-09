#!/usr/bin/env python3
"""
Script de instalação e execução do Sequence Alignment Game
"""

import subprocess
import sys
import os

def check_pygame():
    """Verifica se o pygame está instalado"""
    try:
        import pygame
        print("✓ Pygame já está instalado")
        return True
    except ImportError:
        print("✗ Pygame não está instalado")
        return False

def install_pygame():
    """Instala o pygame se necessário"""
    print("Instalando pygame...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame>=2.0.0"])
        print("✓ Pygame instalado com sucesso!")
        return True
    except subprocess.CalledProcessError:
        print("✗ Erro ao instalar pygame")
        return False

def run_demo():
    """Executa a demonstração do algoritmo"""
    print("\n" + "="*50)
    print("EXECUTANDO DEMONSTRAÇÃO DO ALGORITMO")
    print("="*50)
    
    try:
        subprocess.run([sys.executable, "example.py"])
    except FileNotFoundError:
        print("✗ Arquivo example.py não encontrado")

def run_game():
    """Executa o jogo principal"""
    print("\n" + "="*50)
    print("INICIANDO O SEQUENCE ALIGNMENT GAME")
    print("="*50)
    
    try:
        subprocess.run([sys.executable, "main.py"])
    except FileNotFoundError:
        print("✗ Arquivo main.py não encontrado")

def main():
    """Função principal"""
    print("SEQUENCE ALIGNMENT GAME - INSTALADOR")
    print("="*50)
    
    # Verificar e instalar pygame
    if not check_pygame():
        if not install_pygame():
            print("Não foi possível instalar o pygame. Saindo...")
            return
    
    # Menu de opções
    while True:
        print("\nOpções:")
        print("1. Executar demonstração do algoritmo")
        print("2. Jogar o jogo")
        print("3. Sair")
        
        choice = input("\nEscolha uma opção (1-3): ").strip()
        
        if choice == "1":
            run_demo()
        elif choice == "2":
            run_game()
        elif choice == "3":
            print("Obrigado por usar o Sequence Alignment Game!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main() 