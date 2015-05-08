from source.game import game


def test_build():
    assert True

def test_game():
    x = game()
    if x.screen!=None:
        assert True
    else:
        assert False
