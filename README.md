# BolivarCoin Sentinel

An all-powerful toolset for BolivarCoin.

Sentinel is an autonomous agent for persisting, processing and automating BolivarCoin v2.0 governance objects and tasks.

Sentinel is implemented as a Python application that binds to a local version 0.2 bolivarcoind instance on each BolivarCoin Masternode.

This guide covers installing Sentinel onto an existing 0.1 Masternode in Ubuntu 14.04 / 16.04.

## Installation

### 1. Install Prerequisites

Make sure Python version 2.7.x or above is installed:

    python --version

Update system packages and ensure virtualenv is installed:

    $ sudo apt-get update
    $ sudo apt-get -y install python-virtualenv

Make sure the local BolivarCoin daemon running is at least version 0.2 (2000002)

    $ bolivarcoin-cli getinfo | grep version

### 2. Install Sentinel

Clone the Sentinel repo and install Python dependencies.

    $ git clone https://github.com/BOLI-Project/sentinel.git && cd sentinel
    $ mkdir database
    $ virtualenv ./venv
    $ ./venv/bin/pip install -r requirements.txt

### 3. Set up Cron

Set up a crontab entry to call Sentinel every minute:

    $ crontab -e

In the crontab editor, add the lines below, replacing '/home/YOURUSERNAME/sentinel' to the path where you cloned sentinel to:

    * * * * * cd /home/YOURUSERNAME/sentinel && ./venv/bin/python bin/sentinel.py >/dev/null 2>&1

### 4. Test the Configuration

Test the config by runnings all tests from the sentinel folder you cloned into

    $ ./venv/bin/py.test ./test

With all tests passing and crontab setup, Sentinel will stay in sync with bolivarcoind and the installation is complete

## Configuration

An alternative (non-default) path to the `Bolivarcoin.conf` file can be specified in `sentinel.conf`:

    boli_conf=/path/to/Bolivarcoin.conf

## Troubleshooting

To view debug output, set the `SENTINEL_DEBUG` environment variable to anything non-zero, then run the script manually:

    $ SENTINEL_DEBUG=1 ./venv/bin/python bin/sentinel.py

### License

Released under the MIT license, under the same terms as BolivarCoin Core itself. See [LICENSE](LICENSE) for more info.

## Español

### 1. Instalar requisitos:

Verifique tener instalado la versión 2.7.x de Python o una versión superior.

    python --version

Actualice los paquetes del sistema y asegúrese de que virtualenv esté instalado:

    $ sudo apt-get update
    $ sudo apt-get -y install python-virtualenv

Asegúrese de que el demonio local BolivarCoin en ejecución sea al menos la versión 0.2 (2000002)

    $ bolivarcoin-cli getinfo | grep version

### 2. Instalar Sentinel

Clone el repositorio de Sentinel e instale las dependencias de Python.

    $ git clone https://github.com/BOLI-Project/sentinel.git && cd sentinel
    $ mkdir database
    $ virtualenv ./venv
    $ ./venv/bin/pip install -r requirements.txt

### 3. Edite el archivo de configuración:

Dentro de la carpeta sentinel edite el archivo `sentinel.conf`, ajustando la linea siguiente:

```
   # boli_conf=/path/to/Bolivarcoin.conf
```

Si su Master Nodo se encuentra ubicado en `/root/.Bolivarcoin` entonces debe editar la linea de la siguiente manera apuntando al archivo `Bolivarcoin.conf`:

    boli_conf=/root/.Bolivarcoin/Bolivarcoin.conf

### 4. Pruebe de configuración.

Si edito correctamente el archivo `sentinel.conf` realice una prueba de funcionamiento con la siguiente instrucción:

    $ SENTINEL_DEBUG=1 ./venv/bin/python bin/sentinel.py

### 5. Configure Cron

Configure una entrada crontab para llamar a Sentinel cada minuto:

    $ crontab -e

En el editor de crontab, agregue las líneas a continuación, reemplazando '/root/sentinel' con la ruta donde clonó Sentinel:

    * * * * * cd /root/sentinel && ./venv/bin/python bin/sentinel.py >/dev/null 2>&1