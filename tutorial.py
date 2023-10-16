users = [
    'aya-yasmine',
    'Anna',
    'velocitatem',
    'laura',
    'torkuno',
    'isabel',
    'zaid',
    'restartdk'
]

def greet(user):
    print(f'Hello {user}!')


if __name__ == "__main__":
    [greet(user) for user in users]
