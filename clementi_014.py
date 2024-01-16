import math

for raggio in range(1, 21):
    circonferenza = 2 * math.pi * raggio
    area = math.pi * (raggio ** 2)
    print(f"Raggio: {raggio} - Circonferenza: {circonferenza} - Area: {area}")