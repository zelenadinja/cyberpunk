
import pytest
<<<<<<< HEAD

from titles_to_s3 import get_titles
=======
from movie_titles_to_s3 import get_titles
>>>>>>> 9613a4329bd82624e96f6fa780a22020f2383521


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
    """Test scraping movie titles from web url"""

    titles = get_titles(url=url)

    assert isinstance(titles, list)
    assert len(titles) == num_movies

    for title in titles:
        assert isinstance(title, str)

    with pytest.raises(ValueError):
        titles = get_titles(url='nonexisting')
