#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, time

# def files_in_one_minute(folder, lists):
# def files_in_a_period_of_time(folder, lists, seconds):
def files_in_a_period_of_time(folder, seconds):
    lists = os.listdir(folder)
    ret = []
    print('folder', folder)
    print()
    print('lists', lists)
    print()
    for f in lists:
        st = os.stat(folder + "/" + f)
        mtime = st.st_mtime
        # if time.time() - mtime < 60:
        # if time.time() - mtime < 3600 * 24:
        if time.time() - mtime < seconds:
            f = folder + "/" + f
            # f = os.path.join(folder, f)
            ret.append(f)
    return ret

# https://docs.python.org/3/library/os.html#os.stat
# >>> import os
# >>> statinfo = os.stat('somefile.txt')
# >>> statinfo
# os.stat_result(st_mode=33188, st_ino=7876932, st_dev=234881026,
# st_nlink=1, st_uid=501, st_gid=501, st_size=264, st_atime=1297230295,
# st_mtime=1297230027, st_ctime=1297230027)
# >>> statinfo.st_size
# 264   

# https://docs.python.org/3/library/time.html#time.time
# time.time()
# Return the time in seconds since the epoch as a floating point number.    
    
def main():
    result_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir, "reports", "example_suite")
    print(result_dir)
    result_dir = result_dir.replace('\\', '/')
    print(result_dir)
    # lists = os.listdir(result_dir)
    # files = files_in_one_minute(result_dir, lists)
    # files = files_in_a_period_of_time(result_dir, lists, 3600 * 12)
    files = files_in_a_period_of_time(result_dir, 3600 * 12)
    print()
    print('files', files)

if __name__ == '__main__':
    main()
