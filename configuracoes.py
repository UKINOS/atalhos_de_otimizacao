"""Serve só pros menus de configuração em Main não poluirem o código...
"""

import caminhos_e_variaveis_globais
import entrada_usuario
import musicas
import saida_terminal



def musica_aviso():
  saida_terminal.desenhar_tela_terminal(texto=f"O som está {"ativado" if caminhos_e_variaveis_globais.som else "desativado"}, deseja {"desativar?" if caminhos_e_variaveis_globais.som else "ativar?"}")
  saida_terminal.lista_alternada(lista=[f"Sim, {"desative" if caminhos_e_variaveis_globais.som else "ative"}", "Não, mantenha do jeito que está..."], enumerado=True)
  
  valor = entrada_usuario.entrada(tipo_entrada=int, limite_caracteres_numero=[1, 2])
  
  if valor:
    caminhos_e_variaveis_globais.som = not caminhos_e_variaveis_globais.som # Inverte o valor
    
    
def teste_musica():
  saida_terminal.lista_alternada(lista=list(caminhos_e_variaveis_globais.MUSICAS.keys()), enumerado=True)
          
  valor = entrada_usuario.entrada(tipo_entrada=int, limite_caracteres_numero=[1, len(caminhos_e_variaveis_globais.MUSICAS)])
  
  saida_terminal.apagar_terminal()
  saida_terminal.escrever_buffer((True, False))
  saida_terminal.lista_alternada(lista=f"{(list(caminhos_e_variaveis_globais.MUSICAS.keys()))[valor - 1]}", enumerado=valor)
  
  musicas.tocar_musica(partitura=caminhos_e_variaveis_globais.MUSICAS.get((list(caminhos_e_variaveis_globais.MUSICAS.keys()))[valor - 1]), mostrar_nota=True)
  

def velocidade_interface():
  saida_terminal.desenhar_tela_terminal(texto=f"Isso altera a velocidade de coisas que mexem com a interface, é recomendado que você mantenha em {(list(caminhos_e_variaveis_globais.DELAY_VALORES.keys()))[0]}...")
  saida_terminal.lista_alternada(lista=list(caminhos_e_variaveis_globais.DELAY_VALORES.keys()), enumerado=True)
  
  valor = entrada_usuario.entrada(tipo_entrada=int, limite_caracteres_numero=[1, len(caminhos_e_variaveis_globais.DELAY_VALORES)])
  
  caminhos_e_variaveis_globais.delay = (list(caminhos_e_variaveis_globais.DELAY_VALORES.values()))[valor - 1]
  
  # # To doido?! Parece q não há diferença entre os modos?!
  # # Nope, o Windows q é lento quando você adiciona muitas linhas kkkkkkkkkkkkkkkkk
  # # O ajuste do tempo de time.sleep(0) não adianta se o gargalo é o tempo pra desenhar 50 linhas a cada reset...
  # print(caminhos_e_variaveis_globais.delay)
  # time.sleep(3)