from tqdm import tqdm
from time import sleep

MAX_ITER = 3

# 1. Using default bar_format

with tqdm(total=100, desc = 'Increasing sleep') as pbar:
    for i in range(MAX_ITER):
        sleep(i + 0.2)
        pbar.update(100/MAX_ITER)

# 2. Customising the bar_format to remove {remaining} and add whitespaces around the {bar}

with tqdm(total=100, desc = 'Increasing sleep',
          bar_format='{desc}: {percentage:3.0f}% | {bar} | {n_fmt}/{total_fmt} [{elapsed}, {rate_fmt}{postfix}]') as pbar:
    for i in range(MAX_ITER):
        sleep(i + 0.2)
        pbar.update(100/MAX_ITER)

# 3. Customising the bar_format to add the current/total in the postfix
# Note that a ", " is automatically added before {postfix}

with tqdm(total=100, desc='Increasing sleep',
          bar_format='{desc}: {percentage:3.0f}% | {bar} | [{elapsed}, {rate_fmt}{postfix}]') as pbar:
    for i in range(MAX_ITER):
        sleep(i + 0.2)
        pbar.update(100/MAX_ITER)

        # Get the current progress and set the formatted current progress with 2 decimals in the postfix
        current = pbar.n
        pbar.set_postfix_str(f'{current:.2f}/{pbar.total}')