import requests
import whois
import datetime
import argparse


def load_urls4check(path):
    try:
        with open(path) as file:
            for url in file.readlines():
                yield url.strip()
    except FileNotFoundError:
        print('File "{0}" is not found.'.format(path))


def is_server_respond_with_200(url):
    status_code = requests.get(url).status_code
    return True if status_code == 200 else False


def get_domain_expiration_date(domain_name):
    whois_domain = whois.whois(domain_name)
    expiration_date = whois_domain.expiration_date
    return expiration_date.date()


def is_domain_expiration_date_valid(expiration_date):
    days_count = 30
    today = datetime.date.today()
    month = datetime.timedelta(days=days_count)
    month_ahead = today + month
    return True if expiration_date >= month_ahead else False


def get_input_data():
    parser = argparse.ArgumentParser(description='Script for sites monitoring')
    parser.add_argument('url_file', help='Text file with URL addresses for check')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_input_data()

    urls = list(load_urls4check(args.url_file))

    for num, url in enumerate(urls):
        expiration_date = get_domain_expiration_date(url)
        print(
            '{0} URL: {1}; STATUS 200: {2}; EXPIRATION DATE: {3} (VALID: {4})'.format(
                num + 1,
                url,
                'OK' if is_server_respond_with_200(url) else 'NO',
                expiration_date,
                'OK' if is_domain_expiration_date_valid(expiration_date) else 'NO',
            )
        )
