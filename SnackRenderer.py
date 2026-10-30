from __future__ import annotations
import pygame

STAGE_W, STAGE_H = 480, 360

class Renderer:
    def draw(self):
        self.fill((255, 255, 255))