import pygame
import sys

from SnackRenderer import Renderer

def main():
    pygame.init()
    try:
        screen = pygame.display.set_mode((480, 360))
        renderer = Renderer
        clock = pygame.time.Clock()
        pygame.display.set_caption("snack")
        running = True

        while running:
            dt = min(clock.tick(30) / 1000.0, 0.1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            renderer.draw(screen)
            pygame.display.flip()
    except Exception as exc:
        print(f"Error: {exc}")
        raise
    finally:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()