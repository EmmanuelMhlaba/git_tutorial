class StartMenu:
    def __init__(self):
        self.screen = 1

    def showScreen(self):
        if (self.screen == 1):
            self.showStartScreen()

    def showStartScreen(self):
        print("This is the start menu, welcome!")
