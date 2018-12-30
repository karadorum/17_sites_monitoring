import requests
import whois
import argparse
import datetime


def console_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Enter a path of file with urls')
    arg = parser.parse_args()
    return arg


def load_urls4check(path):
    with open(path, 'r', encoding='utf-8') as file:
        urls_list = [url.replace('\n', '') for url in file]
    return urls_list


def is_server_respond_with_200(url):
    response = requests.get(url)
    if response.ok:
        return ('OK')
    else:
        return response.status_code


def check_expiration_date(url):
    whois_response = whois.whois(url)
    first_exp_index = 0
    exp_date = whois_response['expiration_date'][first_exp_index]
    tz = exp_date.tzinfo
    now = datetime.datetime.now(tz=tz)
    max_exp_time = datetime.timedelta(days=30)
    days_before_exp = exp_date - now
    if days_before_exp > max_exp_time:
        return 'more than 30'
    else:
        return days_before_exp.days


if __name__ == '__main__':
    arguments = console_args()
    urls_file_path = arguments.path
    urls_list = load_urls4check(urls_file_path)
    for url in urls_list:
        url_status = is_server_respond_with_200(url)
        exp_status = check_expiration_date(url)
        print(url, 'status: {},
              days before expiration: {}'.format(url_status, exp_status))
