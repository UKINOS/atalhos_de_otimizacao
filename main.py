"""Bem vindo ao caos generalizado. Sente-se e chore.
Aqui, a gente é o chefe q apenas manda nos outros e quase não faz nada kkkkkkk
"""

# Importação interna
import sys


# Código externo - necessário
import caminhos_e_variaveis_globais
import comportamentos
import configuracoes
import entrada_usuario
import ferramentas
import limpeza_e_organizacao
import musicas
import saida_terminal



# Código externo - Desnecessário
# Toda a importação de código extra deve ser lidada pela biblioteca abaixo
deteccao_codigo_externo = None

try:
  # Define pasta padrão
  sys.path.append(".")
  
  # Código externo - Não é necessário pra execução do código principal
  import codigo_externo

  # Se chegou aqui, rodou de boa
  deteccao_codigo_externo = True

except ImportError as erro:
  saida_terminal.desenhar_tela_terminal(texto=f"Code alert 1 - Resposta esperada - {erro}", formatacao=["NEGRITO", "TEXTO_PRETO", "FUNDO_AMARELO"], add_to_buffer_text=False)
  saida_terminal.desenhar_tela_terminal(texto="Code alert 1 - Apesar de sua presença ser esperada, não é necessário que \"codigo_externo.py\" esteja presente para a funcionalidade do main...", add_to_buffer_text=False)
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)
  input("Aperte enter para continuar...")
  
  deteccao_codigo_externo = False
  
  pass

except Exception as erro:
  saida_terminal.desenhar_tela_terminal(texto=f"Code exit 1 - Resposta inesperada - {erro}", formatacao=["NEGRITO", "TEXTO_BRANCO", "FUNDO_VERMELHO"], add_to_buffer_text=False)
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)
  sys.exit(1)
   
   

if not ferramentas.eh_admin():
  saida_terminal.desenhar_tela_terminal(texto=f"Code exit 2 - O código não está sendo executado como administrador", formatacao=["NEGRITO", "TEXTO_BRANCO", "FUNDO_VERMELHO"], add_to_buffer_text=False)
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"], quebra_de_linha=False)
  sys.exit(1)


OPCOES_ORIGINAL = {
  "Otimização geral" : [
    "Voltar",
    "Limpeza de arquivos temporários",
    "Desfragmentador de HDD/SSD",
    "Hibernação",
    "Inicialização mais rápida do Explorer",
  ],
  
  "Otimizações específicas" : [
    "Voltar",
    "Plano de energia de desempenho máximo",
    "Inicialização rápida",
    "Aceleração de hardware",
    "Indexação do Windows",
    "sysmain - prefetch / superprefetch / compressão ram"
  ],
  
  "Sistema Operacional (Windows) e outros" : [
    "Voltar",
    "Verificação de armazenamento",
    "Verificação de corrupção no sistema",
    "Relatório bateria",
    "Atualização de aplicativos utilizando winget"
  ],
  
  "Configurações do código" : [
    "Voltar",
    "Desativar música/aviso",
    "Teste música",
    "Interface v.s. Velocidade"
  ],
  
  "Encerrar código" : [
    "Voltar",
    "Encerrar código"
  ]
}


if deteccao_codigo_externo == False:  # O código externo existe?
  opcoes = OPCOES_ORIGINAL
  
elif not codigo_externo.opcoes_extra: # A lista está vazia?
  opcoes = OPCOES_ORIGINAL
  
else:
  opcoes = OPCOES_ORIGINAL | codigo_externo.opcoes_extra


   
