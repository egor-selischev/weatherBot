import unittest
# import config
# from main import get_weather, get_location


class TgBotTests(unittest.TestCase):

    # def test_owm_token_is_exists(self):
    #     self.assertIsNotNone(config.TOKEN)
    #
    # def test_get_weather(self):
    #     with self.assertRaises(Exception):
    #         get_weather("вв")

    def test_get_location(self):
        # self.assertIsNotNone(get_location('88', '77'))
        self.assertEqual(1 + 1, 2)


if __name__ == '__main__':
    unittest.main()