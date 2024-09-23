import pygame

# Inicializar o Pygame
pygame.init()

# Definir dimensões da tela
largura, altura = 540, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Sudoku Interface")

# Cores
PRETO = (0, 0, 0)
AZUL_CLARO = (255, 0, 0)

# Dimensões da célula
largura_celula = 60
altura_celula = 60
margem_superior = 60  # Deixar um espaço em cima

# Carregar imagem de fundo
imagem_fundo = pygame.image.load('imagem/sandy.jpg')  # Altere para o nome da sua imagem
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))  # Redimensiona a imagem para caber na tela

# Função para desenhar a grade de Sudoku
def desenhar_grade():
    for i in range(10):  # 9 linhas principais + 1 borda final
        largura_linha = 4 if i % 3 == 0 else 1  # Linhas grossas a cada 3 quadrados
        pygame.draw.line(tela, PRETO, (i * largura_celula, margem_superior), (i * largura_celula, margem_superior + 9 * altura_celula), largura_linha)
        pygame.draw.line(tela, PRETO, (0, margem_superior + i * altura_celula), (9 * largura_celula, margem_superior + i * altura_celula), largura_linha)

# Função para realçar a célula selecionada
def desenhar_selecao(selecionado):
    if selecionado:
        linha, coluna = selecionado
        pygame.draw.rect(tela, AZUL_CLARO, (coluna * largura_celula, margem_superior + linha * altura_celula, largura_celula, altura_celula), 3)

# Função para detectar clique e selecionar célula
def obter_celula_clicada(pos):
    if pos[0] < 9 * largura_celula and pos[1] > margem_superior:
        coluna = pos[0] // largura_celula
        linha = (pos[1] - margem_superior) // altura_celula
        return (linha, coluna)
    return None

# Loop principal
def main():
    rodando = True
    selecionado = None  # Nenhuma célula selecionada no início

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Captura o evento de fechar a janela
                rodando = False  # Encerra o loop

            if evento.type == pygame.MOUSEBUTTONDOWN:  # Captura cliques do mouse
                pos = pygame.mouse.get_pos()
                selecionado = obter_celula_clicada(pos)

        # Desenhar a imagem de fundo
        tela.blit(imagem_fundo, (0, 0))

        desenhar_grade()  # Desenhar a grade do Sudoku
        desenhar_selecao(selecionado)  # Realçar célula selecionada
        pygame.display.update()  # Atualizar a tela

    pygame.quit()  # Fecha a janela quando o loop termina

if __name__ == "__main__":
    main()
