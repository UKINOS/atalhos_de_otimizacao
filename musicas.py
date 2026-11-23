"""Isso é só pela besteira, dependendo eu deveria colocar ele em main.py em vez de fazer um código separado...
"""

import time
import winsound


import caminhos_e_variaveis_globais
import saida_terminal



# Frequências das notas
FREQUENCIA_NOTAS = {
    # Oitava 2
    'C2': 65, 'C#2': 69, 'D2': 73, 'D#2': 78, 'E2': 82, 'F2': 87, 'F#2': 92, 'G2': 98, 'G#2': 104, 'A2': 110, 'A#2': 117, 'B2': 123,
    # Oitava 3
    'C3': 131, 'C#3': 139, 'D3': 147, 'D#3': 156, 'E3': 165, 'F3': 175, 'F#3': 185, 'G3': 196, 'G#3': 208, 'A3': 220, 'A#3': 233, 'B3': 247,
    # Oitava 4
    'C4': 261, 'C#4': 277, 'D4': 294, 'D#4': 311, 'E4': 329, 'F4': 349, 'F#4': 370, 'G4': 392, 'G#4': 415, 'A4': 440, 'A#4': 466, 'B4': 494,
    # Oitava 5
    'C5': 523, 'C#5': 554, 'D5': 587, 'D#5': 622, 'E5': 659, 'F5': 698, 'F#5': 740, 'G5': 784, 'G#5': 830, 'A5': 880, 'A#5': 932, 'B5': 987,
    # Oitava 6
    'C6': 1046, 'C#6': 1108, 'D6': 1174, 'D#6': 1244, 'E6': 1318, 'F6': 1396, 'F#6': 1480, 'G6': 1568, 'G#6': 1661, 'A6': 1760, 'A#6': 1864, 'B6': 1975,
    # Notas usadas anteriormente (para garantir que estejam presentes)
    'null': 0
}



def tocar_musica(partitura, mostrar_nota=False):
  """Música braba

  Args:
    partitura (list(nota, duração))|str: A nota será comparada com a variável no mesmo código, e a duração será enviada... E se você cometer o erro de enviar o nome da música em vez da partitura, ele resolve isso na hora...
    mostrar_nota (bool): Usado apenas no modo teste, não deve ser usado em nenhum outro caso...
  """
  
  if type(partitura) == str:
    partitura = caminhos_e_variaveis_globais.MUSICAS.get(partitura)
  
  for nota, tempo in partitura:
    # Pra que isso dipsy
    if mostrar_nota:
      saida_terminal.lista_alternada(lista=f"{nota}", enumerado=tempo)
    
    winsound.Beep(int(FREQUENCIA_NOTAS.get(nota)), tempo)
    time.sleep(0.1)
    
    if mostrar_nota:
      saida_terminal.delete_last_line()