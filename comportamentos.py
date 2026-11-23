"""Código responsável por lidar com como o sistema é configurado...
"""
import time



import caminhos_e_variaveis_globais
import entrada_usuario
import ferramentas
import limpeza_e_organizacao
import saida_terminal



def hibernacao():
  """Lida com a hibernação do sistema, levando em consideração a chave de inicialização rápida...
  """
  
  estado_hibernacao = ferramentas.regedit(nome_chave="HiberFileType", local=R"HKLM\SYSTEM\CurrentControlSet\Control\Power")
  estado_inicializacao_rapida = ferramentas.regedit(nome_chave="HiberbootEnabled",local=R"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Power")
  
  saida_terminal.apagar_terminal()
  saida_terminal.escrever_buffer([True, True])
  
  
  if estado_hibernacao[-1] == "0x2":
    saida_terminal.desenhar_tela_terminal(formatacao=["TEXTO_PRETO", "FUNDO_CIANO"], texto="A hibernação está ativada - FULL (memória completa)")
    
  elif estado_hibernacao[-1] == "0x1":
    saida_terminal.desenhar_tela_terminal(formatacao=["TEXTO_PRETO", "FUNDO_AZUL"], texto="A hibernação está desativada -  REDUCED (inicialização rápida)")
  
  else:
    saida_terminal.desenhar_tela_terminal(formatacao=["TEXTO_BRANCO", "FUNDO_PRETO"], texto="A hibernação está desativada - Off (nada)")

    
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)
  saida_terminal.desenhar_tela_terminal(formatacao=["NEGRITO", "TEXTO_PRETO", "FUNDO_BRANCO"], texto="Qual será sua ação?")
  saida_terminal.lista_alternada(lista=["Ative hibernação", "Desative hibernação", "Nada"], enumerado=True)
    
  escolha = entrada_usuario.entrada(int, [1, 3])
  
  saida_terminal.apagar_terminal()
  saida_terminal.escrever_buffer([True, True])
  
  
  if escolha == 1:
    ferramentas.terminal(tipo=1, comando="powercfg /h on")
    ferramentas.terminal(tipo=1, comando="powercfg /h /type full")
    
    if estado_inicializacao_rapida[-1] == "0x0":
      ferramentas.regedit(acao="ADD", nome_chave="HiberbootEnabled", valor="/t REG_DWORD /d 0x0", local=R"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Power")
    
    
  elif escolha == 2:
    if estado_inicializacao_rapida[-1] == "0x1":
      ferramentas.terminal(tipo=1, comando="powercfg /h /type reduced")
      
    else:
      ferramentas.terminal(tipo=1, comando="powercfg /h off")
      ferramentas.regedit(acao="ADD", nome_chave="HiberbootEnabled", valor="/t REG_DWORD /d 0x0", local=R"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Power")
      
      
def inicializacao_rapida_explorer():
  """Adiciona ou remove chave que remove os 10 segundos de delay do Windows...
  """
  
  local_chave = R"HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Serialize"
  estado = ferramentas.regedit(nome_chave="StartupDelayInMSec", local=local_chave)

  if estado[-1] == "0x0":
    saida_terminal.desenhar_tela_terminal(formatacao=["TEXTO_PRETO", "FUNDO_CIANO"], texto="A inicialização rápida do Explorer está ativada")
  
  else:
    saida_terminal.desenhar_tela_terminal(formatacao=["TEXTO_BRANCO", "FUNDO_PRETO"], texto="A inicialização rápida do Explorer está desativada (padrão do Windows)")

  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)
  saida_terminal.desenhar_tela_terminal(formatacao=["NEGRITO", "TEXTO_PRETO", "FUNDO_BRANCO"], texto="Qual será sua ação?")
  
  saida_terminal.lista_alternada(lista=["Ativar", "Desativar", "Nada"], enumerado=True)

  escolha = entrada_usuario.entrada(int, [1, 3])

  if escolha == 1:
    ferramentas.regedit(acao="ADD", nome_chave="StartupDelayInMSec", valor="/t REG_DWORD /d 0x0", local=local_chave)
    
  elif escolha == 2:
    ferramentas.regedit(acao="DELETE", nome_chave="StartupDelayInMSec", local=local_chave)
    
    
