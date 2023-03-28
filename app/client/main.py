# -*- coding: utf-8 -*-

import ipaddress
import socket, click 
from app.utils.constant import (
    UTF,
    IA,
    SAY_SOMETHING,
    ENTER_SERVER_IP,
    CONNECTION_ERROR,
    CONNECTION_IMPOSSIBLE,
    DASHED,
    PORT,
    ADDRESS_NOT_VALID
)   

from app.utils.verify_env import _check_env_file
from app.base import Base_CGPT

def main():
    
    adresse_ip = click.prompt(ENTER_SERVER_IP)

    try:

        ipaddress.IPv4Address(adresse_ip)
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:

            s.connect((adresse_ip, int(PORT)))
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

        except OSError as e: 

            if e.errno == 113:
                click.echo(CONNECTION_IMPOSSIBLE)
            else:
                click.echo(CONNECTION_ERROR, e)

        finally:

            s.close()

    except ipaddress.AddressValueError: 

        click.echo(ADDRESS_NOT_VALID)

if __name__ == '__main__':
    main()