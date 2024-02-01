# aplicação para o monitoramento de ambientes

## Objetivo
projeto criado no intuito da finalação do primeiro ciclo do curso de férias IoT.
----

## Descrição
O projeto visa simular o envio de dados através de um dispositivo IoT e o acesso dos mesmos através de softwares locais.


## Requisitos

* Instalar Python3.10 ou superior ([tutorial](https://computingforgeeks.com/how-to-install-python-on-ubuntu-linux-system/))
```
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
```

* simular o seguinte o dispositivo IoT:  https://wokwi.com/projects/388460858283101185

```
python3 src/main.py -a <IP_ADDRESS_OR_URL> -p <PORT> -d <ID_DISPOSITIVO_IoT>
```
**por padrão, o id do dispositivo é: 987654322**

## Menções
- O software responsável pelo acesso aos dados foi baseado no seguinte repositório: https://github.com/ruandg/simple_proxy_iot