def plano_de_energia():
  lista_planos = ferramentas.terminal(tipo=2, comando="powercfg /L")
  guid_maximo = None
  ativo = False

  if "(Desempenho" in lista_planos and "Máximo)" in lista_planos:
    for iterador in range(len(lista_planos)):
      if lista_planos[iterador - 1] == "(Desempenho" and lista_planos[iterador] == "Máximo)":
        guid_maximo = lista_planos[iterador - 2]
        
        if iterador + 1 < len(lista_planos): # Evita overflow... ( ͡° ͜ʖ ͡°)
          if lista_planos[iterador + 1] == "*":
            ativo = True
        
        break


  if guid_maximo and ativo:
    saida_terminal.desenhar_tela_terminal(formatacao=["TEXTO_PRETO", "FUNDO_CIANO"], texto="O plano de Desempenho Máximo já existe e está ativo")
  
  elif guid_maximo and not ativo:
    saida_terminal.desenhar_tela_terminal(formatacao=["TEXTO_PRETO", "FUNDO_AZUL"], texto="O plano de Desempenho Máximo já existe, mas está desativado")
  
  else:
    saida_terminal.desenhar_tela_terminal(formatacao=["TEXTO_BRANCO", "FUNDO_PRETO"], texto="O plano de Desempenho Máximo ainda não foi criado nesta máquina")


  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)
  saida_terminal.desenhar_tela_terminal(formatacao=["NEGRITO", "TEXTO_PRETO", "FUNDO_BRANCO"], texto="Qual será sua ação?")
  saida_terminal.lista_alternada(lista=["Ativar desempenho máximo", "Ativar plano equilibrado (padrão)", "Abrir menu de energia", "Nada"], enumerado=True)

  escolha = entrada_usuario.entrada(int, [1, 4])


  if escolha == 1:
    if not guid_maximo:
      saida_criar = ferramentas.terminal(tipo=2, comando="powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61")
      
      if "Energia:" in saida_criar:
        guid_maximo = saida_criar[saida_criar.index("Energia:") + 1]
        
      else:
        ferramentas.deteccao_de_erro(nome="Erro no Plano de Energia", log=f"Falha ao duplicar esquema: {saida_criar}")
        return

    ferramentas.terminal(tipo=1, comando=f"powercfg /setactive {guid_maximo}")

  elif escolha == 2:
    ferramentas.terminal(tipo=1, comando="powercfg /setactive 381b4222-f694-41f0-9685-ff5bb260df2e")
    
  if escolha == 1 or escolha == 2:
    saida_terminal.desenhar_tela_terminal(formatacao=["NEGRITO", "TEXTO_PRETO", "FUNDO_BRANCO"], texto="Deseja que eu abra o menu de configurações?")
    saida_terminal.lista_alternada(lista=["Sim", "Não"], enumerado=True)
    
    escolha = entrada_usuario.entrada(int, [1, 2])
    
    # Gambiarra pra ativar a escolha abaixo:
    # 1 --> 3
    # 2 --> 4
    escolha += 2

  if escolha == 3:
    ferramentas.terminal(tipo=1, comando="powercfg.cpl")
    
    
def inicializacao_rapida_windows():
  """Lida com a hibernação do sistema, levando em consideração a chave de inicialização rápida...
  """
  estado_inicializacao_rapida = ferramentas.regedit(nome_chave="HiberbootEnabled", local=R"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Power")
  estado_hibernacao = ferramentas.regedit(nome_chave="HiberFileType", local=R"HKLM\SYSTEM\CurrentControlSet\Control\Power")
  
  saida_terminal.apagar_terminal()
  saida_terminal.escrever_buffer([True, True])
  
  
  if estado_inicializacao_rapida[-1] == "0x1":
    saida_terminal.desenhar_tela_terminal(formatacao=["TEXTO_PRETO", "FUNDO_CIANO"], texto="A inicialização_rapida está ativada")
  
  else:
    saida_terminal.desenhar_tela_terminal(formatacao=["TEXTO_BRANCO", "FUNDO_PRETO"], texto="A inicialização_rapida está desativada")

    
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)
  saida_terminal.desenhar_tela_terminal(formatacao=["NEGRITO", "TEXTO_PRETO", "FUNDO_BRANCO"], texto="Qual será sua ação?")
  saida_terminal.lista_alternada(lista=["Ative inicialização_rápida", "Desative inicialização_rápida", "Nada"], enumerado=True)
    
  escolha = entrada_usuario.entrada(int, [1, 3])
  
  saida_terminal.apagar_terminal()
  saida_terminal.escrever_buffer([True, True])
  
  
  if escolha == 1:
    # Se eu verificar por 0x0, tem chance de dar erro por chave inesistente....
    if estado_hibernacao[-1] not in ["0x1", "0x2"]:
      ferramentas.terminal(tipo=1, comando="powercfg /h on")
      ferramentas.terminal(tipo=1, comando="powercfg /h /type reduced")
      
    ferramentas.regedit(acao="ADD", nome_chave="HiberbootEnabled", valor="/t REG_DWORD /d 0x1", local=R"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Power")
    
    
  elif escolha == 2:
    if estado_hibernacao[-1] == "0x2":
      ferramentas.regedit(acao="ADD", nome_chave="HiberbootEnabled", valor="/t REG_DWORD /d 0x0", local=R"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Power")
      
    else:
      ferramentas.terminal(tipo=1, comando="powercfg /h off")
      ferramentas.regedit(acao="ADD", nome_chave="HiberbootEnabled", valor="/t REG_DWORD /d 0x0", local=R"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Power")
      
      
def aceleracao_de_hardware():
  """Responsável por lidar com a aceleração de hardware, controlando-a por chaves no registro...
  Nota: Se o sistema não tiver suporte, mudar essa chave não vai alterar o comportamento do sistema...
  """
  
  estado_aceleracao = ferramentas.regedit(nome_chave="HwSchMode", local=R"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers")
  
  if "0x2" in estado_aceleracao:
    saida_terminal.desenhar_tela_terminal(formatacao=["TEXTO_PRETO", "FUNDO_CIANO"], texto="A aceleração de hardware está ativada")
    
  else:
    saida_terminal.desenhar_tela_terminal(formatacao=["TEXTO_BRANCO", "FUNDO_PRETO"], texto="A aceleração de hardware está desativada")
    
    
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)
  saida_terminal.desenhar_tela_terminal(formatacao=["NEGRITO", "TEXTO_PRETO", "FUNDO_BRANCO"], texto="Qual será sua ação?")
  saida_terminal.lista_alternada(lista=["Ativar aceleração de hardware", "Desativar aceleração de hardware", "Nada"], enumerado=True)
  
  escolha = entrada_usuario.entrada(int, [1, 3])
  
  if escolha == 1:
    ferramentas.regedit(acao="ADD", nome_chave="HwSchMode", valor="/t REG_DWORD /d 0x2", local=R"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers")
    
  elif escolha == 2:
    ferramentas.regedit(acao="ADD", nome_chave="HwSchMode", valor="/t REG_DWORD /d 0x1", local=R"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers")
  

