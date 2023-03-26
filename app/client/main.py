# -*- coding: utf-8 -*-

import socket, click 
from app.utils.constant import (
    UTF,
    IA,
    SAY_SOMETHING,
    ENTER_SERVER_IP,
    CONNECTION_LOST,
    CONNECTION_IMPOSSIBLE,
    DASHED
)   

from app.utils.verify_env import _check_env_file
from app.base import Base_CGPT


def main():
    
    adresse_ip = click.prompt(ENTER_SERVER_IP)
    port = 2048
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:

        s.connect((adresse_ip,port))
        Base_CGPT._void_func = _check_env_file

        cgpt = Base_CGPT(
            exit_key="q",
            modify_api_key="m",
            input_text=SAY_SOMETHING,
            decoration=DASHED,
            encode=UTF,
            icon_ans=IA,
            socket_resp=True,
            socket_instance=s

        )

        cgpt.infinite_loop()
   
    except BrokenPipeError:
        click.echo(CONNECTION_LOST)
    
    except socket.gaierror:
        click.echo(CONNECTION_IMPOSSIBLE)

    finally:
        # close the connection
        s.close()
 
if __name__ == '__main__':
    main()