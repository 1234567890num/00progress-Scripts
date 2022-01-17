def breakfile():
    import struct
    f = open('00progress.bin/00progress.bin','rb').read()
    for i in range(f[4]):
        name = f[0x10*i+0x14:0x10*i+0x18]
        name = name.decode()
        name = name.replace('\x00', '')
        g = open('00progress.bin/'+name+'.bin','wb')
        offset = struct.unpack('I',f[0x10*i+0x18:0x10*i+0x1C])[0]
        length = struct.unpack('I',f[0x10*i+0x1C:0x10*i+0x20])[0]
        g.write(f[offset:offset+length])
        g.close()

breakfile()
