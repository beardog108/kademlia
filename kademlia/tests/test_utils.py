from hashlib import shake_128

from kademlia.utils import digest, shared_prefix


class TestUtils:
    def test_digest(self):  # pylint: disable=no-self-use
        dig = shake_128(b'1').digest(20)
        assert dig == digest(1)

        dig = shake_128(b'another').digest(20)
        assert dig == digest('another')

    def test_shared_prefix(self):   # pylint: disable=no-self-use
        args = ['prefix', 'prefixasdf', 'prefix', 'prefixxxx']
        assert shared_prefix(args) == 'prefix'

        args = ['p', 'prefixasdf', 'prefix', 'prefixxxx']
        assert shared_prefix(args) == 'p'

        args = ['one', 'two']
        assert shared_prefix(args) == ''

        args = ['hi']
        assert shared_prefix(args) == 'hi'
