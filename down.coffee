#!/usr/bin/env coffee

fs = require 'fs'

do =>
  n = 0
  while ++n <= 100000
    url = "https://www.thiswaifudoesnotexist.net/example-#{n}.jpg"
    dir = n % 100
    outdir = "in/#{dir}"
    fs.mkdirSync(outdir,recursive:true)
    fs.mkdirSync("out/#{dir}",recursive:true)

    console.log "wget #{url} -O #{outdir}/#{n}.jpg &"
    if n % 10 == 0
      console.log "sleep 5"

