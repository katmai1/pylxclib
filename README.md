# pylxclib
Libreria en python para gestionar Linux Containers (LXC)



###########################

# Installation process and allow unprivileged user

## as root
apt install lxc libvirt0 libpam-cgroup libpam-cgfs bridge-utils cgroupfs-mount
echo 'USE_LXC_BRIDGE="true"' > /etc/default/lxc-net
echo "kernel.unprivileged_userns_clone=1" > /etc/sysctl.d/80-lxc-userns.conf
usermod --add-subuids 100000-165536 USUARIO
usermod --add-subgids 100000-165536 USUARIO
echo "USUARIO veth lxcbr0 10"| tee -i /etc/lxc/lxc-usernet
echo 'veth' >> /etc/modules
systemctl lxc-net restart

### contenido de '/etc/lxc/default.conf'
lxc.idmap = u 0 100000 65536
lxc.idmap = g 0 100000 65536
lxc.net.0.type = veth
lxc.net.0.link = lxcbr0
lxc.net.0.flags = up

## as user
cd $HOME
mkdir -p .config/lxc
setfacl -m u:100000:x . .local .local/share
echo 'lxc.include = /etc/lxc/default.conf' > .config/lxc/default.conf

########################