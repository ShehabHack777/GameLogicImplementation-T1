import random

def take_turn(player, enemy, game_state):
  """
  Simulates a turn in a turn-based game.

  Args:
      player (dict): A dictionary containing player stats like attack, defense, health, etc.
      enemy (dict): A dictionary containing enemy stats.
      game_state (dict): A dictionary containing the current game state information (optional).

  Returns:
      dict: A dictionary containing the results of the turn, including player damage dealt,
            enemy damage dealt, updated player and enemy health, and game over status.
  """

  # Calculate player attack damage
  player_attack = player["attack"] + random.randint(0, 5)  # Add some randomness

  # Apply attack modifiers based on game state (optional)
  if game_state and "player_buff" in game_state:
    player_attack *= game_state["player_buff"]

  # Calculate enemy defense against player attack
  enemy_defense = enemy["defense"]

  # Calculate damage dealt to enemy after defense reduction
  enemy_damage_taken = max(0, player_attack - enemy_defense)

  # Update enemy health
  enemy["health"] -= enemy_damage_taken

  # Check if enemy is defeated
  if enemy["health"] <= 0:
    return {
      "player_damage": enemy_damage_taken,
      "enemy_damage": 0,
      "player_health": player["health"],
      "enemy_health": 0,
      "game_over": True
    }

  # Enemy attack logic (similar to player attack)
  enemy_attack = enemy["attack"] + random.randint(0, 5)
  player_defense = player["defense"]
  player_damage_taken = max(0, enemy_attack - player_defense)

  # Apply defense modifiers based on game state (optional)
  if game_state and "enemy_buff" in game_state:
    player_damage_taken *= game_state["enemy_buff"]

  # Update player health
  player["health"] -= player_damage_taken

  # Return turn results
  return {
    "player_damage": enemy_damage_taken,
    "enemy_damage": player_damage_taken,
    "player_health": player["health"],
    "enemy_health": enemy["health"],
    "game_over": False
  }

# Example usage
player = {"attack": 10, "defense": 5, "health": 100}
enemy = {"attack": 8, "defense": 2, "health": 80}
game_state = {}  # No game state modifiers in this example

turn_results = take_turn(player, enemy, game_state)

print(f"Player dealt {turn_results['player_damage']} damage to enemy.")
print(f"Enemy dealt {turn_results['enemy_damage']} damage to player.")
print(f"Player health: {turn_results['player_health']}")
print(f"Enemy health: {turn_results['enemy_health']}")

if turn_results["game_over"]:
  print("Player wins!")