def indexacao_windows():
  """Lida com o serviço de indexação do windows...

  Returns:
      bool: Retorna pra avisar se houve uma execução de comando ou não.
  """
  
  resposta = ferramentas.servicos_windows(nome_servico="WSearch", acao=0)
  
  if isinstance(resposta, str):
    ferramentas.deteccao_de_erro(nome="Erro na lógica de indexacao_windows", log=f"Expected True or False, returned: {resposta}", parada=False)
    return 1  
  
  else:
    if resposta:
      saida_terminal.desenhar_tela_terminal(formatacao=["TEXTO_PRETO", "FUNDO_CIANO"], texto="A indexação do Windows está ativada")
    
    else:
      saida_terminal.desenhar_tela_terminal(formatacao=["TEXTO_BRANCO", "FUNDO_PRETO"], texto="A indexação do Windows está desativada")
      
      
    saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)
    saida_terminal.desenhar_tela_terminal(formatacao=["NEGRITO", "TEXTO_PRETO", "FUNDO_BRANCO"], texto="Qual será sua ação?")
    saida_terminal.lista_alternada(lista=["Ativar indexação do Windows", "Desativar indexação do Windows", "Nada"], enumerado=True)
    
    escolha = entrada_usuario.entrada(int, [1, 3])
    
    if escolha == 1:
      ferramentas.servicos_windows(nome_servico="WSearch", acao=1)
      
    elif escolha == 2:
      ferramentas.servicos_windows(nome_servico="WSearch", acao=2)
      
      saida_terminal.desenhar_tela_terminal(formatacao=["NEGRITO", "TEXTO_PRETO", "FUNDO_BRANCO"], texto="Notei q vc desativou o serviço, deseja deletar o que o Windows indexou?")
      saida_terminal.desenhar_tela_terminal(formatacao=["RESET", "NEGRITO", "TEXTO_BRANCO", "FUNDO_VERMELHO"], texto="AVISO: O ÍNDICE PRECISARÁ SER RECRIADO DO ZERO SE O SERVIÇO FOR INICIADO NO FUTURO, O QUE PODE DEMORAR HORAS!")
      
      saida_terminal.lista_alternada(lista=["Delete o índice", "Mantenha-o"], enumerado=True)
      
      escolha = entrada_usuario.entrada(tipo_entrada=int, limite_caracteres_numero=[1, 2])
      
      if escolha == 1:
        limpeza_e_organizacao.delete_recursivo(R"C:\ProgramData\Microsoft\Search\Data\Applications\Windows")
        limpeza_e_organizacao.delete_recursivo(R"C:\ProgramData\Microsoft\Search\Data\Applications\Windows11")
      
    return 0
  
  
