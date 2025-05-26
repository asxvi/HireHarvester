import argparse
# from urllib.parse import 

def parse_args():
    parser = argparse.ArgumentParser(description='Scrape jobs (legally) from Himalayas.app')
    parser.add_argument('-r', '--role', type=str, 
                        # default='software engineer',
                        help='Input specific role or skill. Default: software engineer')
    parser.add_argument('-l', '--location', type=str, 
                        default='United States',
                        help='Input specific location. Default: United States')
    parser.add_argument('-e', '--experience', type=str,
                        # choices=['entry-level', 'mid-level', 'senior', 'manager', 'director'],
                        # default='entry-level',
                        help='Specify experience level. Default: entry-level')
    parser.add_argument('-t', '--type', type=str,
                        # choices=['full-time', 'part-time', 'intern', 'contractor', 'volunteer', 'other', 'temporary'],
                        # default='full-time',
                        help='Specify job type level. Default: full time')
    parser.add_argument('-p',  '--pages', type=int, default=1, help="Max number of pages to scrape. Default: 1 page")
    return parser.parse_args()


def slugify(text): # called slugify apparently
    return text.strip().lower().replace(',', '%2C').replace(' ', '-') #add separator for mutiple selection e.g entry-level mid-level
    # rv = text.strip().lower().replace(' ', '-') 
    # return rv.replace(',', '%2C')   #add separator for mutiple selection e.g entry-level mid-level

def construct_url(role: str = None, location: str = None, experience: str = None, type: str = None, pages: int = None):
    base_url = 'https://himalayas.app/jobs' # as of 5/23/25
    path = base_url

    if location:
        path += f"/countries/{slugify(location)}"
    if role:
        path += f"/{slugify(role)}?"
    if experience:
        path += f"experience={slugify(experience)}"
    if type:
        path += f"&type={slugify(type)}"
    print(path)
    return path