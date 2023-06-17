import argparse
from scraper import Scraper


def main(url: str, max_url: int, depth: int = 0, filter_duplicate_urls: bool = False, **kwargs):
    """
    This is the main function.
    You can see the full documentation if the README.md file.
    Example:
    >> python3.9 main.py --url http://example.com --max_url 5 --depth 5 --unique
    :param url: the URL
    :param max_url: the maximum URLs you want to get from a scrape
    :param depth: the depth you want the Scraper to get
    :param filter_duplicate_urls: a flag if you want to save the same URL even you already scan it
    TODO: filter based on some Hash function instead name checking
    :param kwargs: filter_duplicate_urls_same_html. if the user wants to filter the URLs inside HTML
    """
    # Checks and reformat user input
    if depth not in [0, 1, 2]:
        raise Exception("The supported Depth is 0, 1 and 2 only. Read the README.md for more information")
    if depth == 2:  # When the user inputs 2 - they mean 5. By the requirements.
        depth = 5

    if url.endswith('/'):  # It's the same address
        url = url[:-1]

    # Logic
    scraper_object = Scraper(depth=depth, filter_duplicate_urls=filter_duplicate_urls)
    scraper_object.process_url(url, max_url=max_url, current_depth=0, **kwargs)


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="Web Crawler")
        parser.add_argument("--url", required=True, help="The URL to start the scraping process")
        parser.add_argument("--max_url", type=int, required=True,
                            help="The maximal amount of URLs to extract from each page")
        parser.add_argument("--depth", type=int, required=True, help="The depth factor")
        parser.add_argument("--unique", action="store_true", help="Filter out duplicate URLs")

        args = parser.parse_args()
        main(args.url, args.max_url, args.depth, args.unique)
    except ValueError as e:
        print(f"Error: Invalid argument value.\n{e}")
        print("Usage:\npython3.9 main.py --url <insert url here> --max_url <number of the maximum url> --depth <number "
              "for the search depth. 0 if not specified> --unique <if not specified False, if specified - True>")
    except Exception as e:
        print(f"Error: An error occurred: {e}")
