### 1. 
### Config CLI:
`RP/0/RP0/CPU0:Router(config)#ssh server v2`

`RP/0/RP0/CPU0:Router(config)#ssh server netconf`

`RP/0/RP0/CPU0:Router(config)#ssh server netconf vrf <vrf-name>`

### 2. 
### Config CLI:
`RP/0/RP0/CPU0:Router(config)#netconf-yang agent ssh`

`RP/0/RP0/CPU0:Router(config)#netconf agent tty`

### Verification CLI:
`show netconf-yang status`

`show netconf-yang capabilities`

### 3.
Use `"docker --version"` CLI or check Docker images with `"docker image ls"` and running container with 
`"docker container ls"`

### 6.
Use `"docker build -t led-t-netconf:latest ."` command in terminal

### 7.
Use `"docker run -it led-t-netconf:latest"` command in terminal

### 9.
Use `"show netconf-yang capabilities"` and compare them with the script ouput

### 10.
`show netconf-yang statistics` - first time

`run the file in docker container`

`show netconf-yang statistics` - once again and compare the statistics

### 11.
`clear netconf-yang trace`

> ``run the file in docker container``

`show netconf-yang trace agent`

### 12.
`pyang -f tree openconfig-interfaces.yang`

### 13.
`show netconf-yang client`

> ``ssh <username>@<host_ip>> -p 830 -s netconf`` -  from another terminal on laptop

`show netconf-yang client` - once again

