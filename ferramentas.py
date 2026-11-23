"""Ferramentas para lidar com sistemas do windows por aqui...
"""

import ctypes
import html
from html.parser import HTMLParser
import os
import pathlib
import sys
import subprocess
import shutil
import traceback



import entrada_usuario
import saida_terminal



local_de_erro = pathlib.Path.home() / "Documents" / "atalhos_de_otimizacao" / "erros.txt"



# Sim, usei IA. Ainda não sei usar classes ;-;
# Vou chorar ;---;
class _LeitorTextoHTML(HTMLParser):          # Recebe os eventos enquanto o HTML é lido.
  def __init__(self):
    super().__init__(convert_charrefs=True)  # Inicializa o parser e converte entidades HTML.
    self.partes = []                         # Guarda os trechos de texto encontrados.
    self.ignorar = 0                         # Maior que zero enquanto estamos em style/script.

  def handle_starttag(self, tag, atributos): # Chamado ao encontrar uma tag de abertura.
    if tag in ("script", "style"):
      self.ignorar += 1                      # Ignora o conteúdo de CSS e JavaScript.
    elif not self.ignorar and tag in ("br", "div", "h1", "h2", "p", "tr"):
      self.partes.append("\n")               # Separa blocos e linhas da tabela.
    elif not self.ignorar and tag in ("td", "th"):
      self.partes.append(" ")                # Separa células da tabela.

  def handle_endtag(self, tag):              # Chamado ao encontrar uma tag de fechamento.
    if tag in ("script", "style"):
      self.ignorar -= 1                      # Terminou o bloco de CSS/JavaScript a ignorar.
    elif not self.ignorar and tag in ("div", "h1", "h2", "p", "tr"):
      self.partes.append("\n")               # Separa o fim do bloco ou da linha.
    elif not self.ignorar and tag in ("td", "th"):
      self.partes.append(" ")                # Separa esta célula da próxima.

  def handle_data(self, data):
    if not self.ignorar:
      self.partes.append(data)               # Guarda o texto encontrado entre as tags.



def deteccao_de_erro(nome:str, log:str, parada:bool=False):
  """Gera um erro no código

  Args:
      nome (str): _description_
      log (str): _description_
      parada (bool, optional): _description_. Defaults to False.
  """
  
  # Obrigado Gemini (Hydrogen)!
  # Essa coisa pega o nome do arquivo e linha do erro...
  # Perai, esse é um erro total ou básico?
  if isinstance(log, BaseException):
    ultimo_passo = traceback.extract_tb(log.__traceback__)[-1]
    arquivo = os.path.basename(ultimo_passo.filename)
    detalhe_erro = f"{arquivo} (linha {ultimo_passo.lineno} em {ultimo_passo.name}): {log}"
  
  # Ata, menos mal
  else:
    detalhe_erro = log
  
  os.makedirs(os.path.dirname(local_de_erro), exist_ok=True)
  
  saida_terminal.desenhar_tela_terminal(formatacao=["NEGRITO", "TEXTO_BRANCO", "FUNDO_VERMELHO"], texto=nome)
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET", "TEXTO_PRETO", "FUNDO_AMARELO"], texto=detalhe_erro)
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"])
  
  with open(local_de_erro, 'a', encoding='utf-8') as log_de_erros:
    log_de_erros.write(f"\n[{terminal(tipo=2, comando="date /t")[-1]} {terminal(tipo=2, comando="time /t")[-1]}] - {"CRITICAL - " if parada else ""}{nome}\n{detalhe_erro}\n")
    
    for loop in range(13):
      saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)
      saida_terminal.delete_last_line()
  
  if parada:
    saida_terminal.desenhar_tela_terminal(formatacao=["RESET", "TEXTO_VERDE"], texto="O erro está forçando o encerramento imediato do código...")
    terminal(tipo=1, comando="pause")
    
    saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)
    sys.exit(1)

  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)


def tamanho_terminal():
  """Serve para dizer o tamanho da tela do terminal

  Returns:
      list: Retorna uma tuple com 2 valores: (colunas, linhas)
  """
  
  colunas, linhas = shutil.get_terminal_size(fallback=(120, 30))
  
  return (colunas, linhas)