try:
  while True:
    # # Teste de except
    # raise MemoryError("Test")
    
    saida_terminal.apagar_terminal()
    saida_terminal.apagar_buffer([True, True])
    
    resposta = entrada_usuario.menu_escolha(nome="Atalhos para otimizar PC", lista=opcoes)
    
    # DLC?
    if resposta [0] not in OPCOES_ORIGINAL:
      codigo_externo.menu_de_opcoes_extra(resposta)
      
      continue
    
    
    # Tabom, estamos indo solo
    if resposta[0] == "Otimização geral":
      if resposta[1] == "Limpeza de arquivos temporários":
        # É muita linha de código, precisei jogar pra outro lugar...
        limpeza_e_organizacao.limpeza_arquivos_temporarios()
        if caminhos_e_variaveis_globais.som: musicas.tocar_musica("END__FUR_ELISE")

        
      elif resposta[1] == "Desfragmentador de HDD/SSD":
        # Se no futuro for adicionar compatibilidade com Linux, adicionar verificação de Windows...
        limpeza_e_organizacao.desfragmentador()
        if caminhos_e_variaveis_globais.som: musicas.tocar_musica("ODE_ALEGRIA")
        
        
      elif resposta[1] == "Hibernação":
        # Não vou deixar o main ficar sujo kkkk
        comportamentos.hibernacao()
        if caminhos_e_variaveis_globais.som: musicas.tocar_musica("END__FUR_ELISE")
        
        
      elif resposta[1] == "Inicialização mais rápida do Explorer":
        # Essa daqui acabei fazendo com IA, mas não se preocupa q ta funcionando de boa
        comportamentos.inicializacao_rapida_explorer()
        
        
    elif resposta[0] == "Otimizações específicas":
      if resposta[1] == "Plano de energia de desempenho máximo":
        # Precisa de mais potência?
        comportamentos.plano_de_energia()
        
        
      elif resposta[1] == "Inicialização rápida":
        # Isso da problema dependendo da máquina kkk
        comportamentos.inicializacao_rapida_windows()
        
        
      elif resposta[1] == "Aceleração de hardware":
        # Isso daqui pode ajudar ou piorar as coisas...
        comportamentos.aceleracao_de_hardware()
        
        
      elif resposta[1] == "Indexação do Windows":
        # E isso daqui pode ajudar pra quem não a usa...
        comportamentos.indexacao_windows()
        
        
      elif resposta[1] == "sysmain - prefetch / superprefetch / compressão ram":
        comportamentos.sysmain()
        
    
    elif resposta[0] == "Sistema Operacional (Windows) e outros":
      if resposta[1] == "Verificação de armazenamento":
        ferramentas.chkdsk()
        if caminhos_e_variaveis_globais.som: musicas.tocar_musica("ODE_ALEGRIA")
        
        
      elif resposta[1] == "Verificação de corrupção no sistema":
        # Música curta pra retorno rápido, ou longa pro segundo retorno longo
        final_longo_musica = comportamentos.sistema_corrompido()
        if final_longo_musica:
          if caminhos_e_variaveis_globais.som: musicas.tocar_musica("FUR_ELISE")
        else:
          if caminhos_e_variaveis_globais.som: musicas.tocar_musica("END__FUR_ELISE")
        
      elif resposta[1] == "Relatório bateria":
        # Por favor não me julgue, essa função funciona na base da IA e sonhos kkkkkk
        comportamentos.vida_bateria()
        
        
      elif resposta[1] == "Atualização de aplicativos utilizando winget":
        # Acho q esse é o único q não vai ter função externa kkkkk
        ferramentas.terminal(tipo=1, comando="winget upgrade --all")
        
        
    elif resposta[0] == "Configurações do código":
      if resposta[1] == "Desativar música/aviso":
        configuracoes.musica_aviso()
        
        
      elif resposta[1] == "Teste música":
        configuracoes.teste_musica()
        
        
      elif resposta[1] == "Interface v.s. Velocidade":
        configuracoes.velocidade_interface()
        
    
    elif resposta[0] == "Encerrar código":
      if resposta[1] == "Encerrar código":
        break
        
        
    # Isso daqui era só pra testes...
    # ferramentas.terminal(tipo=1, comando="pause")
    
    
except Exception as erro:
  saida_terminal.desenhar_tela_terminal(formatacao=["RESET"])
  saida_terminal.desenhar_tela_terminal(texto=f"Code exit 1 - Except Geral - {erro}", formatacao=["NEGRITO", "TEXTO_BRANCO", "FUNDO_VERMELHO"], add_to_buffer_text=False)
  saida_terminal.desenhar_tela_terminal(texto=f"Esse erro foi capturado pelo except geral, e isso é PREOCUPANTE...", formatacao=["RESET", "TEXTO_PRETO", "FUNDO_AMARELO"])
  saida_terminal.desenhar_tela_terminal(texto=f"Para sua segurança, a execução do código foi cancelada..., aguarde enquanto a gente tenta salvar esse erro em {ferramentas.local_de_erro}...")
  
  # Insere o código aqui, vagabundo
  # Depois :)
  # Depois quando? Quando conseguir uma namorada?!?
  ferramentas.deteccao_de_erro(nome="Code exit 1 - Except Geral", log=erro, parada=True)
  # FEITO!
  # Mais lento que um bicho preguiça...
  # Nota: Como a função acima encerra a execução automáticamente, não é necessário fazer mais nada...
  
  
# Pera, você saiu normalmente?!
mensagem = "Obrigado por utilizar meu código! :)"

for iterador in range(0, len(mensagem)):
  # O código original de "lista alternada" da \n automáticamente... e não vou alterar uma função só pra isso...
  saida_terminal.desenhar_tela_terminal(texto=f"{mensagem[iterador]}", quebra_de_linha=False, formatacao=saida_terminal.COMBINACOES_CORES[iterador % len(saida_terminal.COMBINACOES_CORES)])
  
# Achou que eu ia esquecer de rodar esse comando?
saida_terminal.desenhar_tela_terminal(formatacao=["RESET"])
if caminhos_e_variaveis_globais.som:
  musicas.tocar_musica("END__FUR_ELISE")