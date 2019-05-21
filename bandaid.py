from __future__ import print_function
import csv
from pylab import *
import ipywidgets as widgets
from ipywidgets import *
from IPython.display import display
from bandaid_gui import bandaid_app

def project_exec(inputs):
    #grab html input from textboxes and send to code
    # import cgi
    # form = cgi.FieldStorage()
    # searchterm =  form.getvalue('searchbox')
    #NEED TO PUT RELATIVE OS PATH IN HERE
    #HARD CODED TO MY COMPUTER NEEDS TO CHANGE BEFORE DISTRIBUTION
    #'/Users/baldy/Documents/GitHub/CFDauto/long_radius.csv'
    with open('/Users/baldy/Documents/GitHub/CFDauto/long_radius.csv') as csvfile:
        info_data=csv.reader(csvfile, delimiter=' ', quotechar='|')
        reader=csv.DictReader(csvfile)
        name=[]; vel=[]; flow=[]
        for row in reader:
            name.append(row['filename'])
            vel.append(row['flow_velocity'])
            flow.append(row['flow_model'])
    input_names=[]; slurm_names=[]; master_names=[]
    for i in range(len(name)):
        input_names.append(str(name[i])+'_input'+'.in')
        slurm_names.append(str(name[i])+'_slurm'+'.txt')
        #master_names.append=str(name[i])+'_master'+'.txt'
    for i in range(len(name)):
        # input_path='/Users/baldy/Documents/GitHub/CFDauto/input_files/'+input_names[i]
        # slurm_path='/Users/baldy/Documents/GitHub/CFDauto/slurm_files/'+slurm_names[i]
        input_path='/Users/baldy/Documents/GitHub/CFDauto/input_files/'+input_names[i]
        slurm_path='/Users/baldy/Documents/GitHub/CFDauto/slurm_files/'+slurm_names[i]
        f=open(input_path,'w')
        f.close()
        f=open(slurm_path,'w')
        f.close()
    #CSV reader that will read in values for gui objects if gui is broken USE GUI IF AT ALL POSSIBLE
    #to use this cell uncomment it and do not put values into gui objects
    # with open('/Users/baldy/Documents/GitHub/CFDauto/alt_gui.csv') as csvfile:
    #     info_data=csv.reader(csvfile, delimiter=' ',quotechar='|')
    #     reader=csv.DictReader(csvfile)
    #     list=[]
    #     for row in reader:
    #         list.append(row['input'])
    #work_dir.value=list[0]; base_case.value=list[1]; work_home.value=list[2]; inlet_name.value=list[3]
    #inlet_bc.value=list[4]; inlet_options.value=list[5]; outlet_name.value=list[6]; outlet_bc.value=list[7]
    #outlet_options.value=list[8]; conv_crit.value=list[9]; num_iter.value=list[10]
    # work_dir=str(list[0])
    # base_case=str(list[1])
    # work_home=str(list[2])
    # inlet_name=str(list[3])
    # inlet_bc=str(list[4])
    # inlet_options=str(list[5])
    # outlet_name=str(list[6])
    # outlet_bc=str(list[7])
    # outlet_options=str(list[8])
    # conv_crit=str(list[9])
    # num_iter=str(list[10])

    # get input from GUI fields
    work_dir = inputs['work_dir']
    base_case = inputs['base_case']
    nodes = inputs['nodes']
    cores = inputs['cores']
    work_home = inputs['work_home']
    inlet_name = inputs['inlet_name']
    inlet_bc = inputs['inlet_bc']
    inlet_options = inputs['inlet_geo']
    outlet_name = inputs['outlet_name']
    outlet_bc = inputs['outlet_bc']
    outlet_options = inputs['outlet_geo']
    conv_crit = inputs['conv_crit']
    num_iter = inputs['iterations']

    script=[]
    write_case=[]
    monitor=[]
    write_data=[]

    option=inlet_options.value.split("vel")
    read_file='/file/read-case /home/'+work_home+'/'+work_dir+'/'+base_case
    initialize='/solve/initialize/hyb-initialization'
    solve='/solve/iterate '+num_iter+'\n/parallel/timer/usage'
    for i in range(len(flow)):
        if flow[i]=='laminar':
            v=str(vel[i])
            n=str(name[i])
            lam_part_1='y y n '
            lam_part_2=' n 0 y n 0 n 0 n 1'
            inlet1='/define/models/viscous/laminar? yes \n/define/boundary-conditions/'+inlet_bc.value+' '+inlet_name.value+' '+lam_part_1+str(v)+lam_part_2
            #n n y y n '+v+' n 0'
            inlet2='\n/define/boundary-conditions/'+outlet_bc+' '+ outlet_name+' '+outlet_options
            case='/file/write-case /home/'+work_home+'/'+work_dir+'/'+str(n)+'.cas'
            data='/file/write-data /home/'+work_home+'/'+work_dir+'/'+str(n)+'.dat \n/file/confirm-overwrite y'
            mon='/solve/monitors/residual/convergence-criteria '+conv_crit+' '+conv_crit+' '+conv_crit+' '+conv_crit
            monitor.append(mon)
            write_case.append(case)
            write_data.append(data)
            script.append(inlet1+inlet2)
        elif flow[i]=='turbulent':
            v=str(vel[i])
            n=str(name[i])
            turb_part_1='y y n '
            turb_part_2=' n 0 y n 1 n 0 n 0 y n 1 n 1'
            inlet1='/define/models/viscous/ke-standard? yes \n/define/boundary-conditions/'+inlet_bc+' '+inlet_name+' '+turb_part_1 +str(v)+turb_part_2
            inlet2='\n/define/boundary-conditions/'+outlet_bc+' '+ outlet_name+' '+outlet_options
            case='/file/write-case /home/'+work_home+'/'+work_dir+'/'+str(n)+'.cas'
            data='/file/write-data /home/'+work_home+'/'+work_dir+'/'+str(n)+'.dat \n/file/confirm-overwrite y'
            mon='/solve/monitors/residual/convergence-criteria '+conv_crit+' '+conv_crit+' '+conv_crit+' '+conv_crit+' '+conv_crit+' '+conv_crit
            monitor.append(mon)
            write_case.append(case)
            write_data.append(data)
            script.append(inlet1+inlet2)
        else:
            v=str(vel[i])
            n=str(name[i])
            turb_part_1='stop'
            turb_part_2='stop'
            inlet1='stop'
            inlet2='pls stop'
            case='no really, please stop'
            data='sigh'
            mon='STOP'
            monitor.append(mon)
            write_case.append(case)
            write_data.append(data)
            script.append(inlet1+inlet2)
