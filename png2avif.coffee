#!/usr/bin/env coffee

sharp = require('sharp')

do =>
  await sharp("./out/example-60004.png").toFile("./out/example-60004.avif")
  process.exit()
