from source.Game import Game


def test_build():
    assert True


def test_game():
    x = Game()
    if x.screen is not None:
        assert True
    else:
        assert False
