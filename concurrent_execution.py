import concurrent.futures
import sys
import time

NUMBER_OF_FILES = 4

def create_file(path, name):
    time.sleep(1)
    print(f'Creating file {name}')
    path = f'{path}/{name}.txt'
    with open(path, 'w', encoding='utf-8') as output:
        output.write('Ola, mundo!')
        time.sleep(2)
        print(f'Done file {name}')
        return path

def create_files_sequentially(path):
    for i in range(0, NUMBER_OF_FILES):
        create_file(path, i)

def create_files_concurrently(path):
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        future_download = {executor.submit(create_file, path, i): i
                           for i in range(0, NUMBER_OF_FILES)}
        for future in concurrent.futures.as_completed(future_download):
            print(f'Completed {future_download[future]} -> {future.result()}')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == '-c':
            create_files_concurrently('/tmp')
        elif sys.argv[1] == '-s':
            create_files_sequentially('/tmp')
