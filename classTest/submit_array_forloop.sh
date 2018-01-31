#!/bin/sh

#SBATCH -p all
#SBATCH --job-name="run_etc_array_forloop"
#SBATCH --output=/home/rodneysa/runetc/slurm.output/simsed%A-%a.out
#SBATCH --error=/home/rodneysa/runetc/slurm.output/simsed%A-%a.err
#SBATCH -N 1
#SBATCH -n 20
#SBATCH --array=0-30

source /share/apps/Modules/3.2.10/init/sh
module load python/anaconda2.3

for i in {0..999}
  do 
     echo --MAG_FILE=/home/rodneysa/runetc/sedsim.output/wfirst_simsed.`printf "%03d" ${SLURM_ARRAY_TASK_ID}``printf "%03d" ${i}`.dat >> /home/rodneysa/runetc/slurm_commands.txt
  done

#python /home/rodneysa/src/subarupfsETC/run_etc.py @/home/rodneysa/runetc/wfirst_subarupfsetc.1hr.defaults  --MAG_FILE=/home/rodneysa/runetc/sedsim.output/wfirst_simsed.`printf "%03d" ${SLURM_ARRAY_TASK_ID}``printf "%03d" ${i}`.dat  --OUTFILE_SNC=/home/rodneysa/runetc/etc.output/subaruPFS_SNR.1hr.`printf "%03d" ${SLURM_ARRAY_TASK_ID}``printf "%03d" ${i}`.dat
#python /home/rodneysa/src/subarupfsETC/run_etc.py @/home/rodneysa/runetc/wfirst_subarupfsetc.5hr.defaults  --MAG_FILE=/home/rodneysa/runetc/sedsim.output/wfirst_simsed.`printf "%03d" ${SLURM_ARRAY_TASK_ID}``printf "%03d" ${i}`.dat  --OUTFILE_SNC=/home/rodneysa/runetc/etc.output/subaruPFS_SNR.5hr.`printf "%03d" ${SLURM_ARRAY_TASK_ID}``printf "%03d" ${i}`.dat
#python /home/rodneysa/src/subarupfsETC/run_etc.py @/home/rodneysa/runetc/wfirst_subarupfsetc.10hr.defaults --MAG_FILE=/home/rodneysa/runetc/sedsim.output/wfirst_simsed.`printf "%03d" ${SLURM_ARRAY_TASK_ID}``printf "%03d" ${i}`.dat --OUTFILE_SNC=/home/rodneysa/runetc/etc.output/subaruPFS_SNR.10hr.`printf "%03d" ${SLURM_ARRAY_TASK_ID}``printf "%03d" ${i}`.dat
#python /home/rodneysa/src/subarupfsETC/run_etc.py @/home/rodneysa/runetc/wfirst_subarupfsetc.40hr.defaults --MAG_FILE=/home/rodneysa/runetc/sedsim.output/wfirst_simsed.`printf "%03d" ${SLURM_ARRAY_TASK_ID}``printf "%03d" ${i}`.dat --OUTFILE_SNC=/home/rodneysa/runetc/etc.output/subaruPFS_SNR.40hr.`printf "%03d" ${SLURM_ARRAY_TASK_ID}``printf "%03d" ${i}`.dat