def sysmain():
  
  
  # Mano, vamos criar flags antes que eu fique doido, é 4 da manhã kkk
  recurso_estado_recomendado = {
    "Sysmain"        : [None, None],
    "Prefetch_geral" : [None, None],
    "Superprefetch"  : [None, None],
    "Compressão RAM" : [None, None],
    "Prefetch_chave" : [None, None]
  }
  
  
  # Antes eu estava fazendo todas as verificações de uma vez só...
  # Entretanto, se Sysmain estiver desativado, isso pode dar problema... enfim...
  servico_sysmain = ferramentas.servicos_windows(acao=0, nome_servico="SysMain")
  if isinstance(servico_sysmain, str):
    ferramentas.deteccao_de_erro(
      nome="Erro na consulta do serviço SysMain",
      log=f"Expected True or False, returned: {servico_sysmain}",
      parada=False
    )
    return
  
  saida_terminal.apagar_terminal()
  saida_terminal.escrever_buffer((True, False))
  
  # E la vamos nós...
  # Verifique primeiro se o serviço está rodando...
  # É como tentar respirar sem ter um pulmão...
  if servico_sysmain:
    saida_terminal.desenhar_tela_terminal(texto="O SysMain está ativado!", formatacao=["TEXTO_PRETO", "FUNDO_CIANO"], add_to_buffer_text=True)
    recurso_estado_recomendado["Sysmain"][0] = True 
    
  else:
    saida_terminal.desenhar_tela_terminal(texto="O SysMain está desativado!", formatacao=["TEXTO_BRANCO", "FUNDO_PRETO"])
    saida_terminal.desenhar_tela_terminal(texto="Para ativar a compressão de memória ram ou prefetch (carregamento de apps mais utilizados na ram), preciso ativar o SysMain... Posso?", formatacao=["RESET", "NEGRITO", "TEXTO_PRETO", "FUNDO_BRANCO"])
    
    saida_terminal.lista_alternada(lista=["Sim, pode ativar!", "Não, talvez em outro momento..."], enumerado=True)
      
    resposta = entrada_usuario.entrada(tipo_entrada=int, limite_caracteres_numero=[1, 2])
    
    if resposta == 2:
      saida_terminal.desenhar_tela_terminal(texto="Bom, vou retornar você pro menu...", formatacao=["RESET", "TEXTO_PRETO", "FUNDO_BRANCO"])
      time.sleep(3)
      return
    
    saida_terminal.desenhar_tela_terminal(texto="Okay, um momento...", formatacao=["RESET", "TEXTO_VERDE"])
    
    ferramentas.servicos_windows(acao=1, nome_servico="SysMain")
    
    saida_terminal.desenhar_tela_terminal(texto="O SysMain está ativado!", formatacao=["RESET", "TEXTO_PRETO", "FUNDO_CIANO"], add_to_buffer_text=True)
    
    
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)
  saida_terminal.apagar_terminal()
  saida_terminal.escrever_buffer((True, True))

  
  # Verificação do powershell... Demorado eu sei...
  powershell_sysmain = ferramentas.terminal(tipo=2, comando="powershell -Command \"Get-MMAgent\"")
  
  # Prefetch (otimização do HDD)
  recurso_estado_recomendado["Prefetch_geral"][0] = powershell_sysmain[powershell_sysmain.index("ApplicationLaunchPrefetching") + 2] == "True"
  
  if recurso_estado_recomendado["Prefetch_geral"][0]:
    saida_terminal.desenhar_tela_terminal(texto="O Prefetch está ativado!", formatacao=["TEXTO_PRETO", "FUNDO_CIANO"], add_to_buffer_text=True)
      
  else:
    saida_terminal.desenhar_tela_terminal(texto="O Prefetch está desativado!", formatacao=["TEXTO_BRANCO", "FUNDO_PRETO"], add_to_buffer_text=True)
    
    
  # Superprefetch (armazena aplicativos mais usados na RAM)
  recurso_estado_recomendado["Superprefetch"][0] = powershell_sysmain[powershell_sysmain.index("ApplicationPreLaunch") + 2] == "True"
  
  if recurso_estado_recomendado["Superprefetch"][0]:
    saida_terminal.desenhar_tela_terminal(texto="O Superprefetch está ativado!", formatacao=["TEXTO_PRETO", "FUNDO_CIANO"], add_to_buffer_text=True)
      
  else:
    saida_terminal.desenhar_tela_terminal(texto="O Superprefetch está desativado!", formatacao=["TEXTO_BRANCO", "FUNDO_PRETO"], add_to_buffer_text=True)
  
  
  # Compressão de memória RAM  
  recurso_estado_recomendado["Compressão RAM"][0] = powershell_sysmain[powershell_sysmain.index("MemoryCompression") + 2] == "True"
  
  if recurso_estado_recomendado["Compressão RAM"][0]:
    saida_terminal.desenhar_tela_terminal(texto="A compressão de memória RAM está ativada!", formatacao=["TEXTO_PRETO", "FUNDO_CIANO"], add_to_buffer_text=True)
    
  else:
    saida_terminal.desenhar_tela_terminal(texto="A compressão de memória RAM está desativada!", formatacao=["TEXTO_BRANCO", "FUNDO_PRETO"], add_to_buffer_text=True)


  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)
  saida_terminal.apagar_terminal()
  saida_terminal.escrever_buffer((True, True))
    

  # Não me esqueça :)
  # Esqueci não docinho
  # Verificar o que o REGEDIT está definido...
  regedit_sysmain = ferramentas.regedit(nome_chave="EnablePrefetcher", local=R"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters")
  
  
  recurso_estado_recomendado["Prefetch_chave"][0] = int(regedit_sysmain[-1][2:])
  
  if recurso_estado_recomendado["Prefetch_chave"][0] == 3:
    saida_terminal.desenhar_tela_terminal(texto="O Prefetcher está com configuração total! (Boot e Apps)", formatacao=["TEXTO_PRETO", "FUNDO_CIANO"], add_to_buffer_text=True)
    
  elif recurso_estado_recomendado["Prefetch_chave"][0] == 2:
    saida_terminal.desenhar_tela_terminal(texto="O prefetcher está com configuração parcial! (Boot)", formatacao=["TEXTO_PRETO", "FUNDO_AZUL"], add_to_buffer_text=True)
    
  elif recurso_estado_recomendado["Prefetch_chave"][0] == 1:
    saida_terminal.desenhar_tela_terminal(texto="O prefetcher está com configuração parcial! (Apps)", formatacao=["TEXTO_PRETO", "FUNDO_AZUL"], add_to_buffer_text=True)
      
  else:
    saida_terminal.desenhar_tela_terminal(texto="O prefetcher está sem configuração/desativado! (Não)", formatacao=["TEXTO_BRANCO", "FUNDO_PRETO"], add_to_buffer_text=True)
    
    
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"])
  saida_terminal.apagar_terminal()
  saida_terminal.escrever_buffer((True, False))
  
  
  # Formatação pra se houver algum conflito... Assim não preciso ficar arrumando ali embaixo...
  saida_terminal.desenhar_tela_terminal(formatacao=["NEGRITO", "TEXTO_BRANCO", "FUNDO_VERMELHO"])
  
  # Pronto, agora verificação de conflitos...
  if recurso_estado_recomendado["Prefetch_chave"][0] == 0 and recurso_estado_recomendado["Prefetch_geral"][0] == True:
    saida_terminal.desenhar_tela_terminal(texto="Notei que você tem o Prefetch ativado (MMAgent), mas não está com ele configurado (Regedit)...")
  
  if recurso_estado_recomendado["Prefetch_chave"][0] > 0 and recurso_estado_recomendado["Prefetch_geral"][0] == False:
    saida_terminal.desenhar_tela_terminal(texto="Notei que você tem o Prefetch configurado(Regedit), mas esqueceu de ativa-lo(MMAgent)...")
    
  
  # E agora a parte divertida...
  saida_terminal.desenhar_tela_terminal(texto="Muito bem, qual modo você prefere?", formatacao=["TEXTO_BRANCO", "FUNDO_AMARELO"])
  
  saida_terminal.lista_alternada(lista=["Modo guiado: Perguntas para ajudar a configurar", "Modo manual: Eu sei o que estou fazendo", "Cancelar: Que medo, não quero mexer nisso não!"],enumerado=True)
  
  modo = entrada_usuario.entrada(tipo_entrada=int, limite_caracteres_numero=[1, 3])
  
  if modo == 3:
    saida_terminal.desenhar_tela_terminal(texto="Bom, vou retornar você pro menu...", formatacao=["RESET", "TEXTO_PRETO", "FUNDO_BRANCO"])
    time.sleep(3)
    return
  
  
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"])
  saida_terminal.apagar_terminal()
  saida_terminal.apagar_buffer((False, True))
  saida_terminal.escrever_buffer((True, False))
  
  # Primeiro, vamos duplicar as entradas...
  for valor in recurso_estado_recomendado.values():
    valor[1] = valor[0]
  
  if modo == 2:
    lista_de_chaves_recurso_estado_recomendado = ["Sair"] + list(recurso_estado_recomendado.keys())

    while True:
      saida_terminal.desenhar_tela_terminal(formatacao=["RESET"])
      saida_terminal.apagar_terminal()
      saida_terminal.escrever_buffer((True, False))

      # E só notei agora q não dei nada pro usuário conseguir escapar do menu abaixo...
      reformatacao_recurso_estado_recomendado = ["Sair"]
      
      # Formatação :)
      # Que porra é essa q fiz as 5 da manhã?
      for chave, valor in recurso_estado_recomendado.items():
        reformatacao_recurso_estado_recomendado.append(f"{(14 - len(chave)) * " "}{chave} -   {(f" {valor[0]}" if valor[0] else valor[0]) if type(valor[0]) == bool else f" {valor[0]}   "}  - {(f" {valor[1]}" if valor[1] else valor[1]) if type(valor[1]) == bool else f"  {valor[1]}  "}")
        
      
      saida_terminal.desenhar_tela_terminal(texto="        NOME      - Anterior - Atual", formatacao=["TEXTO_PRETO", "FUNDO_BRANCO"])
      saida_terminal.lista_alternada(lista=reformatacao_recurso_estado_recomendado, enumerado=True)
      
      alterar = entrada_usuario.entrada(tipo_entrada=int, limite_caracteres_numero=[1, len(lista_de_chaves_recurso_estado_recomendado)])
      
      
      # Só inverter o valor...
      if lista_de_chaves_recurso_estado_recomendado[alterar - 1] == "Sair":
        break
      
      elif lista_de_chaves_recurso_estado_recomendado[alterar - 1] != "Prefetch_chave":
          recurso_estado_recomendado[lista_de_chaves_recurso_estado_recomendado[alterar - 1]][1] = not recurso_estado_recomendado[lista_de_chaves_recurso_estado_recomendado[alterar - 1]][1]
          
      else:
        saida_terminal.lista_alternada(lista=["0x3 - Boot e Apps", "0x2 - Boot", "0x1 - Apps", "0x0 - Desconfigurado"], enumerado=True)
        
        alterar_prefetch_chave = entrada_usuario.entrada(tipo_entrada=int, limite_caracteres_numero=[1, 4])
        
        recurso_estado_recomendado[lista_de_chaves_recurso_estado_recomendado[alterar - 1]][1] = 4 - alterar_prefetch_chave
  
  if modo == 1:
    for iterador in range(0, 3):
      # Isso daqui vai rodar várias vezes...
      
      saida_terminal.desenhar_tela_terminal(formatacao=["RESET"])
      saida_terminal.apagar_terminal()
      saida_terminal.escrever_buffer((True, False))
      
      
      # Corzinha das perguntas...
      saida_terminal.desenhar_tela_terminal(formatacao=["TEXTO_PRETO", "FUNDO_BRANCO"], quebra_de_linha=False)
      
      # Você precisa de otimização? Ou é rico?
      if iterador == 0:
        saida_terminal.desenhar_tela_terminal(texto="1. Você tem 32GB ou mais de memória RAM?")
        saida_terminal.lista_alternada(lista=["Sim", "Não"], enumerado=True)
        
        resposta = entrada_usuario.entrada(tipo_entrada=int, limite_caracteres_numero=[1,2])
        
        if resposta == 1:
          # ELE TEM RAM PEGUEM ELE!
          # Digo, ele tem bastante ram, nesse caso ele nem precisa se preocupar direito kkkkk
          recurso_estado_recomendado["Sysmain"][1] = False
          break
        
        # O q faço? Pra rodar o resto preciso de Sysmain ativo...
        recurso_estado_recomendado["Sysmain"][1] = True
        continue
          
      
      # Precisa de ajuda máxima? Ou pelo menos seu dispositivo está acompanhando as coisas?
      elif iterador == 1:
        saida_terminal.desenhar_tela_terminal(texto="2.A. Você possuí um HDD no seu sistema (HDD externos por USB não contam)?", )
        saida_terminal.lista_alternada(lista=["Sim", "Não"], enumerado=True)
                
        resposta = entrada_usuario.entrada(tipo_entrada=int, limite_caracteres_numero=[1,2])
        
        if resposta == 2:
          # Só tem Nvme ou um diskete/dvd/cd... vou q ele tem um Nvme kkkkk
          recurso_estado_recomendado["Prefetch_geral"][1] = False
          recurso_estado_recomendado["Prefetch_chave"][1] = 0
          recurso_estado_recomendado["Superprefetch"][1] = False
          continue
          
        # Se chegar aqui, sabemos q ele tem um HDD no sistema...
        saida_terminal.desenhar_tela_terminal(texto="2.B. Esse HDD possuí o sistema operacional? (Se houver um HDD com o sistema operacional e um sem, baseie-se no que possuí o sistema operacional)", formatacao=["TEXTO_PRETO", "FUNDO_BRANCO"])
        saida_terminal.lista_alternada(lista=["Sim", "Não"], enumerado=True)
                
        resposta = entrada_usuario.entrada(tipo_entrada=int, limite_caracteres_numero=[1,2])
        
        if resposta == 1:
          # Ótimo, mais um sofredor...
          # Ative o alerta vermelho!
          flag_hdd = True
          
          # Que milagre é esperado?
          saida_terminal.desenhar_tela_terminal(texto="2.C. Você costuma abrir sempre os mesmos programas? Por exemplo: \"Eu sempre abro o Chrome, Office e Outlook\". Caso você varie muito e rode programas que consumam a memória ram inteira, considere essa pergunta como um não.", formatacao=["TEXTO_PRETO", "FUNDO_BRANCO"])
          saida_terminal.lista_alternada(lista=["Sim, sempre sigo a mesma rotina", "Não, meu uso é aleatório e agressivo (abro vários apps pesados)"], enumerado=True)
          
          resposta = entrada_usuario.entrada(tipo_entrada=int, limite_caracteres_numero=[1,2])
          
          if resposta == 1:
            # Certo, provavelmente da pra tentar armazenar os aplicativos, mas precisamos saber se o usuário/colaborador vai gostar...
            saida_terminal.desenhar_tela_terminal(texto="2.D. Nesse caso, você prefere que o computador esteja pronto assim que possível? Ou não tem problema em esperar um pouco se isso significa uma melhor experiência?", formatacao=["TEXTO_PRETO", "FUNDO_BRANCO"])
            saida_terminal.lista_alternada(lista=["Preciso dele assim que possível", "Posso aguardar um pouco mais..."], enumerado=True)
            
            resposta = entrada_usuario.entrada(tipo_entrada=int, limite_caracteres_numero=[1,2])
            
            if resposta == 2:
              # Finalmente, alguém que vai tirar proveito dessas otimizações!
              recurso_estado_recomendado["Superprefetch"][1] = True
              
            if resposta == 1:
              # Não foi dessa vez amigão...
              recurso_estado_recomendado["Superprefetch"][1] = False
              
            recurso_estado_recomendado["Prefetch_geral"][1] = True
            recurso_estado_recomendado["Prefetch_chave"][1] = 3
            continue
          
          # Ta, nesse caso a otimização de Apps foi por água abaixo, talvez de para otimizar o boot do sistema com o prefetch...
          recurso_estado_recomendado["Prefetch_geral"][1] = True
          recurso_estado_recomendado["Prefetch_chave"][1] = 2
          recurso_estado_recomendado["Superprefetch"][1] = False
          
        
        if resposta == 2:
          # Certo, então o HDD não está sobrecarregado...
          # Inclusive vamos tirar essa do caminho pq ela ficou desnecessária...
          recurso_estado_recomendado["Superprefetch"][1] = False
          
          # E com isso, tirou-se a ideia de usar a flag de boot, mas ainda há duvidas sobre usar a flag de apps...
          saida_terminal.desenhar_tela_terminal(texto="2.C. Esse HDD é usado para rodar algo ou é utilizado apenas como armazenamento (ele tem jogos/programas pesados ou só guarda vídeos/fotos/documentos)?", formatacao=["TEXTO_PRETO", "FUNDO_BRANCO"])
          saida_terminal.lista_alternada(lista=["Rodo coisas pesadas nele", "Ele server como backup básico"], enumerado=True)
                  
          resposta = entrada_usuario.entrada(tipo_entrada=int, limite_caracteres_numero=[1,2])
          
          if resposta == 1:
            # Ele puxa coisas pesadas, vamos dar uma ajudinha...
            recurso_estado_recomendado["Prefetch_geral"][1] = True
            recurso_estado_recomendado["Prefetch_chave"][1] = 1
            
          else:
            # Então é bem básico... Não precisa de otimização...
            recurso_estado_recomendado["Prefetch_geral"][1] = False
            recurso_estado_recomendado["Prefetch_chave"][1] = 0
            
            
      # Balança de RAM e CPU?
      elif iterador == 2:
        # Será que a CPU está sofrendo?
        saida_terminal.desenhar_tela_terminal(texto="3.A. Seu sistema está com a CPU quase sempre em uso alto? (Ela está com dificuldade de acompanhar o sistema?)")
        
        saida_terminal.lista_alternada(lista=["Sim", "Não"], enumerado=True)
                        
        resposta = entrada_usuario.entrada(tipo_entrada=int, limite_caracteres_numero=[1,2])
        
        if resposta == 1:
          # Aparentemente sim?
          # Vamos confirmar isso
          saida_terminal.desenhar_tela_terminal(texto="3.B. Quanto de ram você tem? (Se o valor não for exatamente, arredonde para baixo)", formatacao=["TEXTO_PRETO", "FUNDO_BRANCO"])
          saida_terminal.lista_alternada(lista=["4GB", "8GB", "16GB"], enumerado=True)
                        
          resposta = entrada_usuario.entrada(tipo_entrada=int, limite_caracteres_numero=[1,3])
          
          if resposta == 1:
            # Bruh
            recurso_estado_recomendado["Compressão RAM"][1] = True
            continue  
          
          saida_terminal.desenhar_tela_terminal(texto="3.C. Você costuma usar para coisas básicas? Exemplo: Eu apenas vejo e-mails / eu abro apenas o Chrome", formatacao=["TEXTO_PRETO", "FUNDO_BRANCO"])
          saida_terminal.lista_alternada(lista=["Sim, meu uso é básico", "Não, eu costumo fazer mais coisas"], enumerado=True)
                                  
          resposta -= entrada_usuario.entrada(tipo_entrada=int, limite_caracteres_numero=[1,2])
          
          # B - C = 2 - 2 = 0
          if resposta == 0:
            # Nah, ta fora!
            recurso_estado_recomendado["Compressão RAM"][1] = True
            continue
          
          saida_terminal.desenhar_tela_terminal(texto="3.D. Você costuma usar programas leves? Exemplo: Eu abro apenas o Outlook / Word / Chrome", formatacao=["TEXTO_PRETO", "FUNDO_BRANCO"])
          saida_terminal.lista_alternada(lista=["Sim, meu uso é básico", "Não, eu abro várias guias no navegador/uso softwares de edição de imagem e vídeo"], enumerado=True)
                                  
          resposta -= entrada_usuario.entrada(tipo_entrada=int, limite_caracteres_numero=[1,2])
          
          if resposta < 0:
            # Ai avacalho...
            recurso_estado_recomendado["Compressão RAM"][1] = True
            continue
          
        # Impressionante! Ou você é um usuário muito básico, ou tem muita memória RAM...
        recurso_estado_recomendado["Compressão RAM"][1] = False
          
          
  # Agora tem q aplicar tudo as configurações... Q legal...
  # TA PREULA QUANTA LINHA
  # Enfim, bora começar as combinações...

  if recurso_estado_recomendado["Sysmain"][1] == False:
    ferramentas.servicos_windows(acao=2 , nome_servico="SysMain")
    return
    
  for chave, valor in recurso_estado_recomendado.items():
    if chave in caminhos_e_variaveis_globais.MMA_COMANDS:
      ferramentas.terminal(tipo=1, comando=caminhos_e_variaveis_globais.MMA_COMANDS[chave][valor[1]])

    elif chave == "Prefetch_chave":
      ferramentas.regedit(acao="ADD", nome_chave="EnablePrefetcher", local=R"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters", valor=f"/t REG_DWORD /d 0x{valor[1]}")
      
      
