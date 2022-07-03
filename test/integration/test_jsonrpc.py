import pytest
import sys
import os
import re
os.environ['SENTINEL_ENV'] = 'test'
os.environ['SENTINEL_CONFIG'] = os.path.normpath(os.path.join(os.path.dirname(__file__), '../test_sentinel.conf'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import config

from bolid import BoliDaemon
from boli_config import BoliConfig


def test_bolid():
    config_text = BoliConfig.slurp_config_file(config.boli_conf)
    network = 'mainnet'
    is_testnet = False
    genesis_hash = u'000004ccb109d21edfb9dd8bfddacf55a26e8ae3ccb5f04898d849ea38bd118c'
    for line in config_text.split("\n"):
        if line.startswith('testnet=1'):
            network = 'testnet'
            is_testnet = True
            genesis_hash = u'000008c9c92d68854ca14a1d6efd46a10f5549443c858ad814eca81550138e36'

    creds = BoliConfig.get_rpc_creds(config_text, network)
    bolid = BoliDaemon(**creds)
    assert bolid.rpc_command is not None

    assert hasattr(bolid, 'rpc_connection')

    # Bolivarcoin testnet block 0 hash == 000004ccb109d21edfb9dd8bfddacf55a26e8ae3ccb5f04898d849ea38bd118c
    # test commands without arguments
    info = bolid.rpc_command('getinfo')
    info_keys = [
        'blocks',
        'connections',
        'difficulty',
        'errors',
        'protocolversion',
        'proxy',
        'testnet',
        'timeoffset',
        'version',
    ]
    for key in info_keys:
        assert key in info
    assert info['testnet'] is is_testnet

    # test commands with args
    assert bolid.rpc_command('getblockhash', 0) == genesis_hash
