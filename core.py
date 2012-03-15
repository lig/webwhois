import whois

from pynta.apps import PyntaApp
from pynta.storage import Mongodb
from pynta.templates import Mako


class Application(PyntaApp):

    urls = (
        (r'^$', 'self', {}, 'hello'),
    )

    templates = Mako
    storage = Mongodb

    class templates_settings:
        template = 'index.html'


    def get(self):
        return {}

    def post(self):
        names = self.request.POST['domain_list'].replace(',', '').split()
        tld_list = self.request.POST.getall('tld_list')
        
        domains = []
        for name in names:
            domains.extend('%s.%s' % (name, tld) for tld in tld_list)

        result = []
        for domain in domains:
            result.append((domain, bool(whois.query(str(domain)))))

        tlds = {}
        for tld in ['ru', 'su', 'com']:
            tlds.update({tld: tld in tld_list})

        return {'result': result, 'tlds': tlds}
