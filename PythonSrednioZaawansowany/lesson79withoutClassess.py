cake1={
    "taste": 'vanilia',
    "glaze": 'chocolade',
    "text": 'Happy Brithday',
    "weight": 0.7}

cake2={
    "taste": 'tee',
    "glaze": 'lemon',
    "text": 'Happy Python Coding',
    "weight": 1.3}


def show_cake_info(cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(cake['taste'], cake['glaze'], cake['text'], cake['weight']))


print(show_cake_info(cake2))


cakes=[cake1,cake2]
for cake in cakes:
    show_cake_info(cake)


#show_cake_info(cake_01_taste, cake_01_glaze, cake_01_text, cake_01_weight)
#show_cake_info(cake_02_taste, cake_02_glaze, cake_02_text, cake_02_weight)

