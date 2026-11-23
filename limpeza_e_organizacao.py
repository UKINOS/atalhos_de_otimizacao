"""Responsável por tudo q lide com arquivos
"""

import os
import time



import caminhos_e_variaveis_globais
import entrada_usuario
import ferramentas
import saida_terminal


# Variáveis globais
temp_contador_pastas = 0
temp_contador_arquivos_limpos = -69 # hehe
erros = []


def printar_lista_erros(lista_erros):
  """Printa uma lista de erros

  Args:
      lista_erros (list): lista com todos os erros
  """
  
  if caminhos_e_variaveis_globais.delay > 0:
    limite_erros = max(10, ferramentas.tamanho_terminal()[1] - 13)
  
  else:
    limite_erros = 10
  
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"])
  saida_terminal.apagar_terminal()
  saida_terminal.escrever_buffer([True, False])
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"])
  saida_terminal.desenhar_tela_terminal(formatacao=["FUNDO_AMARELO"], texto=f"\n\nEsses erros são normais:")
  
  for erro_completo, index_cor in lista_erros[-limite_erros:]:
    saida_terminal.lista_alternada(lista=f"{erro_completo}", enumerado=index_cor)

  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"])
  time.sleep(caminhos_e_variaveis_globais.delay)


def delete_recursivo(caminho_pasta: str):
  """Função recursiva usada por limpeza_arquivos_temporarios para limpar um diretório inteiro.

  Args:
    caminho_pasta (str): Caminho da pasta a limpar
  """

  global temp_contador_arquivos_limpos
  global erros
  global temp_contador_pastas

  # Resolve nome correto (%TEMP%, %APPDATA%, etc.)
  caminho_real = os.path.expandvars(caminho_pasta)

  # Como assim não existe?
  if not os.path.exists(caminho_real):
    return

  try:
    diretorio = os.listdir(caminho_real) # Posso entrar?
  except Exception:
    return                               # Se não posso entrar, tchau

  for item in diretorio:
    caminho_item = os.path.join(caminho_real, item)
    try:
      # Não altere a ordem disso, ou vai haver consequências...
      # Sério, altere a ordem e você deleta arquivos importantes em vez do symlink...
      #                                  ______________ Esse cara aqui é importante!
      if os.path.isfile(caminho_item) or os.path.islink(caminho_item):
        os.remove(caminho_item)         # Tchau arquivo
        temp_contador_arquivos_limpos += 1
        
      elif os.path.isdir(caminho_item):
        delete_recursivo(caminho_item)  # Vou terceirizar o trabalho kkkkk
        os.rmdir(caminho_item)          # E vou botar meu nome kkkkkkkk
        temp_contador_arquivos_limpos += 1
        
    except Exception as erro:
      # Sério? Pra que essa rotina gigante? Quer imitar o terminal do Linux é?!
      erros.append([erro, temp_contador_pastas])
      
      printar_lista_erros(erros)
      
      saida_terminal.escrever_buffer([False, True])
      saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)
          

def limpeza_arquivos_temporarios():
  """Limpa arquivos temporários"""

  # Reseta o contador, vai que o usuário executa de novo...
  global erros
  global temp_contador_pastas
  global temp_contador_arquivos_limpos
  

  # SE EXISTE, VAI SER EXTERMINADOOOOOOOOOOOOOOOOOOOOO

  pastas = caminhos_e_variaveis_globais.DELETE_RECURSIVO_TEMPORARIOS

  erros = []
  temp_contador_pastas = 0
  temp_contador_arquivos_limpos = 0
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)

  for caminho in pastas:
    temp_contador_pastas += 1

    # Exibe o progresso das pastas e usa temp_contador_pastas para alternar as cores
    saida_terminal.lista_alternada(lista=f"Limpando {temp_contador_pastas} de {len(pastas)}\n\n{caminho}", enumerado=temp_contador_pastas, save_buffer=(False, True))

    delete_recursivo(caminho)
    saida_terminal.desenhar_tela_terminal(formatacao=["RESET"])
    saida_terminal.apagar_terminal()
    saida_terminal.apagar_buffer([False, True])
    saida_terminal.escrever_buffer([True, False])
    saida_terminal.desenhar_tela_terminal(formatacao=["RESET"])
    printar_lista_erros(erros)
    
  saida_terminal.apagar_terminal()
  saida_terminal.escrever_buffer([True, False])
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"])
  saida_terminal.desenhar_tela_terminal(texto=f"Conseguimos limpar {temp_contador_arquivos_limpos} itens!", formatacao=["TEXTO_VERDE", "FUNDO_PRETO"])

  # Executa a limpeza de disco do Windows no final
  ferramentas.terminal(tipo=1, comando="cleanmgr")

  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)



def desfragmentador():
  """Desfragmenta o disco... duh"""
  
  saida_terminal.desenhar_tela_terminal(formatacao=["NEGRITO", "TEXTO_AMARELO"], texto=f"Selecione um disco (digite apenas a letra): {os.listdrives()}")

  letra_drive = entrada_usuario.entrada(str, [1, 1])
  

  
  saida_terminal.apagar_terminal()
  saida_terminal.escrever_buffer([True, False])
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"])
  saida_terminal.desenhar_tela_terminal(texto=f"Disco: {letra_drive}", add_to_buffer_text=True)
  
  
  saida_terminal.desenhar_tela_terminal(formatacao=["NEGRITO", "TEXTO_PRETO", "FUNDO_BRANCO"], texto="Deseja desfragmentar?")
  saida_terminal.lista_alternada(["Analisar", "Desfragmentar normal", "Desfragmentação agressiva (manda várias flags)"], True)

  
  comando = entrada_usuario.entrada(int, [1, 3])
  
  # Serve para verificar
  if comando == 1:
    ferramentas.terminal(tipo=1, comando=f"defrag {letra_drive.upper()}: /A /V")
    
    
    saida_terminal.desenhar_tela_terminal(formatacao=["NEGRITO", "TEXTO_PRETO", "FUNDO_BRANCO"], texto="Deseja desfragmentar?")
    saida_terminal.lista_alternada(["Não desfragmentar", "Desfragmentar normal", "Desfragmentação agressiva (manda várias flags) - Usar apenas com HDDs"], True)
  
    comando = entrada_usuario.entrada(int, [1, 3])
    
    saida_terminal.apagar_terminal()
    saida_terminal.escrever_buffer([True, False])
    saida_terminal.desenhar_tela_terminal(formatacao=["RESET"])
    
  
  # Inicia como if para garantir que o usuário inicie a desfragmentação...
  if comando == 2:
    ferramentas.terminal(tipo=1, comando=f"defrag {letra_drive.upper()}: /O /U /V")
    
  
  elif comando == 3:
    ferramentas.terminal(tipo=1, comando=f"defrag {letra_drive.upper()}: /X /B /U /V")
    
    
if __name__ == "__main__":
  None