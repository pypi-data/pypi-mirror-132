#!/usr/bin/python3
import sys
from os.path import join, dirname, abspath
import unittest
import struct

rootDir = dirname(dirname(abspath(__file__)))
sys.path.insert(0, rootDir)

from pyglossary.text_utils import *


class TestTextUtils(unittest.TestCase):
	def test_unescapeNTB(self):
		self.assertEqual("a", unescapeNTB("a", bar=False))
		self.assertEqual("a\t", unescapeNTB("a\\t", bar=False))
		self.assertEqual("a\n", unescapeNTB("a\\n", bar=False))
		self.assertEqual("\ta", unescapeNTB("\\ta", bar=False))
		self.assertEqual("\na", unescapeNTB("\\na", bar=False))
		self.assertEqual("a\tb\n", unescapeNTB("a\\tb\\n", bar=False))
		self.assertEqual("a\\b", unescapeNTB("a\\\\b", bar=False))
		self.assertEqual("a\\\tb", unescapeNTB("a\\\\\\tb", bar=False))
		self.assertEqual("a|b\tc", unescapeNTB("a|b\\tc", bar=False))
		self.assertEqual("a\\|b\tc", unescapeNTB("a\\|b\\tc", bar=False))
		self.assertEqual("a\\|b\tc", unescapeNTB("a\\\\|b\\tc", bar=False))
		self.assertEqual("|", unescapeNTB("\\|", bar=True))
		self.assertEqual("a|b", unescapeNTB("a\\|b", bar=True))
		self.assertEqual("a|b\tc", unescapeNTB("a\\|b\\tc", bar=True))

	def test_escapeNTB(self):
		self.assertEqual(escapeNTB("a", bar=False), "a")
		self.assertEqual(escapeNTB("a\t", bar=False), "a\\t")
		self.assertEqual(escapeNTB("a\n", bar=False), "a\\n")
		self.assertEqual(escapeNTB("\ta", bar=False), "\\ta")
		self.assertEqual(escapeNTB("\na", bar=False), "\\na")
		self.assertEqual(escapeNTB("a\tb\n", bar=False), "a\\tb\\n")
		self.assertEqual(escapeNTB("a\\b", bar=False), "a\\\\b")
		self.assertEqual(escapeNTB("a\\\tb", bar=False), "a\\\\\\tb")
		self.assertEqual(escapeNTB("a|b\tc", bar=False), "a|b\\tc")
		self.assertEqual(escapeNTB("a\\|b\tc", bar=False), "a\\\\|b\\tc")
		self.assertEqual(escapeNTB("|", bar=True), "\\|")
		self.assertEqual(escapeNTB("a|b", bar=True), "a\\|b")
		self.assertEqual(escapeNTB("a|b\tc", bar=True), "a\\|b\\tc")

	def test_splitByBarUnescapeNTB(self):
		f = splitByBarUnescapeNTB
		self.assertEqual(f(""), [""])
		self.assertEqual(f("|"), ["", ""])
		self.assertEqual(f("a"), ["a"])
		self.assertEqual(f("a|"), ["a", ""])
		self.assertEqual(f("|a"), ["", "a"])
		self.assertEqual(f("a|b"), ["a", "b"])
		self.assertEqual(f("a\\|b|c"), ["a|b", "c"])
		self.assertEqual(f("a\\\\1|b|c"), ["a\\1", "b", "c"])
		# self.assertEqual(f("a\\\\|b|c"), ["a\\", "b", "c"])  # FIXME
		self.assertEqual(f("a\\\\1|b\\n|c\\t"), ["a\\1", "b\n", "c\t"])

	def test_unescapeBar(self):
		f = unescapeBar
		self.assertEqual("", f(""))
		self.assertEqual("|", f("\\|"))
		self.assertEqual("a|b", f("a\\|b"))
		self.assertEqual("a|b\tc", f("a\\|b\tc"))
		self.assertEqual("a|b\\t\\nc", f("a\\|b\\t\\nc"))
		self.assertEqual("\\", f("\\\\"))
		self.assertEqual("\\|", f("\\\\\\|"))

	def test_splitByBar(self):
		f = splitByBar
		self.assertEqual(f(""), [""])
		self.assertEqual(f("|"), ["", ""])
		self.assertEqual(f("a"), ["a"])
		self.assertEqual(f("a|"), ["a", ""])
		self.assertEqual(f("|a"), ["", "a"])
		self.assertEqual(f("a|b"), ["a", "b"])
		self.assertEqual(f("a\\|b"), ["a|b"])
		self.assertEqual(f("a\\|b|c"), ["a|b", "c"])
		self.assertEqual(f("a\\\\1|b|c"), ["a\\1", "b", "c"])
		# self.assertEqual(f("a\\\\|b|c"), ["a\\", "b", "c"])  # FIXME

	def test_unescapeBarBytes(self):
		f = unescapeBarBytes
		self.assertEqual(b"", f(b""))
		self.assertEqual(b"|", f(b"\\|"))
		self.assertEqual(b"a|b", f(b"a\\|b"))
		self.assertEqual(b"a|b\tc", f(b"a\\|b\tc"))
		self.assertEqual(b"a|b\\t\\nc", f(b"a\\|b\\t\\nc"))
		self.assertEqual(b"\\", f(b"\\\\"))
		self.assertEqual(b"\\|", f(b"\\\\\\|"))

	def test_splitByBarBytes(self):
		f = splitByBarBytes
		self.assertEqual(f(b""), [b""])
		self.assertEqual(f(b"|"), [b"", b""])
		self.assertEqual(f(b"a"), [b"a"])
		self.assertEqual(f(b"a|"), [b"a", b""])
		self.assertEqual(f(b"|a"), [b"", b"a"])
		self.assertEqual(f(b"a|b"), [b"a", b"b"])
		self.assertEqual(f(b"a\\|b"), [b"a|b"])
		self.assertEqual(f(b"a\\|b|c"), [b"a|b", b"c"])
		self.assertEqual(f(b"a\\\\1|b|c"), [b"a\\1", b"b", b"c"])
		# self.assertEqual(f("a\\\\|b|c"), ["a\\", "b", "c"])  # FIXME

	def test_formatHMS(self):
		f = formatHMS
		self.assertEqual(f(0, 0, 0), "00")
		self.assertEqual(f(0, 0, 9), "09")
		self.assertEqual(f(0, 0, 10), "10")
		self.assertEqual(f(0, 0, 59), "59")
		self.assertEqual(f(0, 1, 0), "01:00")
		self.assertEqual(f(0, 1, 5), "01:05")
		self.assertEqual(f(0, 5, 7), "05:07")
		self.assertEqual(f(0, 59, 0), "59:00")
		self.assertEqual(f(0, 59, 59), "59:59")
		self.assertEqual(f(1, 0, 0), "01:00:00")
		self.assertEqual(f(123, 5, 7), "123:05:07")
		self.assertEqual(f(123, 59, 59), "123:59:59")

	def test_uint32ToBytes(self):
		f = uint32ToBytes
		self.assertEqual(f(0), bytes([0, 0, 0, 0]))
		self.assertEqual(f(0x3e8), bytes([0, 0, 0x03, 0xe8]))
		self.assertEqual(f(0x186a0), bytes([0, 1, 0x86, 0xa0]))
		self.assertEqual(f(0x3b9aca00), bytes([0x3b, 0x9a, 0xca, 0x00]))
		self.assertEqual(f(0xffffffff), bytes([0xff, 0xff, 0xff, 0xff]))

		with self.assertRaises(struct.error) as ctx:
			f(0xffffffff + 1)
		self.assertEqual(
			str(ctx.exception),
			"'I' format requires 0 <= number <= 4294967295",
		)

		with self.assertRaises(struct.error) as ctx:
			f(10000000000)
		self.assertEqual(
			str(ctx.exception),
			"'I' format requires 0 <= number <= 4294967295",
		)

		with self.assertRaises(struct.error) as ctx:
			f(-1)
		self.assertEqual(str(ctx.exception), "argument out of range")

	def test_uint32FromBytes(self):
		f = uint32FromBytes
		self.assertEqual(0, f(bytes([0, 0, 0, 0])))
		self.assertEqual(0x3e8, f(bytes([0, 0, 0x03, 0xe8])))
		self.assertEqual(0x186a0, f(bytes([0, 1, 0x86, 0xa0])))
		self.assertEqual(0x3b9aca00, f(bytes([0x3b, 0x9a, 0xca, 0x00])))
		self.assertEqual(0xffffffff, f(bytes([0xff, 0xff, 0xff, 0xff])))

		with self.assertRaises(struct.error) as ctx:
			f(bytes([0x01, 0xff, 0xff, 0xff, 0xff]))
		self.assertEqual(str(ctx.exception), "unpack requires a buffer of 4 bytes")

	def test_uintFromBytes(self):
		f = uintFromBytes
		self.assertEqual(0, f(bytes([0, 0, 0, 0])))
		self.assertEqual(0x3e8, f(bytes([0, 0, 0x03, 0xe8])))
		self.assertEqual(0x186a0, f(bytes([0, 1, 0x86, 0xa0])))
		self.assertEqual(0x3b9aca00, f(bytes([0x3b, 0x9a, 0xca, 0x00])))
		self.assertEqual(0xffffffff, f(bytes([0xff, 0xff, 0xff, 0xff])))
		self.assertEqual(
			0xffabcdef5542,
			f(bytes([0xff, 0xab, 0xcd, 0xef, 0x55, 0x42])),
		)

	def test_crc32hex(self):
		f = crc32hex
		self.assertEqual(f(b""), "00000000")
		self.assertEqual(f(b"\x00"), "d202ef8d")
		self.assertEqual(f(b"\x00\x00"), "41d912ff")
		self.assertEqual(
			f(bytes.fromhex("73c3bbc38b7459360ac3a9c2b3c2a2")),
			"bbfb1610",
		)

	def test_urlToPath(self):
		f = urlToPath
		self.assertEqual(
			f("https://github.com/ilius/pyglossary"),
			"https://github.com/ilius/pyglossary",
		)
		self.assertEqual(
			f("file:///home/test/abc.txt"),
			"/home/test/abc.txt",
		)
		self.assertEqual(
			f("file:///home/test/%D8%AA%D8%B3%D8%AA.txt"),
			"/home/test/تست.txt",
		)

	def test_replacePostSpaceChar(self):
		f = replacePostSpaceChar
		self.assertEqual(
			f("First sentence .Second sentence.", "."),
			"First sentence. Second sentence.",
		)
		self.assertEqual(
			f("First ,second.", ","),
			"First, second.",
		)

	def test_isASCII(self):
		f = isASCII
		self.assertEqual(f(""), True)
		self.assertEqual(f("abc"), True)
		self.assertEqual(f("xyz"), True)
		self.assertEqual(f("ABC"), True)
		self.assertEqual(f("XYZ"), True)
		self.assertEqual(f("1234567890"), True)
		self.assertEqual(f("\n\r\t"), True)
		self.assertEqual(f("\x80"), False)
		self.assertEqual(f("abc\x80"), False)
		self.assertEqual(f("abc\xff"), False)


if __name__ == "__main__":
	unittest.main()
