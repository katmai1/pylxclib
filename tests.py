import unittest
import sys
import logging

from src.lxc_manager import LXCManager
from src.errors import ContainerAlreadyExist


log = logging.getLogger(__name__)


class LXCTesting(unittest.TestCase):

    def setUp(self):
        self.lx = LXCManager("test1")

    def test_create_new_container_without_errors(self):
        '''crea un primer usuari de test  y comprueba que se 
          haya creado correctamente'''
        self.assertIsNone(self.lx.create())
        self.assertTrue(self.lx.is_created)
    
    # def test_create_container_already_exists(self):
    #     '''debe devolver una excepcion'''
    #     self.assertRaises(ContainerAlreadyExist, self.lx.create)
    
    def test_delete_containers_without_errors(self):
        '''elimina los containers usados en las pruebas'''
        self.assertEqual(len(self.lx.destroy()), 0)
        self.assertFalse(self.lx.is_created)

    def test_delete_container_that_not_exist(self):
        ...


# ─── MAIN ───────────────────────────────────────────────────────────────────────


if __name__ == "__main__":
    unittest.main()