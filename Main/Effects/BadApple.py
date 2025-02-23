import pygame
import sys
import ctypes
from ffpyplayer.player import MediaPlayer

# Caminho do vídeo
VIDEO_PATH = "badapple.mp4"


# Configurar a API do Windows para bloquear comandos como Alt+Tab e Alt+F4
def block_keys():
    hwnd = pygame.display.get_wm_info()["window"]

    # Mantém a janela sempre no topo e remove a barra de tarefas
    ctypes.windll.user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0001 | 0x0002)

    # Impede Alt+Tab, Ctrl+Esc, Alt+F4 (Requer rodar como Administrador)
    ctypes.windll.user32.SystemParametersInfoW(97, 0, 0, 0)


# Função principal do vídeo
def play_video():
    pygame.init()

    # Tela Fullscreen
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Modo Bloqueado")

    # Bloquear teclas no Windows
    block_keys()

    # Carregar o vídeo
    player = MediaPlayer(VIDEO_PATH)
    clock = pygame.time.Clock()

    running = True
    while running:
        frame, val = player.get_frame()
        if val == 'eof':  # Se o vídeo acabar, reinicia
            player.close_player()
            player = MediaPlayer(VIDEO_PATH)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Impedir fechamento
                pass
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Impedir ESC
                    pass

        # Exibir vídeo centralizado
        if frame is not None:
            img, _ = frame
            img = pygame.image.frombuffer(img.to_bytearray()[0], img.get_size(), "RGB")

            screen_width, screen_height = screen.get_size()
            video_width, video_height = img.get_size()
            x = (screen_width - video_width) // 2
            y = (screen_height - video_height) // 2

            screen.blit(img, (x, y))

        pygame.display.update()
        clock.tick(30)

    player.close_player()
    pygame.quit()
    sys.exit()


# Loop Infinito: Se fechar, reabre
while True:
    play_video()

