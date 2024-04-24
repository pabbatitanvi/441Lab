import sys
import pygame
import random
from sprite import Sprite
from pygame_combat import run_pygame_combat
from pygame_human_player import PyGameHumanPlayer
from lab5.landscape import get_landscape, elevation_to_rgba, get_elevation
from pygame_ai_player import PyGameAIPlayer, PyGameAICombatPlayer
#from lab3.travel_cost import get_route_cost
from lab12.episode import run_episode
from journal import journal
from lab4.rock_paper_scissor import ComputerPlayer

from pathlib import Path

sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

from lab2.cities_n_routes import get_randomly_spread_cities, get_routes

get_combat_bg = lambda pixel_map: elevation_to_rgba(
    get_elevation(pixel_map), "RdPu"
)

journal = journal()

pygame.font.init()
game_font = pygame.font.SysFont("Comic Sans MS", 15)


def get_landscape_surface(size):
    elevation = get_elevation(size)
    landscape = get_landscape(size)
    print("Created a landscape of size", landscape.shape)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3])
    return pygame_surface, elevation


def get_combat_surface(size):
    landscape = get_combat_bg(size)
    print("Created a landscape of size", landscape.shape)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3])
    return pygame_surface


def setup_window(width, height, caption):
    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return window


def displayCityNames(city_locations, city_names):
    for i, name in enumerate(city_names):
        text_surface = game_font.render(str(i) + " " + name, True, (0, 0, 150))
        screen.blit(text_surface, city_locations[i])

def get_route_cost(cities, city, to_city, elevation):
    cityElevations = []
    cityElevations.append(elevation[cities[city][0]][cities[city][1]])
    cityElevations.append(elevation[cities[to_city][0]][cities[to_city][1]])
    return (int)((cityElevations[1] - cityElevations[0]) * 100)

class State:
    def __init__(
        self,
        current_city,
        destination_city,
        travelling,
        encounter_event,
        cities,
        routes,
    ):
        self.current_city = current_city
        self.destination_city = destination_city
        self.travelling = travelling
        self.encounter_event = encounter_event
        self.cities = cities
        self.routes = routes


if __name__ == "__main__":
    size = width, height = 640, 480
    black = 1, 1, 1
    start_city = 0
    end_city = 9
    sprite_path = "assets/lego.png"
    sprite_speed = 0.5

    screen = setup_window(width, height, "Game World Gen Practice")

    landscape_surface, elevation = get_landscape_surface(size)
    print("1L")
    combat_surface = get_combat_surface(size)
    print("1C")
    city_names = [
        "Morkomasto",
        "Morathrad",
        "Eregailin",
        "Corathrad",
        "Eregarta",
        "Numensari",
        "Rhunkadi",
        "Londathrad",
        "Baernlad",
        "Forthyr",
    ]

    city_locations = get_randomly_spread_cities(size, len(city_names))
    print("1CL")
    routes = get_routes(city_locations)
    print("1R")
    random.shuffle(routes)
    routes = routes[:10]
    print("1RS")
    player_sprite = Sprite(sprite_path, city_locations[start_city])
    print("1PS")
    player = PyGameAIPlayer()
    #player = PyGameHumanPlayer()
    print("1PO")
    """ Add a line below that will reset the player variable to 
    a new object of PyGameAIPlayer class."""

    state = State(
        current_city=start_city,
        destination_city=start_city,
        travelling=False,
        encounter_event=False,
        cities=city_locations,
        routes=routes,
    )

    #cost = 0
    #health = 100
    bool = False
    while True:
        print("1W")
        action = player.selectAction()
        if 0 <= int(chr(action)) <= 9:
        # if 0 <= state.current_city <= 9:
            print("1IF")
            if int(chr(action)) != state.current_city and not state.travelling:
                print("olalala")
                ''' 
                Check if a route exist between the current city and the destination city.
                '''
                for route in routes:
                    if route[0] == city_locations[state.current_city] and route[1] == city_locations[int(chr(action))]:
                        bool = True
                        print("1FOR")
                        break
                
                if bool == True:
                    print("1IF2")
                    start = city_locations[state.current_city]
                    state.destination_city = int(chr(action))
                    destination = city_locations[state.destination_city]
                    player_sprite.set_location(city_locations[state.current_city])
                    state.travelling = True
                    print(
                        "Travelling from", state.current_city, "to", state.destination_city
                    )
                    #journal.generate_journal_entry(state)
                    route_coordinate = start, destination
                    player.money -= get_route_cost(city_locations, state.current_city, state.destination_city, elevation)
                    player.health -= 5
                else:
                    print("No route from the current city to destination")

        screen.fill(black)
        screen.blit(landscape_surface, (0, 0))

        for city in city_locations:
            pygame.draw.circle(screen, (255, 0, 0), city, 5)

        for line in routes:
            pygame.draw.line(screen, (255, 0, 0), *line)

        displayCityNames(city_locations, city_names)
        if state.travelling:
            print("1ST")
            state.travelling = player_sprite.move_sprite(destination, sprite_speed)
            state.encounter_event = random.randint(0, 1000) < 2
            if not state.travelling:
                print("1NST")
                print('Arrived at', state.destination_city)
                print("Money: ", player.money)
                print("Health: ", player.health)

        if not state.travelling:
            print("1NST2")
            encounter_event = False
            state.current_city = state.destination_city

        if state.encounter_event:
            print("1SEE")
            # episode = run_episode(player, opponent)
            # print(episode)
            # win = run_pygame_combat(combat_surface, screen, player_sprite)
            # player.money += win * 10
            # player.health += 5
            # state.encounter_event = False
            run_pygame_combat(combat_surface, screen, player_sprite)
            state.encounter_event = False
        else:
            player_sprite.draw_sprite(screen)
        pygame.display.update()
        if state.current_city == end_city:
            print("1SCC")
            print('You have reached the end of the game!')
            print("You won! You have ", player.money, "with ", player.health, "health.")
            break
        if player.money < 0 or player.health == 0:
            print("Game Over. You lost")
            break