def sistema_corrompido():
  """Verifica se o sistema está corrompido

  Returns:
      bool: É uma descrição básica pra avisar pra main se ele deve tocar a música completa ou não...
  """
  
  saida_terminal.desenhar_tela_terminal(formatacao=["NEGRITO", "TEXTO_PRETO", "FUNDO_BRANCO"], texto="Para verificar se o sistema está desfragmentado: Primeiro é necessário verificar o disco por erros (o que força-rá uma reinicializaçao do sistema) e depois verificar a imagem do sistema e seus arquivos... O que você acha?")
  saida_terminal.lista_alternada(["Desejo verificar o disco por erros", "Já verifiquei o disco, desejo verificar o sistema"], True)
  
  iteracao = entrada_usuario.entrada(int, [1, 2])
  
  
  if iteracao == 1:
    ferramentas.chkdsk(disco_sistema=True)
    saida_terminal.desenhar_tela_terminal(formatacao=["NEGRITO", "TEXTO_PRETO", "FUNDO_BRANCO"], texto="Deseja que eu reinicie a máquina pra você?")
    saida_terminal.lista_alternada(["Sim, reinicie ela", "Não, ainda desejo fazer algumas coisas..."], True)
    
    acao = entrada_usuario.entrada(int, [1, 2])
    
    if acao == 1:
      ferramentas.terminal(tipo=1, comando="shutdown /r")
    
    return False
  
  # Se chegar aqui, é porque o ususário selecionou a opção 2
  ferramentas.terminal(tipo=1, comando="DISM.exe /Online /Cleanup-image /Restorehealth")
  ferramentas.terminal(tipo=1, comando="sfc /scannow")
  return True


