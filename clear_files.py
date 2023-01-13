import os


def clear_files() -> str:
    folder = 'uploads'
    files = os.listdir(folder)
    for file in files:
        os.remove(f'{folder}/{file}')
    return '<h1>Server files cleared</h1>'
