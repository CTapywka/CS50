def main():
    while True:
        fruit = input().strip().lower()
        if norm_frukt(fruit):
            print(callories(fruit))
            # break
        else:
            print('Введите корректное название!')



def norm_frukt(f):
    fruits = [
        'apple', 'avocado', 'banana', 'cantaloupe', 'grapefruit', 'grapes',
    'honeydew', 'kiwifruit', 'lemon', 'lime', 'nectarine', 'orange', 'peach',
    'pear', 'pineapple', 'plums', 'strawberries', 'sweet cherries', 'tangerine', 'watermelon'
    ]
    if f in fruits:
        return True
    else:
        return False


def callories(fr):
    list_callories = {
        'apple' : 130, 'avocado' : 50, 'banana' : 110, 'cantaloupe' : 50, 'grapefruit' : 60, 'grapes' : 90,
        'honeydew' : 50, 'kiwifruit' : 90, 'lemon' : 15, 'lime' : 20, 'nectarine' : 60, 'orange' : 80, 'peach' : 60,
        'pear' : 100, 'pineapple' : 50, 'plums' : 70, 'strawberries' : 50, 'sweet cherries' : 100, 'tangerine' : 50, 'watermelon' : 80
    }
    return list_callories[fr]


main()