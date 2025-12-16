
# feito por M1000 - github.com/curious0w
**versão 0.5**


> **AVISO LEGAL:** Este projeto é estritamente para **fins educacionais e de pesquisa em cibersegurança**. O autor não se responsabiliza por qualquer uso indevido ou atividade ilegal. Use com responsabilidade e apenas em ambientes de teste autorizados.
# Creditos 
**https://github.com/weijarz**
- Usei o ofuscador de payload dele


# Resumo da Ferramenta
Esta ferramenta é um utilitário em Python que fornece um menu interativo para gerar e gerenciar comandos/payloads (modo seguro — não executa payloads automaticamente) e inclui um ofuscador de código (`ofuscador.py`) para reduzir/embaralhar código Python.(obs: O criador do ofuscador python no momento é weijarz )

**Principais componentes**
- `main.py`: interface/menu interativo (modo seguro).
- `ofuscador.py`: ofuscador principal (minificação/obfuscação de código).
- `requirements.txt`: lista de dependências (ex.: `psutil` e ferramentas de desenvolvimento opcionais).
- `versoes/python/escopo_win.py`: versão do payload que foi contida no repositório; **por segurança** o fluxo atual evita executar automaticamente payloads.

**Funcionalidades**
- Seleção de interface/IP disponível e validação de porta.
- Geração de comandos/payloads para revisão (não executa código de rede automaticamente).
- Ofuscação de arquivos Python via `ofuscador.py`.

## Requisitos
- Python 3.8 ou superior.
- `pip` disponível e preferencialmente uso de `venv` (ambiente virtual).
- Pacotes (instalar via `pip install -r requirements.txt`):
	- `psutil>=5.9.0` (usado para listar interfaces de rede)

Dependências de desenvolvimento (opcionais): `pytest`, `flake8`, `mypy` (ver `requirements.txt`).


**Como executar**
- Abra seu terminal Linux.
- Gere o payload (No momento o payload de Python é o melhor!).
- Execute o listener de sua preferencia (vai depender do tipo de ataque que você ira fazer).
- Compile para .exe (no momento não tem essa opção dentro do codigo, mas está tudo certo para a compilação sair de maneira correta).
	- Mande para o alvo desejado e execute o payload.exe.
	- Desfrute! 


**Observação**

- No momento os payloads estão configurados para mostrar o terminal no computador do alvo, então uma configuração deverá ser feita.



## Imagens de detector de virus

![aqui mostra quantos antivirus detectam o payload python, mostrando que o python é mais oculto do que o .C](codiguin/images/imagem_do_payload_py.png)
![aqui mostra quantos antivirus detectam o payload C.](codiguin/images/imagem_do_payload_c.png)