import requests
import whois
import datetime
import argparse


def load_urls4check(url_file):
    with url_file:
        for url in url_file.readlines():
            yield url.strip()


def is_server_respond_with_200(url):
    status_code = requests.get(url).status_code
    return status_code == requests.codes.ok


def get_domain_expiration_date(domain_name):
    whois_domain = whois.whois(domain_name)
    expiration_date = whois_domain.expiration_date
    if type(expiration_date) is list:
        return expiration_date[0].date()
    else:
        return expiration_date.date()


def is_domain_expiration_date_valid(expiration_date):
    days_count = 30
    days_count_before_expiration_date = (expiration_date - datetime.datetime.now().date()).days
    return days_count_before_expiration_date > days_count


def get_input_data():
    parser = argparse.ArgumentParser(description='Script for sites monitoring')
    parser.add_argument(
        'url_file',
        type=argparse.FileType(),
        help='Text file with URL addresses for check'
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = get_input_data()

    urls = list(load_urls4check(args.url_file))

    for num, url in enumerate(urls):
        server_status = is_server_respond_with_200(url)
        expiration_date = get_domain_expiration_date(url)
        expiration_date_status = is_domain_expiration_date_valid(expiration_date)

        if server_status and expiration_date_status:
            print('{0} URL: {1}; STATUS: OK'.format(num + 1, url))
        elif not server_status and expiration_date_status:
            print('{0} URL: {1}; STATUS: NO (status 200 error)'.format(num + 1, url))
        elif server_status and not expiration_date_status:
            print(
                '{0} URL: {1}; STATUS: NO (expiration date "{2}" is less, than in a month)'.format(
                    num + 1,
                    url,
                    expiration_date
                )
            )
        elif not server_status and not expiration_date_status:
            print(
                '{0} URL: {1}; STATUS: NO (status 200 error; expiration date "{2}" is less, than in a month)'.format(
                    num + 1,
                    url,
                    expiration_date
                )
            )
