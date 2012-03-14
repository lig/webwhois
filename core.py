import whois

from pynta.apps import PyntaApp
from pynta.templates import Mako


class Application(PyntaApp):

    urls = (
        (r'^$', 'self', {}, 'hello'),
    )

    templates = Mako

    class templates_settings:
        template = 'index.html'


    def get(self):
        return {}

    def post(self):
        domains = self.request.POST['domain_list'].replace(',', '').split()

        result= []
        for domain in domains:
            result.append((domain, bool(whois.query(str(domain)))))

        return {'result': result}
