import unittest
import requests


class TestExchangeRatesAPI(unittest.TestCase):
    # creating test method 'test_fetch_exchange_rates' which checks if API response is a valid JSON and if HTTP status is 200 (OK):
    def test_fetch_exchange_rates(self):
        # calling function which makes request to API:
        response = requests.get('http://api.nbp.pl/api/exchangerates/tables/a/?format=json')

        # checking if HTTP status is 200:
        self.assertEqual(response.status_code, 200)

        # checking if response got valid JSON:
        try:
            rates = response.json()[0]['rates']  # formatting response to JSON
            # checking if response contains rates list:
            self.assertTrue(isinstance(rates, list))
            # checking if every rate contains key fields:
            for rate in rates:
                self.assertIn('currency', rate)
                self.assertIn('code', rate)
                self.assertIn('mid', rate)
        except ValueError:
            # giving error for test if response is not valid JSON
            self.fail("Response is not a valid JSON")


# condition that checks whether the script was run directly and not imported as a module, if so then function 'unittest.main()' runs every test method defined in the class:
if __name__ == '__main__':
    unittest.main()


# Expected result when True in terminal:
# ----------------------------------------------------------------------
# Ran 1 tests in 0.067s
#
# OK
