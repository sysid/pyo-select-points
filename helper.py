import logging
from collections import defaultdict
from typing import Dict

import settings

_log = logging.getLogger(__name__)


class Ok(object):

    def __init__(self, config: Dict) -> None:
        super().__init__()
        self.config = config

        self.ok = defaultdict(lambda: 0)
        self.create_ok()

    def create_ok(self) -> None:
        pass


if __name__ == '__main__':
    log_fmt = r'%(asctime)-15s %(levelname)s %(name)s %(funcName)s:%(lineno)d %(message)s'
    logging.basicConfig(format=log_fmt, level=logging.DEBUG)
    logging.getLogger('matplotlib').setLevel(logging.INFO)

    name = 'test'
    ok = Ok(config=getattr(settings, name))
