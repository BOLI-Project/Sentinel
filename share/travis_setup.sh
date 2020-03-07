#!/bin/bash
set -evx

mkdir ~/.Bolivarcoin

# safety check
if [ ! -f ~/.Bolivarcoin/Bolivarcoin.conf ]; then
  cp share/Bolivarcoin.conf.example ~/.muncore/Bolivarcoin.conf
fi
