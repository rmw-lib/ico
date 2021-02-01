#!/usr/bin/env coffee

sharp = require('sharp')
fs = require 'fs'

do =>
  [png] = process.argv[2..]
  await sharp(png).resize(104,149,{
    withoutEnlargement:true
  }).avif({quality:75,speed:0}).toFile(png[...-3]+"avif")
  fs.unlinkSync png
  process.exit()
