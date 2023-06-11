from selenium import webdriver
from datetime import date
import os
import time
from git import Repo
import pyautogui

# Inicializar o driver do Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# URL do repositório remoto
remote_repo_url = "https://github.com/viniciuszile/Python_Bot.git"

# Diretório local do repositório
local_repo_folder = os.path.join(os.getcwd(), "Python_Bot")

# Verificar se o diretório local do repositório existe, caso contrário, clonar
if not os.path.exists(local_repo_folder):
    repo = Repo.clone_from(remote_repo_url, local_repo_folder)
else:
    repo = Repo(local_repo_folder)

# Diretório local das imagens
local_image_folder = os.path.join(local_repo_folder, "Prints")

# Verificar se a pasta "Prints" existe no diretório local
if not os.path.exists(local_image_folder):
    print("Pasta 'Prints' não encontrada. Certifique-se de que a pasta 'Prints' existe no diretório"
          "local do repositório.")
    print("Programa encerrado.")
    exit()

# Lista de jogadores e links correspondentes
jogadores = {
    "Zile": "https://tracker.gg/valorant/profile/riot/Zile%23FEC/overview",
    "Minideca": "https://tracker.gg/valorant/profile/riot/minideca%23FEC/overview",
    "Gabigol": "https://tracker.gg/valorant/profile/riot/SenaiGabigol%23Fec/overview",
    "Vitin": "https://tracker.gg/valorant/profile/riot/ViTiN%23fec/overview"
}

# Obter a data atual
data_atual = date.today().strftime('%d-%m-%Y')

# Iterar sobre cada jogador e seu respectivo link
for jogador, link in jogadores.items():
    # Navegar para o link específico
    driver.get(link)

    # Aguardar 3 segundos
    time.sleep(3)

    # Aguardar um pequeno intervalo de tempo para garantir que a página esteja carregada
    time.sleep(2)

    # Simular pressionar a tecla de seta para baixo 10 vezes
    num_rolagens = 10
    for _ in range(num_rolagens):
        pyautogui.press('down')
        time.sleep(1)  # Ajuste o tempo de espera conforme necessário

    # Pasta do jogador
    jogador_folder = os.path.join(local_image_folder, jogador)

    # Verificar se a pasta do jogador já existe, caso contrário, criar
    if not os.path.exists(jogador_folder):
        os.makedirs(jogador_folder)

    # Caminho completo para o arquivo de screenshot
    screenshot_path = os.path.join(jogador_folder, f"{jogador}_{data_atual}.png")

    # Capturar o screenshot da página
    driver.save_screenshot(screenshot_path)

    print(f"Imagem do jogador {jogador} capturada com sucesso.")

# Fechar o navegador
driver.quit()
# Fazer commit e push das alterações para o repositório remoto
repo.git.add(A=True)
repo.git.commit(m=f"Upando os ranks do dia ({data_atual})")
repo.git.push("--force")

print("Todas as imagens foram capturadas e enviadas para o repositório com sucesso.")
print("Programa encerrado.")