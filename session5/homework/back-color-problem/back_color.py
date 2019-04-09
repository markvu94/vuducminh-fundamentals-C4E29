from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    import random
    text = random.choice(["RED","BLUE","YELLOW","GREEN"])
    color = random.choice(["#3F51B5","#C62828","#FFD600","#4CAF50"])
    quiz_type = 1

    return [
                text,
                color,
                quiz_type # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    loop = False
    if quiz_type == 0:
        for item in shapes:
            if item["text"] == text.lower() and item["rect"][0] <= x <= (item["rect"][0] + item["rect"][2]) and item["rect"][1] <= y <= (item["rect"][1] + item["rect"][3]):
                loop = True
            
    if quiz_type == 1:
        for item in shapes:
            if item["color"] == color and item["rect"][0] <= x <= (item["rect"][0] + item["rect"][2]) and item["rect"][1] <= y <= (item["rect"][1] + item["rect"][3]):
                loop = True
    
    return loop
    

    
