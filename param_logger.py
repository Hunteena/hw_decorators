from datetime import datetime
import os
import requests


def parametrized_logger(log_path=os.getcwd(), log_filename='log.txt'):
    if not os.path.exists(log_path):
        print(f"Path '{os.path.abspath(log_path)}' does not exist.")
        print(f"Log file will be saved to the current working directory.")
        log_path = os.getcwd()
    log_full_path = os.path.join(log_path, log_filename)

    def logger(old_function):
        def new_function(*args, **kwargs):
            with open(log_full_path, 'w') as log:
                call_time = datetime.now().isoformat(sep=' ',
                                                     timespec='seconds')
                result = old_function(*args, **kwargs)
                log.write(
                    f"{call_time}\n" +
                    f"{old_function.__name__}\n" +
                    f"{args}, {kwargs}\n" +
                    f"{result}"
                )
            return result
        return new_function
    return logger


@parametrized_logger('logs', 'new_log.txt')
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
