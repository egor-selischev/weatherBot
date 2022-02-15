import unittest

class TgBotTests(unittest.TestCase):

    def test_get_location(self):
        from main import get_location
        self.assertIsNotNone(get_location('88', '77'))

    def test_owm_token_is_exists(self):
        import config
        self.assertIsNotNone(config.TOKEN)

    def test_get_weather(self):
        with self.assertRaises(Exception):
           from main import get_weather
           get_weather("вв")

if __name__ == "__main__":
    unittest.main()