def eh_admin():
  """Simples, ela só responde se o terminal é admin

  Returns:
      bool: Retorna True ou False pra "sua pergunta"
  """
  
  try:
    return ctypes.windll.shell32.IsUserAnAdmin() != 0
  except Exception:
    return False
  
  
# Também usei IA, não sabia o que tava fazendo com a classe, muito menos vou saber como utilizar...
def html_filtragem(texto_html: str) -> str:
  leitor = _LeitorTextoHTML()               # Cria um leitor novo para este HTML.
  leitor.feed(texto_html)                   # Entrega o HTML; o leitor processa tags e texto.
  leitor.close()                            # Avisa que não há mais HTML para processar.

  texto_extraido = "".join(leitor.partes)   # Junta os trechos de texto coletados.
  linhas_limpas = []                        # Vai guardar as linhas já limpas.
  for linha in texto_extraido.splitlines(): # Percorre cada linha extraída.
    palavras = linha.split()                # Separa palavras e descarta espaços repetidos.
    linha_limpa = " ".join(palavras)        # Junta as palavras com apenas um espaço.
    if linha_limpa:                         # Ignora linhas vazias.
      linhas_limpas.append(linha_limpa)     # Guarda a linha que tem texto.

  return "\n".join(linhas_limpas)           # Devolve as linhas separadas por quebras.


def terminal(comando:str, tipo:int=1, salvar_buffer_text:bool = False):
  """Código para interação no terminal do Windows

  Args:
      comando (str): O comando a ser enviado para o terminal
      tipo (int, optional): O tipo de terminal que se deve utilizar, 1 permite interação do usuário ao terminal, 2 permite ler a saída. Defaults to 1.

  Returns:
      bool:list: no tipo 1 retorna o código, no tipo 2 retorna o que saiu no terminal, com o texto dividido por espaços no terminal: ola mundo -> ["ola", "mundo"]
  """
  
  # Coisinha besta pra formatação, pode ignorar kkkkkkk
  try:
    teste_administrador = ctypes.windll.shell32.IsUserAnAdmin() != 0
  except Exception:
    teste_administrador = False
  
  if teste_administrador:
    FORMATACAO = "Administrador"
        
  else:
    FORMATACAO = "Usuário"
    
  saida_terminal.desenhar_tela_terminal(formatacao=["TEXTO_PRETO", "FUNDO_VERDE"])
  
  if tipo == 1:
    saida_terminal.desenhar_tela_terminal(texto=f"\n{FORMATACAO}\\python_{sys.version.split()[0]}\\atalhos_de_otimizacao\\terminal> {comando}", quebra_de_linha=True, add_to_buffer_text=salvar_buffer_text)
    
    
    terminal = os.system(comando)
    
    
    saida_terminal.desenhar_tela_terminal(formatacao=["RESET"])
    return terminal
  
  
  if tipo == 2:
    saida_terminal.desenhar_tela_terminal(texto=f"\n{FORMATACAO}\\python_{sys.version.split()[0]}\\atalhos_de_otimizacao\\headless_terminal> {comando}", quebra_de_linha=True, add_to_buffer_text=salvar_buffer_text)
    
        
    terminal = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
   
   
    stdout, stderr = terminal.communicate()
    
    filtro_stdout = stdout.decode('cp850', errors='replace')
    filtro_stderr = stderr.decode('cp850', errors='replace')


    if terminal.returncode == 0:
      saida_terminal.desenhar_tela_terminal(texto=filtro_stdout, quebra_de_linha=True, add_to_buffer_text=salvar_buffer_text)
      saida_terminal.desenhar_tela_terminal(formatacao=["RESET"])
      return filtro_stdout.strip().split()
    
    else:
      # Obrigado pela ideia Gemini (4 Hydrogen)
      # Caso stderr venha vazio em erro, retorna stdout
      if filtro_stderr.strip():
        mensagem_erro = filtro_stderr
        
      else:
        mensagem_erro = filtro_stdout
        
      
      saida_terminal.desenhar_tela_terminal(texto=mensagem_erro, quebra_de_linha=True, add_to_buffer_text=salvar_buffer_text)
      saida_terminal.desenhar_tela_terminal(formatacao=["RESET"])
      return mensagem_erro.strip().split()
    
    
    
