import win32api
import win32gui

# Configura o espaço de tela utiliazavel
screen_dc = win32gui.GetDC(0)

# Cria um pincel para colorir o retangulo
brush = win32gui.CreateSolidBrush(win32api.RGB(255,0,0)) #interior, para bordas usar o PEN

# Seleciona o brush para ser usado no DC
win32gui.SelectObject(screen_dc,brush)

# Define o retângulo
win32gui.Rectangle(screen_dc,50,200,500,400) # Esquerda Topo Direita Baixo

# Cria uma linha
#win32gui.LineTo(screen_dc,1000,600)