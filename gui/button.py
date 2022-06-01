class Button:
    '''
    This class describes the interface buttons, their design etc.
    '''

    def __init__(self, pos, font, image, base_color, hovering_color,
                 text_input):
        self.x = pos[0]
        self.y = pos[1]
        self.font = font
        self.image = image
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.text_rect = self.text.get_rect(center=(self.x, self.y))

    def update(self, win):
        '''
        Updates the button on the window.
        '''
        if self.image is not None:
            win.blit(self.image, self.rect)
        win.blit(self.text, self.text_rect)

    def checkForInput(self, mouse_pos):
        '''
        Checks for mouse input on the button.
        '''
        if mouse_pos[0] in range(
                self.rect.left + 20,
                self.rect.right - 20) and mouse_pos[1] in range(
                    self.rect.top + 25, self.rect.bottom - 40):
            return True
        return False

    def changeTextColor(self, mouse_pos):
        '''
        Changes the color of the text on the button when hovering.
        '''
        if self.checkForInput(mouse_pos):
            self.text = self.font.render(self.text_input, True,
                                         self.hovering_color)