def regedit(local:str, nome_chave:str, acao:str="QUERY", valor:str=""):
  """Responsável por lidar com o regedit. Ele não retorna até confirmarem q pode...

  Args:
      local (str): Onde está essa chave?
      nome_chave (str): Qual o nome da chave?
      acao (str, optional): O que devo fazer? Defaults to "QUERY".
      valor (str, optional): Se for ADD, qual valor devo definir? Defaults to "".

  Returns:
      _type_: _description_
  """

  forcar_acao = None
  modo = -69 # HEHEHE
  
  
  # Se for uma ação que não retorna nada, apenas execute normalmente
  if acao.upper() == "ADD" or acao.upper() == "DELETE":
    modo = 1
    forcar_acao = True
    
  else:
    modo = 2
    forcar_acao = False
    
  resposta = terminal(tipo=modo, comando=f"REG {acao.upper()} \"{local.upper()}\" /v \"{nome_chave}\" {valor} {"/f" if forcar_acao else ""}")

  return resposta


def servicos_windows(nome_servico:str, acao:int=0):
  """Responsável por lidar com o terminal

  Args:
      nome_servico (str): Nome do serviço a procurar...
      acao (int, optional): Descrição das açoes abaixo. Defaults to 0.
      0 - query
      1 - start
      2 - stop

  Returns:
      0 - bool|str: Retorna True ou False para rodando ou não respectivamente, se resultado inesperado retorna resposta inteira
      1 e 2 - None: Simplesmente executa e tu confia no comando kkkk (irresponsabilidade, eu sei)
  """
  
  if acao == 0:
    resposta = terminal(tipo=2, comando=f"sc query \"{nome_servico}\"")
    
    if "RUNNING" in resposta:
      return True
    
    elif "STOPPED" in resposta:
      return False
    
    else:
      return " ".join(resposta)
    
    
  elif acao == 1:
    terminal(tipo=1, comando=f"sc config \"{nome_servico}\" start= auto")
    terminal(tipo=1, comando=f"net start \"{nome_servico}\" /y") # Usando net pra ele aguardar a inicialização

  elif acao == 2:
    terminal(tipo=1, comando=f"sc config \"{nome_servico}\" start= disabled")
    terminal(tipo=1, comando=f"net stop \"{nome_servico}\" /y") # Usando net pra ele aguardar a finalização


def chkdsk(disco_sistema:bool=False):
  """Verifica o disco do sistema

  Args:
      disco_sistema (bool, optional): flag usada no caso de {insira nome depois}, não é necessário mexer nela... Defaults to False.
  """
  
  if disco_sistema:
    letra_drive = "C"
    
  else:
    saida_terminal.desenhar_tela_terminal(formatacao=["NEGRITO", "TEXTO_AMARELO"], texto=f"Selecione um disco (digite apenas a letra): {os.listdrives()}")
    
    letra_drive = entrada_usuario.entrada(str, [1, 1])
  

  saida_terminal.apagar_terminal()
  saida_terminal.escrever_buffer([True, False])
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"])
  saida_terminal.desenhar_tela_terminal(texto=f"Disco: {letra_drive}", add_to_buffer_text=True)

  
  tipo_armazenamento = terminal(tipo=2, comando=f"powershell -NoProfile -Command \"(Get-Volume -DriveLetter {letra_drive} -ErrorAction SilentlyContinue).FileSystem\"")
  
  
  if "NTFS" in tipo_armazenamento:
    flags = "/b /x"
    
  else:
    flags = "/r /x"
    
  
  terminal(tipo=1, comando=f"chkdsk {letra_drive}: {flags}")
  

if __name__ == "__main__":
  modo = input("Modo? ")
  comando = input("Comando? ")
  
  print(terminal(tipo=int(modo), comando=comando))