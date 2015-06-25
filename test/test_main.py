from source.game import Game


def test_build():
    assert True


def test_game():
    x = Game(1)
    if x.screen is not None:
        assert True
    else:
        assert False
