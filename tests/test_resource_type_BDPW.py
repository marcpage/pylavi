#!/usr/bin/env python3


from pylavi.resource_types import TypeBDPW


def test_basics():
    for binary in TEST_CASES:
        bdpw = TypeBDPW().from_bytes(binary)
        assert bdpw.to_bytes() == binary
        description = bdpw.to_dict()
        reconstituted = TypeBDPW().from_dict(description)
        assert reconstituted.to_bytes() == binary
        assert bdpw.has_password() == TEST_CASES[binary], binary

    binary = b'_M\xcc;Z\xa7e\xd6\x1d\x83\'\xde\xb8\x82\xcf\x99\xaeR}\xd8\xc4\xb7\xb4\x8e\xca\xcf\x89o\xea\x00_\x99t\xd3\xf8\xd9\xa3\xa0!\xcc\xf3\x03x"\xd8\xb1/\xb4'
    bdpw = TypeBDPW().from_bytes(binary)
    assert bdpw.size() == 48
    assert bdpw.password_matches('password')
    assert str(bdpw) == "{password_md5=5f4dcc3b5aa765d61d8327deb882cf99, extra=ae527dd8c4b7b48ecacf896fea005f9974d3f8d9a3a021ccf3037822d8b12fb4}"
    assert repr(bdpw) == "TypeBDPW({password_md5=5f4dcc3b5aa765d61d8327deb882cf99, extra=ae527dd8c4b7b48ecacf896fea005f9974d3f8d9a3a021ccf3037822d8b12fb4})"


