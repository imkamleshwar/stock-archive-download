import time


def update_progress(progress, total_bar_len):
    progress_in_100 = (progress * 100) // total_bar_len
    print('\rProgress: |{0}| {1}% Completed'.format('█' * progress_in_100 + '-' * (100 - progress_in_100),
                                                   progress_in_100), end="")
