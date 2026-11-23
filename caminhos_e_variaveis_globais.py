"""Esse código serve como uma otimização para evitar paredes longas de código... Esse código é apenas um dummy...
"""

DELAY_VALORES = {
  "normal" : 0.1,
  "rápido" : 0.01,
  "sonic"  : 0
}


# Não gerei grande parte desta lista com IA confia kkkkkkkkkkkkkkkkkk
DELETE_RECURSIVO_TEMPORARIOS = [
  # Windows & Sistema (Incluindo WER e LiveKernelReports)
  R"C:\Windows\Temp",
  R"%TEMP%",
  R"C:\Windows\Prefetch",
  R"C:\Windows\SoftwareDistribution\Download",
  R"C:\Windows\SoftwareDistribution\DataStore",
  R"C:\Windows\SoftwareDistribution\Target",
  R"C:\Windows\Logs\CBS",
  R"C:\Windows\Logs\Diagnostic",
  R"C:\Windows\Logs\MoSetup",
  R"C:\Windows\Minidump",
  R"C:\Windows\Panther",
  R"C:\Windows\Panther\NewOS",
  R"C:\Windows\System32\LogFiles\WMI",
  R"C:\Windows\SysWOW64\LogFiles",
  R"C:\ProgramData\Microsoft\Windows\WER",
  R"C:\Windows\LiveKernelReports",
  R"%LOCALAPPDATA%\CrashDumps",
  R"%LOCALAPPDATA%\D3DSCache",
  R"%LOCALAPPDATA%\Packages\Microsoft.WindowsStore_8wekyb3d8bbwe\LocalCache",
  R"%LOCALAPPDATA%\Microsoft\Windows\INetCache",
  R"%LOCALAPPDATA%\Microsoft\Windows\WebCache",
  R"%LOCALAPPDATA%\Microsoft\WindowsApps\Cache",

  # Nvidia, AMD e Intel
  R"C:\ProgramData\NVIDIA Corporation\Downloader",
  R"C:\ProgramData\NVIDIA\Installer2",
  R"%LOCALAPPDATA%\NVIDIA\DXCache",
  R"%LOCALAPPDATA%\NVIDIA\GLCache",
  R"C:\AMD",
  R"C:\AMD\Log",
  R"%LOCALAPPDATA%\AMD\DxCache",
  R"%LOCALAPPDATA%\AMD\GLCache",
  R"%LOCALAPPDATA%\AMD\DxcCache",
  R"C:\Intel\Logs",

  # Python, Dev, Editores e Ferramentas (Docker, Gradle, Maven, JetBrains, VS Code)
  R"%LOCALAPPDATA%\pip\cache",
  R"%LOCALAPPDATA%\npm-cache",
  R"%APPDATA%\npm-cache",
  R"%LOCALAPPDATA%\Yarn\Cache",
  R"%APPDATA%\Code\Cache",
  R"%APPDATA%\Code\CachedData",
  R"%LOCALAPPDATA%\Microsoft\vscode-cpptools\ipch",
  R"%LOCALAPPDATA%\NuGet\v3-cache",
  R"%USERPROFILE%\.cargo\registry\cache",
  R"%LOCALAPPDATA%\Docker\log",
  R"%USERPROFILE%\.gradle\caches",
  R"%USERPROFILE%\.m2\repository\.cache",
  R"%USERPROFILE%\.android\cache",
  R"%LOCALAPPDATA%\Pub\Cache",
  R"%APPDATA%\Hex\cache",
  R"%LOCALAPPDATA%\go-build",
  R"%USERPROFILE%\.dotnet\sdk\NuGetFallbackFolder",
  R"%LOCALAPPDATA%\Microsoft\VisualStudio\Cache",

  # Discord
  R"%APPDATA%\discord\Cache",
  R"%APPDATA%\discord\Code Cache",
  R"%LOCALAPPDATA%\Discord\Cache",
  R"%LOCALAPPDATA%\Discord\Code Cache",
  R"%APPDATA%\discordptb\Cache",
  R"%APPDATA%\discordptb\Code Cache",
  R"%APPDATA%\discordcanary\Cache",
  R"%APPDATA%\discordcanary\Code Cache",
  R"%APPDATA%\discorddevelopment\Cache",
  R"%APPDATA%\discorddevelopment\Code Cache",
  
  # Fluxer
  R"%APPDATA%\fluxer\Cache",
  R"%APPDATA%\fluxer\Code Cache",
  R"%APPDATA%\fluxer_canary\Cache",
  R"%APPDATA%\fluxer_canary\Code Cache",

  # WhatsApp
  R"%APPDATA%\WhatsApp\Cache",
  R"%APPDATA%\WhatsApp\Code Cache",
  R"%LOCALAPPDATA%\WhatsApp\Cache",

  # Launchers de Games e Lojas
  R"%LOCALAPPDATA%\Steam\htmlcache",
  R"%LOCALAPPDATA%\Steam\appcache\httpcache",
  R"%LOCALAPPDATA%\EpicGamesLauncher\Saved\webcache",
  R"%LOCALAPPDATA%\EpicGamesLauncher\Saved\Logs",
  R"%LOCALAPPDATA%\Electronic Arts\EA Desktop\Logs",
  R"%LOCALAPPDATA%\Electronic Arts\EA Desktop\webcache",
  R"%LOCALAPPDATA%\Origin\Logs",
  R"%LOCALAPPDATA%\Ubisoft Game Launcher\cache",
  R"%LOCALAPPDATA%\Ubisoft Game Launcher\logs",
  R"%LOCALAPPDATA%\Battle.net\Cache",
  R"%LOCALAPPDATA%\Blizzard Entertainment\Battle.net\Cache",
  R"%LOCALAPPDATA%\GOG.com\Galaxy\webcache",
  R"%PROGRAMDATA%\GOG.com\Galaxy\webcache",
  R"%LOCALAPPDATA%\Riot Games\Riot Client\Data\Logs",
  R"%LOCALAPPDATA%\Riot Games\Riot Client\Caches",
  R"%LOCALAPPDATA%\Rockstar Games\Launcher\webcache",
  R"%LOCALAPPDATA%\Rockstar Games\Launcher\Logs",
  R"%LOCALAPPDATA%\Roblox\logs",
  R"%LOCALAPPDATA%\Roblox\Downloads",
  R"%LOCALAPPDATA%\CurseForge\Install\Logs",
  R"%LOCALAPPDATA%\Itch\itch\Cache",
  R"%APPDATA%\itch\Cache",
  R"%APPDATA%\Pupae",

  # Navegadores e Mídia
  R"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache",
  R"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Code Cache",
  R"%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\Cache",
  R"%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\Code Cache",
  R"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data\Default\Cache",
  R"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data\Default\Code Cache",
  R"%LOCALAPPDATA%\Opera Software\Opera Stable\Cache",
  R"%LOCALAPPDATA%\Opera Software\Opera GX Stable\Cache",
  R"%LOCALAPPDATA%\Vivaldi\User Data\Default\Cache",
  R"%LOCALAPPDATA%\Tor Browser\Browser\Caches",
  R"%APPDATA%\Adobe\Common\Media Cache Files",
  R"%LOCALAPPDATA%\Spotify\Data",
]



