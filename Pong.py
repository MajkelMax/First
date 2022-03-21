from livewires import games, color
import random

# Gra w której odbijasz

games.init(screen_width=1152, screen_height=648, fps=50)


class Dvd(games.Sprite):
    """
    obiekt będzie odbijał się od bocznych i górnej krawędzi
    jeżeli spadnie na sam dół gra kończy się
    """
    image = games.load_image("DVD.png")

    def __init__(self):
        super(Dvd, self).__init__(image=Dvd.image,
                                  x=games.screen.height / 2,
                                  y=games.screen.width / 2,
                                  dx=-1,
                                  dy= -1)

        self.score = games.Text(value=0, size=25, color=color.white,
                                top=5, right=games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        """ Po osiągnięciu brzegu ekranu zmień poruszanie się na przeciwne"""
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
        if self.top < 0:
            self.dy = -self.dy
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

        self.check_catch()

    def check_catch(self):
        """ Sprawdź, czy nie zostały złapane jakieś pizze. """
        for dvd in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            self.dy = -self.dy

        self.difficulty()

    def difficulty(self):
        """ Zwiększenie poziomu trudności po osiągnięciu progu pkt """
        if self.score.value == 20:
            if self.dx == -1:
                self.dx = -4
            if self.dx == 1:
                self.dx = 4
            if self.dy == 1:
                self.dy = 4
        #stage 3
        if self.score.value == 100:
            if self.dx == -4:
                self.dx = -6
            if self.dx == 4:
                self.dx = 6
            if self.dy == 4:
                self.dy = 6

    def handle_caught(self):
        self.destroy()

    def end_game(self):
        """ Zakończ grę. """
        end_message = games.Message(value="Koniec gry",
                                    size=90,
                                    color=color.white,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)


class Belka(games.Sprite):
    """
    belka którą poruszamy w lewo lub w prawo, odbiją ona dvd w -dx -dy
    """
    image = games.load_image("belka.png")

    def __init__(self):
        super(Belka, self).__init__(image=Belka.image,
                                    x=games.mouse.x,
                                    bottom=games.screen.height)


    def update(self):
        """ Zmień pozycję na wyznaczoną przez współrzędną x myszy. """
        if games.keyboard.is_pressed(games.K_LEFT):
            self.x -= 4
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.x += 4

        if self.left < 0:
            self.left = 0

        if self.right > games.screen.width:
            self.right = games.screen.width



def main():
    """ Uruchom grę. """
    wall_image = games.load_image("background.png", transparent=False)
    games.screen.background = wall_image

    the_dvd = Dvd()
    games.screen.add(the_dvd)

    the_belka = Belka()
    games.screen.add(the_belka)

    games.mouse.is_visible = False
    games.screen.event_grab = True

    games.screen.mainloop()


main()