TEST_CASES = {
    b'_M\xcc;Z\xa7e\xd6\x1d\x83\'\xde\xb8\x82\xcf\x99\xaeR}\xd8\xc4\xb7\xb4\x8e\xca\xcf\x89o\xea\x00_\x99t\xd3\xf8\xd9\xa3\xa0!\xcc\xf3\x03x"\xd8\xb1/\xb4': True,
    b'\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~Bt\xcc\xe02;\xc1v\xc0/j\xa5\xa6\xea!\xb7': False,
    b" W\x11\xd1@r=k\xbbe\x16V+\x9dE\xc8%\xca1*\x9eQ\x10\xf5\xdc8:,\xdf\x96\xf1\xee\xa8\xab'\xdf\x05G{\xbd\x8c\xfc\xdb\x8b7\xec<I": True,
    b" W\x11\xd1@r=k\xbbe\x16V+\x9dE\xc8'\xa6\xae\x8e\x98\xba\xd1\x10c\xa1\xce\x85\x0b\xa0\xdca\xc0\xb3\xf1\xab%\x85.\x9e\xf8\x9b\xa6Z\xa8a\x90\x8b": True,
    b"$/\xa1x{\x13\xe4\xf8?,\xe4O\xc9\xb0\xc6\xaajR8\xbe\xfc.\xfe\xac7O\x9e`\xab\x89\x1d\xc0\xaa\xdd\x903W\x8c\x17C\xd2E\xec\xa8\x1b'\xc2\xbf": True,
    b"&8\x7f\xc9\xbc\\\xf0\x8b%\xa8\xef\xad\xc8\xc48\x94\xbf\x97\x85 o6\xc8=\xf5]\x10\xfcB\xb6\xecYg\xf5\xa4\x04\xea\x11\x91kW\xad\xc2W*\xd4'X": True,
    b"&8\x7f\xc9\xbc\\\xf0\x8b%\xa8\xef\xad\xc8\xc48\x94\xe3f\xcd\x81\xa7\xd3\r]v}\xf9\x8c\x18nk\xed\xe2\xc9\xa0\xc9\xa7\xabFk'\xf1\xb3m]G\xd0\xbe": True,
    b"'N\xb1\xa9\xa5.X\x14\xfa\x03\xff\xe9\xef\x12\x8d\\W\x1e\t\x9d\xf71\x85\xb0R\xa8\x9b,\x0f\xc8\xd5\xca1\xa5\x84\xad\xfd\xac\xb7\xd1N\x13\x12\xda\x1d|\xd0K": True,
    b"'N\xb1\xa9\xa5.X\x14\xfa\x03\xff\xe9\xef\x12\x8d\\[B\xfce\x8eZ8\xf0\xf0\x8e/!\xfc\xbb=\xf4i\x88\xee\x9f\xbb|-7\xe7\xb7\xa3\n\x85\xbd\xfaO": True,
    b"'\xa4xM\xff\xb4\xb2G\xd5\xa3\xe8\xe0\xe9\xd0Ag \n#\xf5\xd5]\xeb%\x17\x85\xbcg\xbe\x8a\xc3\xf0\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~": True,
    b"(\t5OQ\xfa\xb9u>vf\xab\xfb5E\x99M/\x89\xe0'\x01&\xe0\x0e\x9f\xa4\x10\xc1\x8b\x92O\xd6\xd3\xf4\x15\xa9\xc1\x17\x8f\x01\xd9tP\xacsV\x11": True,
    b")\xba\xfc\x0e\xef\xed\x11_\xb6+\x1c\xd2\x97\x95\xa2\x9c.\xa3\xf5\xf6\xcd\x85\xa3\x16'\xe4\xd2a\xb4?m8\n\xc8p\xcd\xcd\x14\x1d:9\x00\xfa\x8f\x0e\x04\xee\\": True,
    b")\xba\xfc\x0e\xef\xed\x11_\xb6+\x1c\xd2\x97\x95\xa2\x9c\x9d\xe9\x02'\xa6\xeesR>>\x96pEl\xa0\x7f\xf7b\xd0k\x08\x0b\xb4\x8c\x19I\xb0\xb4\x04\xf3U\xaf": True,
    b")\xba\xfc\x0e\xef\xed\x11_\xb6+\x1c\xd2\x97\x95\xa2\x9c\xb8+\xda\xbb\x7f\\\xf0\x84\x92\xa9\xdb'\xb8\xd1\xb1\xa5\r\xdc\xdcu\x04\x95U>\xf5(\xeax\x04\xaaa\xe0": True,
    b")\xba\xfc\x0e\xef\xed\x11_\xb6+\x1c\xd2\x97\x95\xa2\x9c\xe8WQ/\xdd\xdd\xce\x82\xf2\x96~EUS\x8d{\xaf\xf7\xf5\xd1?\x92B\x85\xa0\xa0\xe7\xc8\xb8'\x0b\x1b": True,
    b"*,\x9dJ\x99\x87r\t\x16\xe4^\x044\x04Y\xc61R.\xafJ\x8d\x98\x8e#\xc3'B\xc4=`\xe6~,V\x0b\xc3G\xeb7A\x12\x9aO\xb2\xe5\xb9M": True,
    b"/\x92\x0b\x1e\xa1\x9e\x86][\x1c\x86\xbf\xbf\x11\x95.b\xba\x81\xb4\x9dT\xb5(\xfa\x8f\xaf\xcfz\xf9\x0bna~\x8e'p\xd6\xea\xe86s\n\x99\x87?\xd5\x1d": True,
    b"0\xb3(\xd5>\x17\x14\xdek\xde^\xd3\xb1~\x01\xadQ\x84\x01\xc7\x91T\x87\x94\x8b6\x1a\xbf%\x04l<(\xc6\x1a'\x97\x01\xbd\x1e\x14\x8a\xbc\x97\x17s\x86\xd6": True,
    b"2\x89\xae\x001~\x1d\x87\xd2^#\x8d\xd4\xe9\xdf\x001\xb5\x96X/2\xb3R\xbd\xc8{A\xbf\x95\x043\x04%\x17\xf9^\xebX\x1ds\xad'\x0bk\xb53\xb5": True,
    b"5\xf4t\xfd\xa3\x11qh4\x86B)\xb5\xde\xe3\xb0\xf9|yE\xc1\x98\x92\r\xc21\x13\x80j\x84B\x01d\xf1u\x89\xcfQ\xa4\x86\x83\x04\xa7\xb3\t'k\xa4": True,
    b"7\xdd\xc9\xeb\xe9U`n\xb3\xb6\xe9\x9d\x93\xb23Y/\xe0\x04\xbc\xa7'\x92\x8c\xfc\xee\t\xc0\x89\xfdg\xf0\xf0\xc6K\x1db\xbd\xc7F\xbbL\xcag\xcc\xb1\xa7\x8c": True,
    b"8X\xecz\x8b\x92\xdf\x86d\x90;V\xd0\xd1\xb3T\xfa(\x95\xbb\xb4\xda\xb5d'\xb4\xa0`q\xbb\x8e\xc2\x8b\xb0\x1b\xda\xb3\xfe\xbd\xdft\x99{9Y\x80~\xc0": True,
    b">\xb1\xbeP\xdd \x12Y\x0e\xba\xca\x92<\xde[*)\xc8\x98'\xb3:\x06\x8f\x1c\xb1 G\xd4\xb6\x9b\xab`\x0bL\xea\x94\xa8@\xfd5\xca\xe2\x93beG\xa8": True,
    b">\xb1\xbeP\xdd \x12Y\x0e\xba\xca\x92<\xde[*o\x8b\n\x84\xbeU~\\\x8a\x08I\x90\xae\xb5\x85\x04^|\xef\xfe\xda\xbfCQ\x90-e$`{'\xa6": True,
    b"@\x19\xd6\x18\x13\x05m\x1b|UOc\xe5\xa7\xd26 \x15\xf0'\x12\xab\x18M\x9ft\x05\xcb\x8a\x8d\x98\x1c\xc4\x8c\xea\xe8<\xd4<q\xb8\xf7\x14\x01\xc3\xb5M\xe9": True,
    b"A\t\xd4yzy%\x00\x0c+\x11\xb5\xabrK=szw\xebX\xbeH\xc2'\xf2\xd9s\xde`\xba\x06\xe4\xa2\x14\x0fZ\x01a\x8fg[\xe5\x7f\xdcd\xae\xaa": True,
    b"A\xaf\xf52=\xce^\x1az\x0b\x0c\x02\x7f\xcc\xcf\xbd(\xd3\xb8B\x0f\xc4\xd5|1\xf0'\x10O\xbe\xde\xfe\xdd\xf5\xb5[\xcc^CLQ\xb6l\xdc\x05=\xf5|": True,
    b"A\xaf\xf52=\xce^\x1az\x0b\x0c\x02\x7f\xcc\xcf\xbdL\xc9\n*\xf8\xb6)o\xf9\x99}F\x93\x1f\xc9_\xac\xc4\xae\x98}\xb8\tp\xd2'\xa6\xa8\xe5\xc9y\x8b": True,
    b"A\xaf\xf52=\xce^\x1az\x0b\x0c\x02\x7f\xcc\xcf\xbd\xb4\x8d\xe5\x83\x03\xb1oYB\x8c'\xc8r`P\x86\x88s\x17B\x82\xa1\xf2F\x0e\xc2\xba\xb4,D\xd4]": True,
    b"A\xaf\xf52=\xce^\x1az\x0b\x0c\x02\x7f\xcc\xcf\xbd\xb8\x9c)\xe8\xbdf\xe2\xb2\xa8]\xa7\xa5mY~'\xc8\x0b(+Rht\x93\xcb\x12\xcb/\xf9\x8aZ$": True,
    b"A\xaf\xf52=\xce^\x1az\x0b\x0c\x02\x7f\xcc\xcf\xbdj\x8a\xa7\xb2U\x94\x0bD\xaa\x8a\x96d\xf6'\xf4\xacu\x0c\xa8:Fyz\xed@\xbf\xf9\x94\xd0\xef(W": True,
    b"A\xaf\xf52=\xce^\x1az\x0b\x0c\x02\x7f\xcc\xcf\xbdl\xc2\x12oJf\xf6\xeb\x80\x91lZ\xee$\xf0p\x1b\xd2\x9c7\xd7jG#\xf6'?\xc84\xcf\xc4@": True,
    b"A\xaf\xf52=\xce^\x1az\x0b\x0c\x02\x7f\xcc\xcf\xbdx\xcf\xbf\x0b\xb7\xb6\xa1\x1b\x7f\xb7\x8f\xc3\xc0\t\x8a\xea\xdd\x14D\xd6\\\x1c'=\xeb\xf8\xed\xedt42\x05": True,
    b"C\xb6\x91\xd8\xcde\xf6\xa0\xdf\xd0E\x97\x8fe{\x03'\xb8\x1b)\x08m\xe6\xb1r\x97'\xb9\x1f\x11\x16\x00_\xc7\xc9\xff \xa2A\x03\xff\xb5\x12\x14\x10[\xee)": True,
    b"E>\x03.3\xe9\xd7\xceJ\xfbq\xc6\xd9\xb1\xe0\x82;\x8d\xc3\xf6\x04\xfd\xfc\xff\xe5X\xe5\x87\xe7'\xaeN\x86}\xca\xc4\xc23H\xbb\x10]\x85\xe7\x89\xa9-\xc9": True,
    b"FyU\xb5\xf1\xe7dN\x9b\x93/\n\x87\xc3\xd8\xa91\xa9\xba\xf6\xeaO\x94?'\xf5\xe3\xbf\xf9\xaf\xa4f\xdd\x85\xce\x8d\xc9\xe4U\x0c\x0b\x1e<A(\x89^\x89": True,
    b"G\xff_\x80\x03\x0b\xb7d';\xd7ks\xc1`\x98\x08\x9bJ\xaf\xbd\x16\xc1\xa9%\xe3\x80\xac\xe1O\xffp&\xdb\xb1\x9fEMV\xa7\xa4/\x16p,\xef=\x0c": True,
    b"G\xff_\x80\x03\x0b\xb7d';\xd7ks\xc1`\x98\x0bW(\xc5\xa1`\xff/\xd7\xf0\x18\xaal~@\xfd\xb8\xc1\x1bT-\xa4]7\x9fy\xa8\x13\x15\x87\x07\x98": True,
    b"G\xff_\x80\x03\x0b\xb7d';\xd7ks\xc1`\x98\xbaw\x8f\x91\x1dA3<\x01x\xd4\x95x\xdf\xc9\x10Zp(\xbf\xe5:\xc4\xe2@\xed\x9dFA\xf6\xfbs": True,
    b"H\xcf\x95\xc7\x922r'\xc2\x83\xcf5\x02\x054\xb6(\x85\x14@\r\x83\xec\x91\xf7)\xcf\x92\xe33\xec\xa6\xa0\x9f\xebW\xd0\xeb\xa3\xe5\x9a\x1c\xad\x9cd\xed\xb2)": True,
    b"I\x08\xb1\x91a\xc4\x1e\xa5\x83}\xe1\x9b\xda\xee\x9a\x10\x8f\x0c\x82\xcb\xa5\x93z\xbf\x9aX\x1c\\\xc5\x89.'\xc3\x80\x98\xee\x8d\xb4\x82\xdd\x86\x99Q\x94YW\x7f\x18": True,
    b"KU\xfe\xf2m>8o\x03\x07;\xe8\xf0\xf6a\xb6\xc1r\xf3L\xde\xc5\x19R\xf8NZ\xdb\xa5\xd8w\xe2L\xaf\x08\xf9'\xf4p\xfb\xc0\xe0\xd3\x8al\xec\x94\x13": True,
    b"KU\xfe\xf2m>8o\x03\x07;\xe8\xf0\xf6a\xb6_\x85\x04\xd7h\xb4\x8b'#\xa9\xb9\x8cb\xb2\xdb-_\xe9\xbc\x97\xae\xb0\xa5Nh\xf9\x84\xa0Y\x8f#C": True,
    b"K\xc7\x9e%\n]\xcc\x06r\xc1'\xcc\xf9\xf89e(\x0e\xb9\xdc\x065\x99\xfe\xc2\xb9\xe3\t;\xa2\x0e\xd1*\xdd\xaf\xd2\x13\xdc\xb5E\xca\x16\xads\\\x92@n": True,
    b'\xd3\xb8\xa3\xa5sR\xf5\xa9\xf9b\xf9{\xf60\xadr\x94M\xa3<\xe2#p\xe4\x97\xc94\xb3&\xfc\x10S\xd3\xeb\xbbd\xb7\x8b\x03\xa7Z$`\xc6\xd9\xbfV\xc0': True,
    b'\xd4\x00\xed\x98\x05-\xee\x1e\x96\xb2\xd8F\n\xb6=\xb0\xf0\x1aNpw\x04\xcf\xd3\xfd\x84_\x0bNB\x1b\xcb}\xfe\xc3\xa3\xfbp\xa4\x92G\xb8\xf8$\xdf\xa0\x08\xe8': True,
    b'\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~  \xd8\xa5\x07\xe0\x18\x0b\x8c\xed+\xab\tD\xe6d}9o\x08\xf2^*k\x94\x96\x93\xd2+\xcaX\xaa': False,
    b'\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~ !C\x16\x02\x8b\xda\xd8ZU\x15\xf4\xa7s\th\x93\x0b\xcf\x93l\xafetK\x15@\xb6\xf9\xd9v\xa8': False,
    b'\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~ !R\xe67\x99\xd9\xc5\xcb\x1fq\xec\x16\xf5!\xdb\xba\x10p\xc9\xa8>\xeb1"\xc78\xca\x8a\xc4\x904': False,
    b'\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~ !\xa2\xa4\xed\x82\xce\xfa\xe4{\xeek\xa7R\xbe\x98(-\x85\x97\xa5\xc0\xd2%N\x02\x91\xef5GBl': False,
    b'\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~ ")@\xcd\x0c\xed\x99\x95\ro8\xf8\xab\x81+\x803\x1b}\xb9\x04\x8aw\x9du\xd2\xb8I\xabg\xd4': False,
    b'\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~ "\'\xaf!\x8c\xb5\xb7\xec\xa9\xbf\xa8\xcc\x02\x8f\xb4e2C^\xdf\x14\xeag\x07\xb2\x84|a\xbc\xf0\n': False,
    b'\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~ "\xa9\xf9&D\xb3\x8d\x10x\x17\xe4+\x08\xe7\xec%\x00\xee7\xdf\xfeW\xa0\x10\xf7\xd3)\xdfM\x15\t': False,
    b'\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~ "\xa9\xf9&D\xb3\x8d\x10x\x17\xe4+\x08\xe7\xec%\x00\xee7\xdf\xfeW\xa0\x10\xf7\xd3)\xdfM\x15\t': False,
    b'\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~ "\xc9\x9dn\x9aM"n\xf0\xe4@\x9d\xff\x8e\xe6\xc0\xcd\xcb\xcf\xe8,\x9d,i)a\r\xea\x15b\x9a': False,
    b'\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~ "]RC\x01\xa6\xcc \xbbQ\xac\xe5\xb3\xfb\xc4\xe9\x8f+\x82\xe6\x0e\xee%\x13\xec\x10\xf7[x\xa7y': False,
    b'\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~ #\x06\xad<I\x15\xd8\xf71\xe9\xa4y\x82\x12\xec\xbe\x1cMP\xe90\x8f\x1e\xe8\xfc\x1d\xb7=\x1d\nr': False,
    b'\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~ #\x8f\xec3_\x06`\xbb\x17\x96\xe2\xf7<\x9b\xaa\xe6\x1c\xaa\xc06|\x82\xa8D#\xb3\x9e\xef\xb4S\xbe': False,
    b'\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~ #\xba\x9a\x8d\xd6/z\xdd\xe2\xcfO\xa4P^\xe3\xe8\x9b/\xdbT|\xd1F\x0c5\x86\xa0\xfb\xda\x96.': False,
    b'\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~ $\x0f\x0e\xb6\xa1"\x93\x9f\xf6b\xf9\x04\xc7 \xb4\x98eB\xea\xaa\xafm\xd0t\x98!\x8d$\x98=\x0f': False,
}

if __name__ == "__main__":
    test_basics()