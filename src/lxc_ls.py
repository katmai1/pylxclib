import os
from pprint import pprint

class LXC_ls:
    
    # ─── PROPIEDADES ────────────────────────────────────────────────────────────────
 
    @property
    def all(self):
        return self._cmd("lxc-ls -f")
    
    @property
    def active(self):
        return self._cmd("lxc-ls -f --active")

    @property
    def frozen(self):
        return self._cmd("lxc-ls -f --frozen")
    
    @property
    def running(self):
        return self._cmd("lxc-ls -f --running")
    
    @property
    def stopped(self):
        return self._cmd("lxc-ls -f --stopped")
    
    # ─── PRIVATE METHODS ────────────────────────────────────────────────────────────

    def _cmd(self, comando):
        res = os.popen(comando).read()
        return self._parser_results(res.strip())
    
    def _parser_results(self, raw):
        if len(raw) == 0:
            return None
        json = self._genera_json(raw)
        return json

    def _genera_json(self, raw):
        r = []
        lineas = raw.split("\n")
        header = self._line2list(lineas.pop(0))
        for l in lineas:
            merged = zip(header, self._line2list(l))
            r.append(dict(merged))
        return r

    def _line2list(self, raw):
        r = []
        for item in raw.split(" "):
            c = item.replace(" ", "")
            if len(c) > 0:
                r.append(c)
        return r

