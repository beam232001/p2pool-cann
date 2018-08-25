import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fec3b9de'.decode('hex')
P2P_PORT = 39348
ADDRESS_VERSION = 28
RPC_PORT = 39347
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_block_header(bitcoind, '00000a10f7ce671e773330376ce892a6c0b93fbc05553ebbf659b11e3bf9188d')) and # genesis block
            (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'main'
        ))
SUBSIDY_FUNC = lambda height: 70*100000000
BLOCK_PERIOD = 42 # s
SYMBOL = 'CANN'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'CannabisCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/CannabisCoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.CannabisCoin'), 'CannabisCoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/cann/block.dws?'
ADDRESS_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/cann/address.dws?'
TX_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/cann/tx.dws?'
SANE_TARGET_RANGE = (2**256//2**32//1000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 1e8
