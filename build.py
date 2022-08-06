from sdk import Patch, Mod
from os import getcwd, sep

mod = Mod()

patches = [
    Patch(0xcd160, (
        b"\x4C\x20" + # movs r0, #0x4c
        b"\xa8\xf0\x27\xfd" +
        b"\x21\x00" + # movs r1, r4
        b"\x42\xf0\x56\xf8" +
        b"\xc4\xf8\x5c\x0e" + # str.w r0, [r4, #0xe5c]
        b"\x41\xf2\x67\x21" + # movw r1, #4711
        b"\x42\xf0\xbc\xf8" +
        (b"\x00\xbf" * 2)
    )),
    Patch(0xcdb50, b"\x00\xbf" * 2),
    Patch(0xce904, b"\x00\xbf" * 2),
    Patch(0xcec50, b"\x00\xbf" * 2),
    Patch(0xcfcee, b"\x00\xbf" * 2),
    Patch(0xeea30, b"\x00\xbf" * 2),
    Patch(0xf3adc, b"\x00\xbf" * 2),
    Patch(0xf702c, b"\x00\xbf" * 2),
    Patch(0x111ba8, b"\x00\xbf" * 2),
    Patch(0xcc930, b"\x00\xbf" * 2),
    Patch(0xccfa4, b"\x00\xbf" * 2),
    Patch(0xf6d8c, b"\x00\xbf" * 372),
]

for patch in patches:
    mod.add_patch(patch)

mod.save(getcwd() + sep + "pi_api.mod")
