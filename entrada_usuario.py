"""Responsável por lidar com qualquer coisa quue envolva a entrada (input) do usuário
"""
# Código externo
import saida_terminal



def entrada(tipo_entrada:type=str|int, limite_caracteres_numero:list=[1, 999]):
  """_summary_

  Args:
      tipo_entrada (type, optional): O tipo de entrada que o código deve receber. Defaults to str.
      limite_caraceres_numero (list, optional): O tamanho mínimo ou máximo da string ou do int. Defaults to [1, 999].

  Returns:
      str or int: Retorna o valor definido em tipo_entrada com a margem de limite_caracteres_numero.
  """
  
  errou = False
  
  while True:
    saida_terminal.desenhar_tela_terminal(texto="\ninput: ", formatacao=["TEXTO_PRETO", "FUNDO_VERDE"], quebra_de_linha=False)
    resposta = input().strip()
    
    if tipo_entrada == int:
      if not resposta.isdigit():
        saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=not(errou))
        errou = True
        
        saida_terminal.delete_last_line()
        saida_terminal.delete_last_line()
        
        saida_terminal.desenhar_tela_terminal(texto=f"Tipo errado: esperava número", quebra_de_linha=False, add_to_buffer_text=False)
        continue
      
      if limite_caracteres_numero[0] > int(resposta) or int(resposta) > limite_caracteres_numero[1]:
        saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=not(errou))
        errou = True
        
        saida_terminal.delete_last_line()
        saida_terminal.delete_last_line()
        
        saida_terminal.desenhar_tela_terminal(texto=f"Tamanho errado: esperava entre {limite_caracteres_numero[0]} e {limite_caracteres_numero[1]}, reccebeu {resposta}", formatacao=["TEXTO_BRANCO", "FUNDO_VERMELHO"], quebra_de_linha=False, add_to_buffer_text=False)
        continue

      saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=True)
      return int(resposta)
    
    if tipo_entrada == str:
      if limite_caracteres_numero[0] > len(resposta.strip()) or len(resposta.strip()) > limite_caracteres_numero[1]:
        saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=not(errou))
        errou = True
        
        saida_terminal.delete_last_line()
        saida_terminal.delete_last_line()
        
        saida_terminal.desenhar_tela_terminal(texto=f"Tamanho errado: esperava entre {limite_caracteres_numero[0]} e {limite_caracteres_numero[1]}, recebeu {len(resposta)}", formatacao=["TEXTO_BRANCO", "FUNDO_VERMELHO"], quebra_de_linha=False, add_to_buffer_text=False)
        continue
      
      saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=True)
      return resposta.strip()
    
    
def menu_escolha(lista:dict, nome:str):
  """Ajuda em um menu de escolhas
  Nota: Não possuí dependencia com saida_terminal.lista_alternada()

  Args:
      lista (dict): A lista com menu e submenu em chaves e lista {a, [b, c]}
      nome (str): O nome a ser exibido no topo...
      
  Returns:
      list: Retorna uma lista com [menu, submenu]
  """
  
                   # Menu, Submenu - Ambos serão int
  escolhas_feitas = [None, None]
                   

  
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)
  saida_terminal.apagar_terminal()
  saida_terminal.desenhar_tela_terminal(texto=nome, formatacao=["TEXTO_PRETO",  "FUNDO_BRANCO"], add_to_buffer_text=False, add_to_buffer_header=True)
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)
  

  iterador = 1
  for menu, submenu in lista.items():
    saida_terminal.lista_alternada(lista=f"{iterador}. {menu}", enumerado=iterador)
    iterador += 1
    
  
  escolhas_feitas[0] = entrada(int, [1, iterador - 1])
  
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)
  saida_terminal.apagar_terminal()
  saida_terminal.escrever_buffer([True, False])
  
  iterador = 1
  for menu, submenu in lista.items():
    if iterador == escolhas_feitas[0]:
      saida_terminal.lista_alternada(lista=f"{iterador}. {menu}", enumerado=iterador)
      
      iterador = 1
      for itens in submenu:
        saida_terminal.lista_alternada(lista=f" |-> {iterador}. {itens}", enumerado=iterador)
        iterador += 1
        
      
      escolhas_feitas[1] = entrada(int, [1, iterador - 1])
      break
    
    iterador += 1
      
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)
  saida_terminal.apagar_terminal()
  saida_terminal.escrever_buffer([True, False])
  
  iterador = 1
  for menu, submenu in lista.items():
    if iterador == escolhas_feitas[0]:
      escolhas_feitas[0] = menu
      saida_terminal.lista_alternada(lista=f"{iterador}. {menu}", enumerado=iterador, save_buffer=(True, False))
      iterador = 1
      for itens in submenu:
        if iterador == escolhas_feitas[1]:
          saida_terminal.lista_alternada(lista=f" |-> {iterador}. {itens}", enumerado=iterador, save_buffer=(True, False))
          escolhas_feitas[1] = itens
          break
        
        iterador += 1
    iterador += 1
  
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], add_to_buffer_header=True)
  return escolhas_feitas


if __name__ == "__main__":
  lista_teste = {
    "homem" : [
      "cisgenero",
      "Transgênero",
      "Não-binário"
    ],
    "mulher" : [
      "cisgenero",
      "Transgênero",
      "Não-binário"
    ],
    "Prefiro não me identificar" : [
      "Não-binário"
    ]
  }
  
  
  escolha = menu_escolha(nome="Qual seu gênero?", lista=lista_teste)
  saida_terminal.desenhar_tela_terminal(texto=escolha)