import os


def clear_files() -> str:
    folder = 'uploads'
    files = os.listdir(folder)
    for file in files:
        os.system(f'rm {folder}/{file}')
    return '<h1>Server files cleared</h1>'
