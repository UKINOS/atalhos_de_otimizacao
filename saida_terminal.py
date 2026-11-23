"""Responsável por desenhar tudo na tela do terminal
"""
# Import do Python
import sys

# Isso só pra resolver um problema de código ansi... porra windows!
import os
os.system('')



buffer_header = []
buffer_text = []


# O toque não tankou, alinhei tudo kkkkkk
FORMATACAO_E_CORES = {
  # Estilo
  "RESET"          : "\033[0m",
  "NEGRITO"        : "\033[1m",
  "OPACO"          : "\033[2m",
  "ITALICO"        : "\033[3m",
  "SUBLINHADO"     : "\033[4m",
  "INVERTER"       : "\033[7m",
  "RISCADO"        : "\033[9m",
  
  # Cores de texto básicas, primárias e secundárias
  "TEXTO_PRETO"    : "\033[30m",
  "TEXTO_VERMELHO" : "\033[31m",
  "TEXTO_VERDE"    : "\033[32m",
  "TEXTO_AMARELO"  : "\033[33m",
  "TEXTO_AZUL"     : "\033[34m",
  "TEXTO_MAGENTA"  : "\033[35m",
  "TEXTO_CIANO"    : "\033[36m",
  "TEXTO_BRANCO"   : "\033[37m",
  
  # Cores de fundo básicas, primárias e secundárias
  "FUNDO_PRETO"    : "\033[40m",
  "FUNDO_VERMELHO" : "\033[41m",
  "FUNDO_VERDE"    : "\033[42m",
  "FUNDO_AMARELO"  : "\033[43m",
  "FUNDO_AZUL"     : "\033[44m",
  "FUNDO_MAGENTA"  : "\033[45m",
  "FUNDO_CIANO"    : "\033[46m",
  "FUNDO_BRANCO"   : "\033[47m",
}


# Entre criar uma função foda ou armazenar uns kb a mais... prefiro a que é mais fácil :)
COMBINACOES_CORES = [
  # ["TEXTO_BRANCO", "FUNDO_PRETO"], # Retirado pq não destacava
  ["TEXTO_BRANCO", "FUNDO_VERMELHO"],
  ["TEXTO_PRETO",  "FUNDO_VERDE"],
  ["TEXTO_PRETO",  "FUNDO_AMARELO"],
  ["TEXTO_BRANCO", "FUNDO_AZUL"],
  ["TEXTO_BRANCO", "FUNDO_MAGENTA"],
  ["TEXTO_PRETO",  "FUNDO_CIANO"],
  # ["TEXTO_PRETO",  "FUNDO_BRANCO"] # Isso é pra títulos...
]


def escrever_buffer(text_header_binary:list=[False, False]):
  """Escreve os buffers. Não reseta formatação

  Args:
      text_header_binary (list, optional): Possuí dois buffers, com o primeiro escrevendo o cabeçalho, e o segundo escrevendo o texto. Defaults to [False, False].
  """

  if text_header_binary[0]:
    for item in buffer_header:
      desenhar_tela_terminal(texto=item[0], formatacao=item[1], quebra_de_linha=item[2], add_to_buffer_text=False)
    
  if text_header_binary[1]:
    for item in buffer_text:
      desenhar_tela_terminal(texto=item[0], formatacao=item[1], quebra_de_linha=item[2], add_to_buffer_text=False)
      
  # desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)



def delete_last_line():
  """Código para deletar a linha e subir para cima
  Código original em: https://linustechtips.com/topic/1257798-delete-last-line-in-console-python-3/
  """
  
  sys.stdout.write('\x1b[1A')
  sys.stdout.write('\x1b[2K')
  
  
  
def apagar_terminal():
  """Código para deletar a tela inteira, substituindo a partir do buffer
  """
  
  sys.stdout.write('\x1b[2J\x1b[H')

  

