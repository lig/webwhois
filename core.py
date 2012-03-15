from collections import OrderedDict

import whois

from pynta.apps import PyntaApp
from pynta.templates import Mako

TLDS = ['com', 'ru', 'su']


class Application(PyntaApp):

    urls = (
        (r'^$', 'self', {}, 'index'),
    )

    templates = Mako

    class templates_settings:
        template = 'index.html'


    def get(self):
        tlds = OrderedDict.fromkeys(TLDS, False)
        tlds.update({'com': True, 'ru': True})
        return {'tlds': tlds}


    def post(self):
        names = self.request.POST['domain_list'].replace(',', '').split()
        tld_list = self.request.POST.getall('tld_list')
        
        domains = []
        for name in names:
            domains.extend('%s.%s' % (name, tld) for tld in tld_list)

        result = []
        for domain in domains:
            result.append((domain, bool(whois.query(str(domain)))))

        tlds = OrderedDict()
        for tld in TLDS:
            tlds.update({tld: tld in tld_list})

        return {'result': result, 'tlds': tlds}