#dummy values for text box input
    node=3; task=19;total=node*task
    input_names=[]; slurm_names=[]; master_names=[]
    for i in range(len(name)):
        input_names.append(str(name[i])+'_input'+'.in')
        slurm_names.append(str(name[i])+'_slurm'+'.txt')
        #master_names.append=str(name[i])+'_master'+'.txt'
    for i in range(len(name)):
        #create input file for each individual run in ANSYS
        input_path='/Users/baldy/Documents/GitHub/CFDauto/input_files/'+input_names[i]
        slurm_path='/Users/baldy/Documents/GitHub/CFDauto/slurm_files/'+slurm_names[i]
        f=open(input_path,'w')
        f.write(read_file); f.write('\n'); f.write(script[i]); f.write('\n')
        f.write(monitor[i]); f.write('\n'); f.write(initialize); f.write('\n')
        f.write(solve); f.write('\n'); f.write(write_case[i]); f.write('\n')
        f.write(write_data[i]); f.write('\n') 
        f.close()
        #write slurm file for each ANSYS run
        #Needs to reference "input_path.in" files generated previously
        f=open(slurm_path,'w')
        f.write('#!/bin/bash \n \n#SBATCH --job-name='+name[i]+'\n')
        f.write('#SBATCH -o '+name[i]+'.out \n#SBATCH -p nodes \n')
        f.write('#SBATCH -e '+name[i]+'_error.out \n#SBATCH -t 12:00:00 \n')
        #create text input for these values to be input later
        f.write('SBATCH -n '+str(node)+' --tasks-per-node='+str(task)+'\n\n')
        f.write('#-- name of input file \n#\n   TEST='+name[i]+'\n \n')
        f.write('#-- environment \n# \n#  source /usr/share/modules/init/csh \n#  module load ansys/14.0 \n \n')
        f.write('#-- move to submission directory \n#-- pipe.in and pipe.cas must be in submission directory \n#  cd $PBS_O_WORKDIR \n \n')
        #need to modify '-t57' so that it is multiplication of node and task values
        f.write('#-- run test \n# \n/ansys_inc/v161/fluent/bin/fluent 3ddp -g -t'+str(total)+' -mpi=pcmpi -pib -i $TEST.in \n \n')
        f.write('#-- exit \n# \n   unset echo')
        f.close()
    master_path='/Users/baldy/Documents/GitHub/CFDauto/master_files/fluent_master.txt'
    check=len(name)-1
    f=open(master_path,'w')
    f.write('#!/bin/bash \n \n')
    for i in range(len(name)):
        if i<check:
            f.write('sbatch '+str(slurm_names[i])+'\nwait \n')
        else:
            f.write(str(slurm_names[i])+'\nwait \nexit 1')
    f.close()
    return


#project_exec()

# any function passed to the bandaid_app constructor will be bound to the submit button click event
# just be sure that the function passed to it takes an argument for the GUI inputs
# example: def project_exec(inputs): yadayadayada
app = bandaid_app(project_exec)
app.mainloop()
