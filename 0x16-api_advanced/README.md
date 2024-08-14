Reddit API Project

 0x16-api_advanced ALX project

Overview
This project involves querying the Reddit API to perform various tasks related to retrieving and processing subreddit data. The objectives include handling API requests, parsing JSON data, managing pagination, and recursively processing data. Functions are implemented to get subscriber counts, retrieve hot post titles, and count keyword occurrences.

Objectives
Reading API Documentation: Understanding how to navigate and utilize Reddit API documentation.
Handling Pagination: Using recursion to handle pagination in API responses.
Parsing JSON Results: Extracting and processing nested JSON data returned by the API.
Recursive API Calls: Implementing recursive functions to handle API requests and process data.
Sorting and Counting: Counting keyword occurrences and sorting the results by count and keyword.
Functions
0. number_of_subscribers(subreddit)
Queries the Reddit API to return the number of subscribers for a given subreddit.

Prototype:

python
Copy code
def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to return the number of subscribers for the given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
    
    Returns:
        int: Number of subscribers or 0 if the subreddit is invalid.
    """
Objective Addressed: Handling basic API requests and parsing the response.

1. top_ten(subreddit)
Prints the titles of the first 10 hot posts listed for a given subreddit.

Prototype:

python
Copy code
def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for the given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
    
    Returns:
        None: Prints the titles or None if the subreddit is invalid.
    """
Objective Addressed: Parsing JSON results and handling API requests.
2. recurse(subreddit, hot_list=[])
Recursively queries the Reddit API to get a list of all hot articles for a given subreddit.

Prototype:

python
Copy code
def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API to retrieve a list of all hot articles for the given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to accumulate the titles of hot articles.
    
    Returns:
        list: A list of titles of all hot articles or None if the subreddit is invalid.
    """
Objective Addressed: Using recursion to handle pagination and accumulate data.
3. count_words(subreddit, word_list)
Recursively queries the Reddit API to count the occurrences of specified keywords in hot post titles and prints the results.

Prototype:

python
Copy code
def count_words(subreddit, word_list):
    """
    Recursively queries the Reddit API to count keyword occurrences in hot articles for the given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
    
    Returns:
        None: Prints sorted counts of each keyword.
    """
Objective Addressed: Counting keyword occurrences and sorting the results.
Detailed Objectives

1. Reading API Documentation
Understanding the Reddit API documentation is crucial for knowing how to format requests and what data is available. This includes understanding endpoints, query parameters, and response formats.

2. Handling Pagination
Reddit's API uses pagination to manage large sets of data. Recursive functions are used to handle pagination, fetching and processing data from multiple pages until all data is retrieved.

3. Parsing JSON Results
API responses are typically in JSON format. Parsing involves extracting relevant data from nested JSON objects to be used in the application.

4. Recursive API Calls
Recursive functions are used to handle pagination and collect data from multiple pages. This approach ensures that all relevant data is gathered by making additional API requests as needed.

5. Sorting and Counting
After collecting data, the function sorts keyword occurrences by count and alphabetically if counts are the same. This provides a clear and organized output of keyword frequencies.

Requirements
Python 3
requests library (install with pip install requests)
