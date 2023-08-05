"""Dynadot client."""

import inspect

import lxml.etree
import requests


class TokenError(Exception):
    """Bad Dynadot auth token."""


class Client:
    """Interface the Dynadot service."""

    endpoint = "https://api.dynadot.com/api3.xml"

    def __init__(self, key):
        """Return a Dynadot client."""
        self.key = key

    def list_domain(self):
        """List currently registered domains."""
        response = self._request()
        domains = []
        for domain in response.cssselect("DomainInfo"):
            name = domain.cssselect("Name")[0].text
            expiration = domain.cssselect("Expiration")[0].text
            domains.append((name, expiration))
        return domains

    def search(self, *domains):
        """Search for available of domains."""
        domain_params = {
            "domain{}".format(n): domain for n, domain in enumerate(domains)
        }
        response = self._request(show_price="1", **domain_params)
        results = {}
        for result in response:
            # if len(result[0]) == 5:
            # data = {"price": result[0][4].text}
            # results[result[0][1].text] = data
            available = False if result[0].find("Available").text == "no" else True
            price = result[0].find("Price")
            if price is None:
                price = 0
            else:
                if " in USD" in price.text:
                    price = float(price.text.partition(" ")[0])
                else:
                    price = "?"
            results[result[0].find("DomainName").text] = (available, price)
        return results

    def register(self, domain, duration=1):
        """Register domain."""
        return self._request(domain=domain, duration=duration)

    def account_info(self):
        """Return account information."""
        return self._request()[1][0]

    def set_dns2(self, domain, record_type, record):
        """Set DNS record for given domain."""
        return self._request(
            domain=domain, main_record_type0=record_type, main_record0=record
        )

    def _request(self, **payload):
        """Send an API request."""
        payload.update(command=inspect.stack()[1].function, key=self.key)
        response = requests.get(self.endpoint, params=payload)
        message = lxml.etree.fromstring(response.text)
        try:
            if message.cssselect("ResponseCode")[0].text == "-1":
                raise TokenError()
        except IndexError:
            pass
        return message
