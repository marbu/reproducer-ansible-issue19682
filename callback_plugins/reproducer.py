# -*- coding: utf-8 -*-

# Copyright 2016 Martin Bukatovič <martin.bukatovic@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


from ansible.plugins.callback import CallbackBase
from ansible import constants as C


class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_NAME = 'reproducer'
    CALLBACK_NEEDS_WHITELIST = False

    def __init__(self):
        super(CallbackModule, self).__init__()
        print("*** callback: init")

    #
    # start callbacks
    #

    def v2_playbook_on_start(self, playbook):
        print("*** callback: on_start")

    def v2_playbook_on_play_start(self, play):
        print("*** callback: on_play_start")

    def v2_playbook_on_task_start(self, task, is_conditional):
        print("*** callback: on_task_start")

    def v2_playbook_on_handler_task_start(self, task):
        print("*** callback: on_handler_task_start")

    def v2_playbook_on_cleanup_task_start(self, task):
        print("*** callback: on_handler_cleanup_start")
