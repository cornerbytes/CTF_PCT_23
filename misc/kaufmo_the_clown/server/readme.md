compile static binary

`nimble c -d:release --opt:speed --passL:-static --dynlibOverride:libmain.a main.nim`
