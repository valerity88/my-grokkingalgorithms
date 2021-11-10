def countdown(i):
        print(i)
        # Базовый случай
        if i <= 0:
                return 0
        # Рекурсивный случай
        else:
                countdown(i-1)
countdown(5)
