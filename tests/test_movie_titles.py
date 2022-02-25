"""
import pytest

from titles_to_s3 import get_titles


@pytest.mark.parametrize(
    "url, num_movies",
    [
        ("https://www.flickchart.com/Charts.aspx?genre=Cyberpunk+%2f+Tech+Noir&perpage=50", 50),
        ("https://www.flickchart.com/Charts.aspx?genre=Cyberpunk+%2f+Tech+Noir&perpage=100", 100),
        ("https://www.flickchart.com/Charts.aspx?genre=Cyberpunk+%2f+Tech+Noir&perpage=150", 150),
        ("https://www.flickchart.com/Charts.aspx?genre=Cyberpunk+%2f+Tech+Noir&perpage=200", 200)
    ]
)
def test_movie_title(url, num_movies):
    "Test scraping movie titles from web url"

    titles = get_titles(url=url)

    assert isinstance(titles, list)
    assert len(titles) == num_movies

    for title in titles:
        assert isinstance(title, str)

    with pytest.raises(ValueError):
        titles = get_titles(url='nonexisting')
"""

def test_movie_title():

    titles = get_titles(url="https://www.flickchart.com/Charts.aspx?genre=Cyberpunk+%2f+Tech+Noir&perpage=50")
    print(len(titles))
    assert isinstance(titles, list)
    assert len(titles) == 50

    for title in titles:
        assert isinstance(title, str)

    with pytest.raises(ValueError):
        titles = get_titles(url='nonexisting')