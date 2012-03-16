from collections import OrderedDict

import whois

from pynta.apps import PyntaApp
from pynta.templates import Mako

TLDS = ['com', 'ru']


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
        
        result = {}
        tlds = OrderedDict()

        for tld in TLDS:
            tlds.update({tld: tld in tld_list})

            if tlds[tld]:

                for name in names:
                    domain_tup = (name, tld)
                    result.update(
                        {domain_tup:
                            bool(whois.query(str('%s.%s' % domain_tup)))})

        return {'result': result, 'names': names, 'tlds': tlds}