# Sim, IA de novo, eu não sei lidar com HTML e já tive minha paciência esgotada com o Playwright e BeautifulSoup...
def vida_bateria():
  """Gera o relatório, analisa os valores e exibe o resultado no terminal.

  Raises:
      OSError: Se o relatório não puder ser aberto.

  Note:
      A referência é uma heurística linear: 80% de saúde após 1000 ciclos.
      Desvios acima de 20 pontos percentuais são marcados como anomalia;
      abaixo de 40% e a até 10 pontos da referência, a análise usa o rótulo
      humorístico "BATERIA DE CAPACITOR". Isso não determina a causa do desgaste
      nem comprova risco físico.
  """
  # Descobre a pasta onde o powercfg salvará o relatório.
  local_terminal = ' '.join(ferramentas.terminal(tipo=2, comando="cd"))
  
  # Gera o relatório HTML da bateria.
  codigo_saida = ferramentas.terminal(tipo=1, comando="powercfg /batteryreport")
  if codigo_saida != 0:
    ferramentas.deteccao_de_erro(
      nome="Relatório de bateria indisponível",
      log=(
        "powercfg /batteryreport não conseguiu gerar o relatório. "
        f"O dispositivo pode não ter bateria. Código de saída: {codigo_saida}"
      ),
      parada=False
    )
    return
  
  # Lê o arquivo gerado pelo Windows.
  with open(RF"{local_terminal}\battery-report.html", "r", encoding="utf-8-sig") as arquivo:
    conteudo_html = arquivo.read()
    
  # Remove as tags HTML e mantém o texto das tabelas.
  conteudo_html_filtrado = ferramentas.html_filtragem(conteudo_html)

  # Separa o texto em linhas para encontrar os campos do relatório.
  linhas = conteudo_html_filtrado.splitlines()

  def ler_campo(rotulo: str) -> str:
    prefixo = f"{rotulo} "
    for linha in linhas:
      if linha.startswith(prefixo):
        return linha[len(prefixo):].strip()

    raise ValueError(f"O campo {rotulo!r} não foi encontrado no relatório.")

  def ler_inteiro(rotulo: str) -> int:
    valor = ler_campo(rotulo)
    try:
      numero = valor.split()[0].replace(".", "").replace(",", "")
      return int(numero)
    except (IndexError, ValueError) as erro:
      raise ValueError(f"O campo {rotulo!r} não contém um número válido: {valor!r}") from erro

  # Extrai as capacidades e calcula a saúde como fração da capacidade original.
  try:
    capacidade_projeto = ler_inteiro("DESIGN CAPACITY")
    capacidade_atual = ler_inteiro("FULL CHARGE CAPACITY")
  except ValueError as erro:
    ferramentas.deteccao_de_erro(
      nome="Dados da bateria indisponíveis",
      log=(
        "O relatório não contém dados de capacidade. "
        "O dispositivo pode não ter bateria, ou o relatório pode estar incompleto. "
        f"Detalhe: {erro}"
      ),
      parada=False
    )
    return

  saude = capacidade_atual / capacidade_projeto * 100 if capacidade_projeto > 0 else None

  try:
    ciclos = ler_inteiro("CYCLE COUNT")
  except ValueError as erro:
    ciclos = None
    saude_esperada = None
    if capacidade_projeto <= 0 or capacidade_atual <= 0 or (saude is not None and saude > 100):
      analise = "ANOMALIA: o relatório contém capacidades inválidas."
      cor_analise = 0
    else:
      analise = f"Análise por ciclos indisponível: {erro}"
      cor_analise = 2

  else:
    if capacidade_projeto <= 0 or capacidade_atual <= 0 or ciclos < 0:
      analise = "ANOMALIA: o relatório contém capacidades ou ciclos inválidos."
      cor_analise = 0
      saude_esperada = None
    else:
      saude_esperada = max(0.0, 100 - 20 * ciclos / 1000)
      diferenca = saude - saude_esperada

      if saude > 100 or abs(diferenca) > 20:
        analise = "ANOMALIA: os valores estão muito fora da curva de referência; confira a medição."
        cor_analise = 0
      elif saude < 40 and abs(diferenca) <= 10:
        analise = "BATERIA DE CAPACITOR: baixa capacidade, mas compatível com os ciclos reportados."
        cor_analise = 5
      elif diferenca < -10:
        analise = "DEGRADAÇÃO ACIMA DO ESPERADO para os ciclos reportados."
        cor_analise = 4
      elif ciclos >= 800 or saude <= 80:
        analise = "BATERIA DESGASTADA: o nível de desgaste é compatível com uma bateria bem usada."
        cor_analise = 2
      elif diferenca > 10:
        analise = "ACIMA DO ESPERADO: a capacidade está melhor que a curva de referência."
        cor_analise = 1
      else:
        analise = "NORMAL: a capacidade está próxima da curva de referência."
        cor_analise = 1

  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"])
  saida_terminal.apagar_terminal()
  saida_terminal.escrever_buffer([True, False])
  cor_dados = saida_terminal.COMBINACOES_CORES[1]
  saida_terminal.desenhar_tela_terminal(
    texto=f"Capacidade de projeto: {capacidade_projeto} mWh",
    formatacao=cor_dados
  )
  saida_terminal.desenhar_tela_terminal(
    texto=f"Capacidade máxima atual: {capacidade_atual} mWh",
    formatacao=cor_dados
  )

  if saude is None:
    texto_saude = "Saúde estimada: indisponível"
  else:
    texto_saude = f"Saúde estimada: {saude:.1f}%"

  if ciclos is None:
    texto_ciclos = "Ciclos: não disponíveis no relatório."
  else:
    texto_ciclos = f"Ciclos reportados pelo Windows: {ciclos}"

  saida_terminal.desenhar_tela_terminal(texto=texto_ciclos, formatacao=cor_dados)

  if ciclos is not None and saude_esperada is not None:
    saida_terminal.desenhar_tela_terminal(
      texto=f"Saúde de referência para {ciclos} ciclos: {saude_esperada:.1f}% "
      "(heurística: 80% após 1000 ciclos)",
      formatacao=cor_dados
    )

  cor_resultado = saida_terminal.COMBINACOES_CORES[cor_analise]
  saida_terminal.desenhar_tela_terminal(
    texto=texto_saude,
    formatacao=cor_resultado
  )
  saida_terminal.desenhar_tela_terminal(
    texto=f"Análise: {analise}",
    formatacao=cor_resultado
  )
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)
  
  ferramentas.terminal(tipo=1, comando="pause")
  
  


if __name__ == "__main__":
  # precisava testar com urgência, então é...
  vida_bateria()