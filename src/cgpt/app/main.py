# -*- coding: utf-8 -*-

from cgpt.app.utils.constant import SAY_SOMETHING, DASHED, UTF, IA

from cgpt.app.base import Base_CGPT


def prompt() -> None:
    cgpt = Base_CGPT(
        exit_key="q",
        modify_api_key="m",
        input_text=SAY_SOMETHING,
        decoration=DASHED,
        encode=UTF,
        icon_ans=IA,
        socket_resp=False,
        socket_instance=None,
    )

    cgpt.infinite_loop()
