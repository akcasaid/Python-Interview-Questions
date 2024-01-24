import random

'''

Monty Hall problemi için yapılan simülasyon 10,000 deneme ile gerçekleştirildi ve sonuçlar şöyle:

Kapıyı değiştirdiğinizde kazanma olasılığı: yaklaşık %66.79
Kapıyı değiştirmediğinizde kazanma olasılığı: yaklaşık %33.21
'''


def monty_hall_sim(num_trials):
    switch_wins = 0
    stay_wins = 0
    
    for _ in range(num_trials):
        # 0, 1, ve 2 numaralı kapılar arasında rastgele bir kapıyı ödülün arkasına yerleştir
        prize_door = random.randint(0, 2)
        # Yarışmacının bir kapı seçimi
        contestant_choice = random.randint(0, 2)
        
        # Yarışmacının seçmediği kapılardan birini aç
        # Açılan kapının arkasında ödül olmamalı ve yarışmacının seçimi de olmamalı
        remaining_doors = [door for door in range(3) if door != contestant_choice and door != prize_door]
        door_opened = random.choice(remaining_doors)
        
        # Eğer yarışmacı kapı değiştirirse
        switch_choice = 3 - contestant_choice - door_opened
        if switch_choice == prize_door:
            switch_wins += 1
        elif contestant_choice == prize_door:
            stay_wins += 1
    
    return switch_wins / num_trials, stay_wins / num_trials

# Simülasyonu 10000 deneme ile çalıştır
switch_win_prob, stay_win_prob = monty_hall_sim(10000)

switch_win_prob, stay_win_prob

