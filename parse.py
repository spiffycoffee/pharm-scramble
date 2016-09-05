import json
import datetime, time
import os
from sys import exit


def print_intro(first_time=False):
    print '======================================='
    print '   PhorCAS Residency Scramble Checker'
    print '======================================='

    if first_time:
        current_time = time.ctime(time.time()) 
        print 'First checkin @ ' + current_time + '\n' 
    else:
        file_timestamp = time.ctime(os.path.getmtime('previous.json'))
        print 'Last checked @ ' + file_timestamp + '\n'


def print_programs(header, programs):
    print header
    if programs == []:
        print 'none'
    for s in programs:
        print s['school_name'] + ' in ' + s['city'] + ', ' + s['state'] \
                + ' - ' + s['hard_deadline'] + '' 
    print ''


def list_open_programs():
    input_exists = os.path.isfile('input.json')
    if not input_exists: 
        print 'Run the PhorCAS Update Checker by typing: ./grab_data.sh'
        exit() 

    with open('input.json') as data_file:
        data = json.load(data_file)
    return [s for s in data['schools'] if s['expired'] == '0']


def list_prev_programs():
    with open('previous.json') as prev_file:
        prev = json.load(prev_file)
    return [s for s in prev['schools']]


def write_open_programs(open_programs):
    with open('previous.json', 'w') as save_file:
        json.dump({'schools': open_programs}, save_file)


def main():
    open_programs = list_open_programs()

    prev_run_exists = os.path.isfile('previous.json')
    if prev_run_exists: 

        # Make dict to simplify matching new and old 
        prev_open_programs = {s['id']: s for s in list_prev_programs()}

        print_list = {'new': [], 'closed': [], 'same': []}
        for program in open_programs: 
            if program['id'] not in prev_open_programs:
                print_list['new'].append(program)
            else:
                print_list['same'].append(program)
                # Cancel out programs that match on both lists 
                del prev_open_programs[program['id']]
        # Not cancelled out programs must have closed
        print_list['closed'] = prev_open_programs.values()

        print_intro()
        print_programs('New programs:', print_list['new'])
        print_programs('Closed programs:', print_list['closed'])
        print_programs('Still Open programs:', print_list['same'])

    else: 
        print_intro(first_time=True)
        print_programs('Open programs:', open_programs)

    write_open_programs(open_programs)


if __name__ == "__main__":
    main()
