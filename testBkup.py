import os 

desktop_path_for_checking = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
notice_file_path_for_checking = os.path.join(desktop_path_for_checking, 'saferBkup.notice')

if os.path.exists(notice_file_path_for_checking):
    print('Exiting program as saferBkup.notice file exists on desktop')
    exit()
