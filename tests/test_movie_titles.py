
import pytest

from movie_titles_to_s3 import get_titles


@pytest.mark.parametrize(
    "url, num_movies",
    [
        ("https://www.flickchart.com/Charts.aspx?genre=Cyberpunk+%2f+Tech+Noir&perpage=50", 50),
        ("https://www.flickchart.com/Charts.aspx?genre=Cyberpunk+%2f+Tech+Noir&perpage=100", 100),
        ("https://www.flickchart.com/Charts.aspx?genre=Cyberpunk+%2f+Tech+Noir&perpage=150", 150),
    ]
)
def test_movie_title(url, num_movies):
    """Test scraping movie titles from web url"""

    titles = get_titles(url=url)

    assert isinstance(titles, list)
    assert all([type(title) == list for title in titles])
    assert len(titles) == num_movies
