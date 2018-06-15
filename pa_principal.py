import os
import sys
from pa_getter import getter
from pa_parser import parser
from pa_getter_detail import getter_detail
from pa_parser_detail import parser_detail

if len(sys.argv) < 2:
    print("""Missing category parameter\n> python pa_principal.py category""")
    exit(-1)

resultsfolder = sys.argv[1]


# Que resultsfolder se lea por parametro de entrada sys.arg[1]

# Creacion carpetas
# os.sys
def get_pa(category):
    dir = os.path.join("data/",resultsfolder)
    print(dir)
    dir_getter = os.path.join(dir,"getter")
    print(dir_getter)
    dir_getter_detail = os.path.join(dir,"getter_detail")
    print(dir_getter_detail)
    if not os.path.exists(dir):
        os.makedirs(dir,mode=0o777)
        os.makedirs(dir_getter,mode=0o0777) 
        os.makedirs(dir_getter_detail, mode=0o777) 

# Llamar a los programas
##
    getter(resultsfolder)
    parser(resultsfolder)
    getter_detail(resultsfolder)
    parser_detail(resultsfolder)

get_pa(resultsfolder)
