import random
import art
import game_data

print(art.logo)

option_a = random.choice(game_data.data)
option_a_followers = option_a['follower_count']

print(f"Compare A: {option_a['name']}, {option_a['description']}, {option_a['country']}")

print(option_a_followers)