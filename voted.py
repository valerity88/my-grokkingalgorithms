voted = {}
def check_voter(name):
    if voted.get(name):
        print("Выгнать их!")
    else:
        voted[name] = True
        print("Пусть проголосуют!")
