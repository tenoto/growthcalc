#!/bin/bash 

echo "#######################"
echo "#     GROWTH CALC     #"
echo "#######################"

export PATH_GROWTHCALC=$(pwd)
export PATH=$PATH_GROWTHCALC/growthcalc/cli:$PATH
export PYTHONPATH=$PATH_GROWTHCALC:$PYTHONPATH