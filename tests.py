from load_balancer import load_balancer


def test_load_balancer():
    config = {
        'one': {
            'dj': 5,
            'fl': 7,
        },
        'two': {
            'spr': 2,
            'ee': 8,
        },
        'three': {
            'ror': 7,
        },
    }

    load_balancer(config, 'elixir', 10)
    assert config == {
        'one': {
            'dj': 5,
            'elixir': 1,
            'fl': 7,
        },
        'two': {
            "ee": 8,
            "elixir": 3,
            "spr": 2,
        },
        'three': {
            "elixir": 6,
            "ror": 7,
        },
    }


def test_sum():

    config = {
        'one': {},
        'two': {},
        'thee': {},
    }

    load_balancer(config, 'guava', 7)
    load_balancer(config, 'gunicorn', 8)
    load_balancer(config, 'rust', 15)

    assert sum(sum(service.values()) for service in config.values()) == 30