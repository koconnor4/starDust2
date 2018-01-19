#!/bin/sh
#SBATCH --jobname=SNClassification
#SBATCH --output job%j.out
#SBATCH --error job%j.err
#SBATCH -p all
#SBATCH -n 20
#SBATCH -N 1

source /share/apps/Modules/3.2.10/init/modules.sh
module load python/anaconda2.3

#python /home/bradley/Documents/sncosmo/myOwnClassifyTest.py
