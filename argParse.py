import argparse

parser = argparse.ArgumentParser(description='Scrape jobs (legally) from Himalayas.app')
parser.add_argument('-s', '--skill', type=str, default='software engineer',
                    help='Input specific job or skill. Default: software engineer')
parser.add_argument('-l', '--location', type=str, default='United States',
                    help='Input specific location. Default: United States')
parser.add_argument('-e', '--experience', type=str,
                    choices=['entry-level', 'mid-level', 'senior-level'],
                    default='entry-level',
                    help='Specify experience level (entry-level, mid-level, senior-level)')

args = parser.parse_args()