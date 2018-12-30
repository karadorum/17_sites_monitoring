# Sites Monitoring Utility

This script gets urls from a text file and returns an information about every given url: response status and message if a domain name is going to expire within a month.

The path of text file containing urls is the positional argument of the script.

To run script on Linux:
`

$ python check_sites_health.py sites.txt
http://google.com status: OK, days before expiration: more than 30
`

Windows usage is the same.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
