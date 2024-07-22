# Thesis

ssh admin@193.137.203.34

ssh admin@10.3.3.114

b1vbx11

# BENCHMARK

sudo python3 run.py -cn <controller_name>

sudo python3 benchmark.py -ip <ip_addr> -p <port> -s <inicial> -q <query> -max <max_value> -n <controller_name> -t <topology> -m <metrics>  -> VER DETALHES EM ARGUMENTS_PARSER

sudo python3 benchmark.py -ip 193.137.203.34 -p 6653 -s 12 -q 3 -max 30 -n onos -t 3-tier -m N



# ONOS
sudo docker stop onos

sudo docker rm onos

sudo docker run -d -p 8181:8181 -p 8101:8101 -p 5005:5005 -p 830:830 -p 6633:6633 -p 6653:6653 -e ONOS_APPS=drivers,openflow,proxyarp,reactive-routing,fwd,gui2 --name onos onosproject/onos
OU PROACTIVE:
docker run -d -p 8181:8181 -p 8101:8101 -p 5005:5005 -p 830:830 -p 6633:6633 -p 6653:6653 -e ONOS_APPS=drivers,openflow,proxyarp,gui2 --name onos onosproject/onos

sudo docker logs onos | tail


# ODL
cd odl/karaf-0.8.4

sudo ./bin/karaf

# RYU
source ryu/bin/activate

ryu-manager ryu.app.simple_switch_13 ryu.app.rest_topology 


# LIMITATIONS

Tempo de convergência dos controladores odl e ryu: impossibilita de calcular de forma reactiva

De forma proativa, o RYU não possui endpoints para adicionar regras de fluxo, e o ODL possui documentação pouco explicita/limitada

Metricas a serem calculadas separadas em vez de forma consecutiva

Ataques a serem executados diretamente na maquina dos controladores

Rede a ser gerada na VM da execução de benchmark em vez de ser numa maquina diferente