# Defina as notas e suas durações (em milissegundos) para Für Elise - Versão Estendida
MUSICAS = {
  "FUR_ELISE" : [
      # Seção A (como no seu código)
      ('E5', 200), ('D#5', 200), ('E5', 200), ('D#5', 200), ('E5', 200), ('B4', 200), ('D5', 200), ('C5', 200),
      ('A4', 600), ('C4', 200), ('E4', 200), ('A4', 200), ('B4', 600), ('E4', 200), ('G#4', 200), ('B4', 200),
      ('C5', 600), ('E4', 200), ('E5', 200), ('D#5', 200), ('E5', 200), ('D#5', 200), ('E5', 200), ('B4', 200), ('D5', 200), ('C5', 200),
      ('A4', 600), ('C4', 200), ('E4', 200), ('A4', 200), ('B4', 600), ('E4', 200), ('G#4', 200), ('B4', 200),
      ('A4', 600), ('E4', 200), ('A4', 200), ('C5', 200), ('E5', 200), ('A5', 200), ('B5', 200), ('E5', 200), ('D5', 200),
      ('C5', 200), ('A4', 1000),

      # Transição para a Seção B
      ('C5', 200), ('E5', 200), ('A5', 200), ('C6', 200),
      ('B5', 200), ('G5', 200), ('E5', 200), ('C5', 200),
      ('D5', 200), ('F#5', 200), ('A5', 200), ('D6', 200),
      ('C6', 200), ('A4', 200), ('F4', 200), ('D4', 200),

      # Seção B
      ('G4', 400), ('G4', 200), ('A4', 200), ('B4', 400), ('B4', 200), ('C5', 200),
      ('D5', 400), ('D5', 200), ('E5', 200), ('F#5', 400), ('F#5', 200), ('G5', 200),
      ('A5', 400), ('A5', 200), ('G5', 200), ('F#5', 400), ('F#5', 200), ('E5', 200),
      ('D5', 400), ('D5', 200), ('C5', 200), ('B4', 400), ('B4', 200), ('A4', 200),

      ('G4', 400), ('G4', 200), ('A4', 200), ('B4', 400), ('B4', 200), ('C5', 200),
      ('D5', 400), ('D5', 200), ('E5', 200), ('F#5', 400), ('F#5', 200), ('G5', 200),
      ('A5', 400), ('A5', 200), ('G5', 200), ('F#5', 400), ('F#5', 200), ('E5', 200),
      ('D5', 400), ('D5', 200), ('C5', 200), ('B4', 400), ('A4', 600), ('G4', 200),

      # Retorno à Seção A (trecho)
      ('E5', 200), ('D#5', 200), ('E5', 200), ('D#5', 200), ('E5', 200), ('B4', 200), ('D5', 200), ('C5', 200),
      ('A4', 1000)
  ],

  "END__FUR_ELISE" : [
      # Retorno à Seção A (trecho)
      ('E5', 200), ('D#5', 200), ('E5', 200), ('D#5', 200), ('E5', 200), ('B4', 200), ('D5', 200), ('C5', 200),
      ('A4', 1000)
  ],

  # Ode à Alegria - Beethoven (Versão completa e épica)
  "ODE_ALEGRIA" : [
      # Primeira frase - Tema principal (E menor)
      ('E4', 250), ('E4', 250), ('F#4', 250), ('G#4', 250),
      ('A4', 250), ('A4', 250), ('A4', 250), ('G#4', 250),
      ('A4', 250), ('B4', 250), ('C#5', 250), ('D5', 250),
      ('E5', 500),
      
      # Repetição do tema com variação
      ('E5', 250), ('D5', 250), ('C#5', 250), ('B4', 250),
      ('C#5', 250), ('D5', 250), ('E5', 250), ('B4', 250),
      ('C#5', 250), ('D5', 250), ('E5', 500),
      
      # Segunda frase - Subida melódica
      ('E5', 250), ('E5', 250), ('E5', 250), ('E5', 250),
      ('F#5', 250), ('G#5', 250), ('A5', 250), ('B5', 250),
      ('C#6', 500), ('C#6', 250), ('B5', 250),
      
      # Terceira frase - Descida melódica
      ('A5', 250), ('G#5', 250), ('F#5', 250), ('E5', 250),
      ('D5', 250), ('C#5', 250), ('B4', 250), ('A4', 250),
      ('B4', 500), ('B4', 250), ('A4', 250),
      
      # Volta ao tema principal
      ('E4', 250), ('E4', 250), ('F#4', 250), ('G#4', 250),
      ('A4', 250), ('A4', 250), ('A4', 250), ('G#4', 250),
      ('A4', 250), ('B4', 250), ('C#5', 250), ('D5', 250),
      
      # Toquezinho final de encerramento (notas mais altas)
      ('G5', 100), ('A5', 100), ('B5', 100), ('E6', 200),
      
      # Final épico - Nota longa
      ('E5', 500), ('A4', 2000)
  ],

  # Happy Birthday
  "HAPPY_BIRTHDAY" : [
      ('C4', 200), ('C4', 200), ('D4', 400), ('C4', 400), ('F4', 400), ('E4', 800),
      ('C4', 200), ('C4', 200), ('D4', 400), ('C4', 400), ('G4', 400), ('F4', 800),
      ('C4', 200), ('C4', 200), ('C5', 400), ('A4', 400), ('F4', 400), ('E4', 400), ('D4', 400),
      ('A#4', 200), ('A#4', 200), ('A4', 400), ('F4', 400), ('G4', 400), ('F4', 800)
  ],

  # Marcha de Zacarias (Wagner) - trecho épico
  "MARCHA_ZACARIAS" : [
      ('E4', 150), ('E4', 150), ('E4', 150), ('E4', 150), ('E4', 300),
      ('G4', 150), ('E4', 300), ('A4', 300),
      ('B4', 600), ('B4', 300), ('B4', 300),
      ('E4', 150), ('E4', 150), ('E4', 150), ('E4', 150), ('E4', 300),
      ('G4', 150), ('E4', 300), ('A4', 300),
      ('B4', 900)
  ],

  # Twinkle Twinkle Little Star
  "TWINKLE_TWINKLE" : [
      ('C4', 450), ('C4', 450), ('G4', 450), ('G4', 450), ('A4', 450), ('A4', 450), ('G4', 900),
      ('F4', 450), ('F4', 450), ('E4', 450), ('E4', 450), ('D4', 450), ('D4', 450), ('C4', 900),
      ('G4', 450), ('G4', 450), ('F4', 450), ('F4', 450), ('E4', 450), ('E4', 450), ('D4', 900),
      ('G4', 450), ('G4', 450), ('F4', 450), ('F4', 450), ('E4', 450), ('E4', 450), ('D4', 900),
      ('C4', 450), ('C4', 450), ('G4', 450), ('G4', 450), ('A4', 450), ('A4', 450), ('G4', 900),
      ('F4', 450), ('F4', 450), ('E4', 450), ('E4', 450), ('D4', 450), ('D4', 450), ('C4', 1350)
  ]
}


MMA_COMANDS = {
    "Prefetch_geral" : {
        True  : "powershell -Command \"Enable-MMAgent -ApplicationLaunchPrefetching\"",
        False : "powershell -Command \"Disable-MMAgent -ApplicationLaunchPrefetching\""
    },
    
    "Superprefetch" : {
        True  : "powershell -Command \"Enable-MMAgent -ApplicationPreLaunch\"",
        False : "powershell -Command \"Disable-MMAgent -ApplicationPreLaunch\""
    },
    
    "Compressão RAM" : {
        True  : "powershell -Command \"Enable-MMAgent -MemoryCompression\"",
        False : "powershell -Command \"Disable-MMAgent -MemoryCompression\""
    }
}



# Variável_global
delay = DELAY_VALORES.get("normal")
som = True