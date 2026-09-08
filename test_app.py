from app import recommend_book


def test_book_recommendation():
    result = recommend_book("stressed", "motivational")
    assert result == "The Alchemist"
