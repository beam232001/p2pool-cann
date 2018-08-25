from p2pool.bitcoin import networks

PARENT = networks.nets['cannabiscoin']
SHARE_PERIOD = 7
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 30
IDENTIFIER = '1bfe14c3cc75a0c9'.decode('hex')
PREFIX = '1bfe14c3cd0e374a'.decode('hex')
P2P_PORT = 28742
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 28741
BOOTSTRAP_ADDRS = 'crypto.office-on-the.net siberia.mine.nu p2p-spb.xyz chel.mine.nu p2p-south.xyz'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-cann'
VERSION_CHECK = lambda v: None if 130000 <= v else 'CannabisCoin version too old. Upgrade to 0.13.0 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 1300
NEW_MINIMUM_PROTOCOL_VERSION = 3301
SEGWIT_ACTIVATION_VERSION = 17
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
