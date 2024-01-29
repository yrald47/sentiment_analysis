from kbbi import KBBI
import json
import sys

kata = sys.argv[1]
deskripsi = KBBI(kata)
print(deskripsi)
kode = json.dumps(deskripsi.serialisasi()['entri'][0]['makna'][0]['kelas'][0]['kode'])
print(json.dumps(len(deskripsi.serialisasi()['entri'][0]['makna'])))
print(kode)