from subprocess import PIPE, Popen
import logging
from .errors import ContainerAlreadyExist


# ────────────────────────────────────────────────────────────────────────────────


class LXCManager:

    def __init__(self, name):
        self.log = logging.getLogger(__name__)
        self.name = name

    # ─── PRIVATE METHODS ────────────────────────────────────────────────────────────

    def _cmd(self, comando):
        stdout, stderr = Popen(comando, stdout=PIPE, stderr=PIPE, shell=True).communicate()
        if len(stderr) > 0:
            self._parser_errors(stderr.decode("utf-8"))
        return self._parser_stdout(stdout.decode("utf-8"))
    
    def _parser_stdout(self, raw):
        if "You just created" in raw:
            return None
        return raw

    def _parser_errors(self, raw):
        if "Container already exists" in raw:
            raise ContainerAlreadyExist("Ya existe un contenedor con este nombre")
        elif "Failed to open tty" in raw:
            pass
        elif "Destroyed container" in raw:
            return None
        else:
            raise Exception(raw.decode("utf-8"))
        

    # ─── METODOS ────────────────────────────────────────────────────────────────────

    def create(self, dist="archlinux", release="current", arch="amd64"):
        comando = f"lxc-create -n {self.name} -t download -- "
        comando += f"--dist {dist} --release {release} --arch {arch}"
        return self._cmd(comando)

    def destroy(self):
        return self._cmd(f"lxc-destroy -n {self.name}")
    
    # ─── PROPIEDADES ────────────────────────────────────────────────────────────────

    @property
    def container_list(self):
        stdout = self._cmd("lxc-ls -1")
        return stdout.strip().split("\n")
        
    @property
    def is_created(self):
        if self.name in self.container_list:
            return True
        return False

# l = LXCManager("joan1")
# l.create()
# print(l.destroy())