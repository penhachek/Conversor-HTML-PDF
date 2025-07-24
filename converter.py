import weasyprint
import os

# Esta parte inteligente para achar o caminho continua a mesma
caminho_do_script = os.path.dirname(os.path.abspath(__file__))
nome_arquivo_html = 'exemplo.html'
caminho_completo_do_html = os.path.join(caminho_do_script, nome_arquivo_html)

try:
    with open(caminho_completo_do_html, 'r', encoding='utf-8') as arquivo:
        html_content = arquivo.read()
    print(f"Sucesso! Arquivo lido de: '{caminho_completo_do_html}'")

except FileNotFoundError:
    print(f"--- ERRO ---")
    print(f"O arquivo não foi encontrado no caminho: '{caminho_completo_do_html}'")
    exit()

# --- A MÁGICA DA CORREÇÃO ACONTECE AQUI ---

print("Criando objeto HTML com endereço base...")
# Ao criar o objeto HTML, passamos o 'base_url'.
# Isso diz ao WeasyPrint: "Se você encontrar um caminho relativo no HTML
# (como para um arquivo CSS ou uma imagem), comece a procurar
# a partir desta pasta base".
html_object = weasyprint.HTML(
    string=html_content,
    base_url=caminho_do_script  # <-- A LINHA MÁGICA!
)

# O resto do código para gerar o PDF
nome_arquivo_pdf = 'PDF_Apresentacao_FiBrasil_Corrigido.pdf'
caminho_completo_do_pdf = os.path.join(caminho_do_script, nome_arquivo_pdf)

print("Iniciando a conversão para PDF...")
# Agora, geramos o PDF a partir do objeto 'html_object' já configurado
html_object.write_pdf(caminho_completo_do_pdf)

# --- FIM DA CORREÇÃO ---

print(f"--- SUCESSO ---")
print(f"Conversão concluída! Verifique o novo arquivo: '{caminho_completo_do_pdf}'.")