import os


class LXC_ctl:

    def __init__(self, name):
        self.name = name

    def _cmd(self, comando):
        res = os.popen(comando).read()
        return res

    # ─── METHODS ────────────────────────────────────────────────────────────────────

    def stop(self):
        return self._cmd(f"lxc-stop -n {self.name}")
    
    def start(self):
        return self._cmd(f"lxc-start -n {self.name}")
    
    def destroy(self):
        return self._cmd(f"lxc-destroy -n {self.name}")
    
    def shell(self):
        return self._cmd(f"lxc-attach -n {self.name}")
    
    def execute(self, cmd, silent=False):
        if self.is_running:
            res = self._cmd(f"lxc-attach -n {self.name} -- {cmd}")
        else:
            res = self._cmd(f"lxc-execute -n {self.name} -- {cmd}")
        if silent:
            return None
        return res

    # ─── PROPIEDADES ────────────────────────────────────────────────────────────────
    
    @property
    def is_stopped(self):
        if "STOPPED" in self._cmd(f"lxc-info -n {self.name} -s"):
            return True
        return False
    
    @property
    def is_running(self):
        if "RUNNING" in self._cmd(f"lxc-info -n {self.name} -s"):
            return True
        return False


if __name__ == "__main__":
    t = LXC_ctl("test3")
    t.start()
    print(t.execute("ls -l"))