def apagar_buffer(text_header_binary:list=[False, False]):
  """Serve para limpar a lista do buffer
  
  Args:
      text_header_binary (list): Possuí um binário de duas posições, com a primeiro limpando o buffer de cabeçalho e o segundo limpando o buffer de texto. Default to [True, False]
  
  """
  
  if text_header_binary[0]:
    buffer_header.clear()
    
  if text_header_binary[1]:
    buffer_text.clear()
    
  # Isso é inutil, delete se precisar de alguns bytes...
  if not text_header_binary[0] and not text_header_binary[1]:
    # Mais inutil que meu pen- ;-;
    
    # drive de 128mb, né?
    # NÉ?!
    # - Gemini, vendo eu tentar analisar uma lista que eu tinha acabado de deletar kkkkkkkkkkkkkkkk
    
    None
    
    
def lista_alternada(lista:list|str, enumerado:bool|int, save_buffer:tuple=(False, False)):
  """Cansei de ficar escrevendo isso em cada linha de código, então transformei na sua própria função... Reseta formatação.

  Args:
      lista (list or str): Lista de itens q ele vai printar / string a colorir
      enumerado (bool or int, optional): Os itens devem ser numerados / qual a próxima cor?
      save_buffer (tuple -> (header, text)): Coisas bestas q notei depois...
  """
  
  if type(lista) == list:
    for iterador in range(0, len(lista)):
      desenhar_tela_terminal(formatacao=COMBINACOES_CORES[iterador % len(COMBINACOES_CORES)], quebra_de_linha=False)
      
      if enumerado:
        desenhar_tela_terminal(texto=f"{iterador + 1}. ", quebra_de_linha=False, add_to_buffer_header=save_buffer[0], add_to_buffer_text=save_buffer[1])
    
      desenhar_tela_terminal(texto=lista[iterador], add_to_buffer_header=save_buffer[0], add_to_buffer_text=save_buffer[1])
      
      
  if type(lista) == str:
    desenhar_tela_terminal(texto=lista, formatacao=COMBINACOES_CORES[enumerado % len(COMBINACOES_CORES)], add_to_buffer_header=save_buffer[0], add_to_buffer_text=save_buffer[1])
    
  
  desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)
    
  
  
def desenhar_tela_terminal(texto:str="", formatacao:list=[], quebra_de_linha:bool=True, add_to_buffer_text:bool=False, add_to_buffer_header:bool=False):
  """Código responsável por desenhar as coisas no terminal. Não reseta formatação.

  Args:
      texto (str): Texto a ser printado. Default to ""
      formatacao (list): Formatação do texto. Default to []
      quebra_de_linha (bool): \n no final da frase?. Default to True
      add_to_buffer_text (bool): Adiciona ao buffer, usado quando a tela é limpa. Default to True
      add_to_buffer_header (bool): Adiciona ao buffer, usado quando a tela é limpa. Default to False

  Returns:
      list: Retorna uma lista, com o primeiro valor sendo um código de identificação interno e o segundo sendo o motivo:
      [0, ""] - Sucesso
      [1, ""] - Falha geral (sem ideia)
      [2, ""] - Falha de programador (erro do programador)
      
  """
  
  # Tratamento strings
  string_completa = []
  
  # Buffer buferizando
  if add_to_buffer_text:
    buffer_text.append([texto, formatacao, quebra_de_linha])
    
  if add_to_buffer_header:
    buffer_header.append([texto, formatacao, quebra_de_linha])

  try:
    for item in formatacao:
      if FORMATACAO_E_CORES.get(item) != None:
        string_completa.append(FORMATACAO_E_CORES.get(item))
        
    string_completa.append(texto)

    if quebra_de_linha:
      string_completa.append("\n")
    
    string_completa = ''.join(string_completa)
    
    print(string_completa, flush=True, end="")


    return [0, "Sucesso"]
  
  
  except Exception as erro:
    return [1, erro]
        


if __name__ == "__main__":
  desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)
  
  desenhar_tela_terminal(texto="Código teste ativado: ", formatacao=["TEXTO_VERDE", "FUNDO_PRETO"], quebra_de_linha=False)
  
  desenhar_tela_terminal(texto="Black on White", formatacao=["TEXTO_PRETO", "FUNDO_BRANCO"], quebra_de_linha=True)
  
  desenhar_tela_terminal(texto="Eu ainda to com o efeito original! ME RESETA AAAAAAAAAAA", quebra_de_linha=True)
  
  desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)
  
  desenhar_tela_terminal(texto="Obrigado...")
  
  apagar_terminal(reescrever=True, text_header_binary=[False, True])