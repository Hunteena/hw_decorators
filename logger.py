from datetime import datetime
import requests

def logger(old_function):
    def new_function(*args, **kwargs):
        with open('log.txt', 'w') as log:
            call_time = datetime.now().isoformat(sep=' ', timespec='seconds')
            result = old_function(*args, **kwargs)
            log.write(f"{call_time}\n")
            log.write(f"{old_function.__name__}\n")
            log.write(f"{args}, {kwargs}\n")
            log.write(f"{result}\n")
        return result
    return new_function

@logger
def most_intelligent_superhero(names):
    token = '2619421814940190'
    intelligences = []
    for name in names:
        url = f'https://superheroapi.com/api/{token}/search/{name}'
        response = requests.get(url=url)
        hero_intelligence = \
            response.json()['results'][0]['powerstats']['intelligence']
        intelligences.append(int(hero_intelligence))
    most_intelligent = names[intelligences.index(max(intelligences))]
    return most_intelligent
    pass

if __name__ == '__main__':
    superheroes = ['Hulk', 'Captain America', 'Thanos']
    print(
        f'The most intelligent superhero is',
        f'{most_intelligent_superhero(superheroes)}.'
    )
