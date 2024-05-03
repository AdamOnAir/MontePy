import random

def estimate_pi(num_points):
  """
  Estime la valeur de pi en utilisant la méthode de Monte-Carlo.

  Args:
      num_points: Le nombre de points aléatoires à générer.

  Returns:
      Une estimation de la valeur de pi.
  """
  circle_points = 0
  total_points = 0

  for _ in range(num_points):
    x = random.random()
    y = random.random()

    # Vérifier si le point est à l'intérieur du cercle
    if (x**2 + y**2) <= 1:
      circle_points += 1
    total_points += 1

  # Estimer pi
  pi_estimation = (circle_points / total_points) * 4

  return pi_estimation

# Exemple d'utilisation
num_points = int(input("Nombre de points ..."))
pi_estimate = estimate_pi(num_points)

print(f"Estimation de pi avec {num_points} points: {pi_estimate}")
