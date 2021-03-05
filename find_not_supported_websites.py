import csv
import regex
from pprint import pprint
from urllib.parse import urlparse

csv_file_name = 'log-events-viewer-result.csv'

hosts = {}
with open(csv_file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            foundUrls = regex.findall(r'(https?://[^\s]+)', row[1])
            for url in foundUrls:
                parsed_uri = urlparse(url)
                host = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
                if host in hosts:
                    hosts[host] += 1
                else:
                    hosts[host] = 1
            line_count += 1

sortedUrls = list((sorted(hosts.items(), key=lambda item: item[1], reverse=True)))
pprint(sortedUrls)
