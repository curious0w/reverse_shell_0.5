#feito por M1000 - github.com/curious0w

import zlib
import base64
import sys
import os

def ofuscar_codigo(codigo_fonte: str) -> str:
    """
    Ofusca o código-fonte usando a sequência: Zlib Compressão -> Base64 Encode -> String Reverse.
    
    Args:
        codigo_fonte: O código Python (como string) a ser ofuscado.
        
    Returns:
        O código ofuscado pronto para ser inserido no exec().
    """
    
    # 1. Zlib Compressão
    # Transforma o código em bytes antes de comprimir
    bytes_comprimidos = zlib.compress(codigo_fonte.encode('utf-8'))
    
    # 2. Base64 Codificação
    bytes_codificados = base64.b64encode(bytes_comprimidos)
    
    # 3. Inverter o string (Reverse)
    # Transforma em string de volta para inverter
    string_invertida = bytes_codificados.decode('utf-8')[::-1]
    
    # Formata a string de bytes (com o prefixo 'b') para o código final
    return f"b'{string_invertida}'"

def criar_script_ofuscado(nome_arquivo_entrada: str, nome_arquivo_saida: str):
    """
    Lê o código de entrada, ofusca e escreve o resultado no arquivo de saída.
    """
    try:
        with open(nome_arquivo_entrada, 'r', encoding='utf-8') as f:
            codigo_fonte = f.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo_entrada}' não encontrado.")
        sys.exit(1)
        
    # Realiza a ofuscação
    codigo_ofuscado_str = ofuscar_codigo(codigo_fonte)
    
    # Monta o código Python final que decodificará e executará o código original
    script_final = f"""
# Script Python Ofuscado - Gerado por Gemini
# Logica de decodificacao: Reverso -> Base64 -> Zlib

_ = lambda __: __import__('zlib').decompress(
    __import__('base64').b64decode(__[::-1]))
exec((
    _
)({codigo_ofuscado_str}))
"""

    with open(nome_arquivo_saida, 'w', encoding='utf-8') as f:
        f.write(script_final.strip())
        
    print(f"\n Sucesso! O código ofuscado foi salvo em '{nome_arquivo_saida}'")
    print(f"O tamanho original era: {len(codigo_fonte)} caracteres.")
    print(f"O tamanho ofuscado é: {len(script_final)} caracteres.")


# --- Execução Principal ---
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 gerador_ofuscador.py <arquivo_de_entrada.py> [arquivo_de_saida.py]")
        sys.exit(1)

    arquivo_entrada = sys.argv[1]
    
    if len(sys.argv) > 2:
        arquivo_saida = sys.argv[2]
    else:
        # Padrão: Adiciona '_ofuscado' ao nome do arquivo original
        base, ext = os.path.splitext(arquivo_entrada)
        arquivo_saida = f"{base}_ofuscado{ext}"
        
    criar_script_ofuscado(arquivo_entrada, arquivo_saida)
