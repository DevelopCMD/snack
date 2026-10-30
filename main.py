import pygame
import sys

def main():
    pygame.init()
    try:
        screen = pygame.display.set_mode((480, 360))
        clock = pygame.time.Clock()
        pygame.display.set_caption("snack")
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill((255, 255, 255))
            dt = min(clock.tick(30) / 1000.0, 0.1)
            pygame.display.flip()
            clock.tick(dt)
    except Exception as exc:
        print(f"Error: {exc}")
        raise
    finally:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()