import pygame

class Button:
    def __init__(self, rect: pygame.Rect, cornerRadius: int):
        self.rect = rect
        self.font = pygame.Font(None, 32)
        self.cornerRadius = cornerRadius

    def draw(self, surface: pygame.Surface, text: str, color: pygame.Color, textColor: pygame.Color):
        pygame.draw.rect(surface, color, self.rect, 0, self.cornerRadius)
        self._drawText(surface, text, textColor)
    
    def _drawText(self, surface: pygame.Surface, text: str, textColor: pygame.Color):
        txt = self.font.render(text, True, textColor)
        txtRect = txt.get_rect()
        txtRect.center = self.rect.center

        surface.blit(txt, (txtRect.x, txtRect.y))
    
    def isClicked(self, events: pygame.Event) -> bool:
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        return True
        return False
