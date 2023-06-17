import os.path
import re
import requests

from utils import create_directory


class URL:
    """
    This class represents URL with methods directly connected to URL - getting HTML content and using its data (saving
    and extracting data).
    """
    BASE_DIRECTORY = "saved_html"
    create_directory(BASE_DIRECTORY)

    def __init__(self, url_address: str):
        self.url_address = url_address  # TODO: we can add an option to get the "real" URL if necessary.
        self.html_content = None
        self.urls = None

    def get_html_content(self):
        """
        This function uses the 'requests' module to obtain the HTML content of the given URL.
        """
        try:
            response = requests.get(url=self.url_address)
            if response.status_code == 200:
                self.html_content = response.text
            else:
                print(f"FAILED: Got response: {response} for URL: {self.url_address}")
        except ConnectionError:
            print(f"Could not connect to the address: {self.url_address}")
        except Exception as e:
            print(f"Exception occurred: {e}")

    def get_all_urls(self, max_url: int, filter_duplicate_urls_same_html: bool = True) -> list:
        """
        This function gets all the URL in html content.
        Some logic: It returns only the amount of URLs asked by the user (by the param: max_url)
                    It returns only the distinct URL from an individual html content (by the param:
            filter_duplicate_urls_same_html)
        :param max_url: The amount of URLs asked by the user
        :param filter_duplicate_urls_same_html: A boolean parameter that indicates if the user want only the distinct
            URLs inside a given html content.
        :return:
        """
        # url_pattern = re.compile(r'href=[\'"]?([^\'" >]+)') || This line finds any link TODO: do you want this one?
        website_pattern = re.compile(r'href=["\'](http[s]?://[^\s"/\\]+\.[^\s"/\\]+)')  # Extracts website links only
        if self.html_content:
            self.urls = re.findall(website_pattern, self.html_content)
            self.urls = self.urls[:max_url]
            if filter_duplicate_urls_same_html:
                no_duplicated_urls = list(set(self.urls))
                self.urls = no_duplicated_urls
            return self.urls
        elif not self.html_content:
            print(f"INFO: We don't extract any URL from {self.url_address} because it was already scan in our systems")
            return []

    def save_html_content(self, filter_duplicate_urls, depth_level):
        """
        This function saves the HTML to a file to an organized File System.
        :param filter_duplicate_urls: filter duplicate URLs
        :param depth_level: the number for cross layer scraping
        """
        # Folder and filename setup
        directory = self.BASE_DIRECTORY + "/" + str(depth_level)
        create_directory(directory)
        filename = self._reformat_url_to_filename()

        occurrence = 1

        if os.path.exists(os.path.join(directory, filename)) and filter_duplicate_urls:
            print(f"INFO: File {filename} already saved.")  # TODO: logging
            return

        while os.path.exists(os.path.join(directory, filename)):
            occurrence += 1
            filename = self._reformat_url_to_filename(occurrence)

        file_path = os.path.join(directory, filename)
        self.get_html_content()
        with open(file_path, 'w') as file:
            file.write(self.html_content if self.html_content else "")
        print(f"SUCCESS: File saved as: {file_path}")  # TODO: logging

    def _reformat_url_to_filename(self, occurrence: int = 1):
        """
        This function reformat the filename considering double URLs (if 'filter_duplicate_urls' False).
        :param occurrence: The number of times the URL was saved
        :return: the URL after reformatting
        """
        url_without_prefix = self.url_address.replace("http://", "").replace("https://", "")
        sanitized_url = url_without_prefix.replace("/", "_").replace(".", "_")

        if occurrence > 1:
            sanitized_url = sanitized_url + "_" + str(occurrence)
        sanitized_url += ".html"
        return sanitized_url
