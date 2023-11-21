import os
import std/strutils
proc main =
  let FLAG = getenv("FLAG")
  echo("> ayo bantu kaufmo mencari pintu keluar")
  echo("> bantu kaufmo untuk mencari kata sandi yang digunakan")
  stdout.write("masukkan kata sandi : ")
  stdout.flushFile()

  var user_input: string = readLine(stdin)
  user_input = user_input.replace("kaufmo", "")  # filter bad input

  if user_input == "kaufmo":
    echo("ini flag mu : ", FLAG, " dan terima kasih telah membantu kaufmo!")
  elif user_input == "cheat":
    echo("gak boleh cheat. https://www.youtube.com/watch?v=Y29XTh59F2g")
  else:
    echo("kata sandi yang kamu masukkan : ", user_input)
    echo("kata sandi salah")

when isMainModule:
  main()
