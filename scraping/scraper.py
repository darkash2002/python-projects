from url import URL


class Scraper:
    """
    This class represents Scraper (A process design to search the web given URL and other relevant arguments).
    """
    def __init__(self, depth: int = 0, filter_duplicate_urls: bool = True):
        self.depth = depth
        self.filter_duplicate_urls = filter_duplicate_urls
        self.urls = []

    def process_url(self, url_address: str, max_url: int, current_depth: int, **kwargs):
        """
        Processes a URL by scraping its content, saving it, and recursively processing its child URLs.

        :param url_address: the URL to process
        :param max_url: the maximum number of URLs to retrieve from each page
        :param current_depth: the current depth level in the recursive process
        **kwargs: additional keyword arguments
        """
        if current_depth > self.depth:
            return

        url_object = URL(url_address=url_address)

        url_object.save_html_content(self.filter_duplicate_urls, depth_level=current_depth)
        urls = url_object.get_all_urls(max_url=max_url, **kwargs)
        if urls:
            for u in urls:
                if u not in self.urls:
                    self.urls.append(u)
                    if current_depth < self.depth:
                        self.process_url(url_address=u, max_url=max_url, current_depth=current_depth + 1, **kwargs)
