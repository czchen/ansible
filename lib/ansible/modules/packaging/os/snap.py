#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017 ChangZhuo Chen (陳昌倬) <czchen@czchen.org>
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.


DOCUMENTATION = '''
module: snap
short_description: Manages snap packages
description:
    -   Manages snaps, which is universal Linux packages.
options:
    name:
        description:
            -
        required: false
        default: null
    state:
        description:
            -
        required: false
        default: present
        choices: [ "absent", "present" ]
    channel:
        description:
            -
        required: false
        default: null
        choices: [ "stable", "candidate", "beta", "edge" ]
    mode:
        description:
            -
        required: false
        default: null
        choices: [ "devmode", "jailmode", "classic" ]
'''


from ansible.module_utils.basic import AnsibleModule


def main():
    argument_spec = dict(
        name=dict(default=None, type='string'),
        state=dict(default='present', choices=['absent', 'present']),
        channel=dict(default=None, choices=['stable', 'candidate', 'beta', 'edge']),
        mode=dict(default=None, choices=['devmode', 'jailmode', 'classic'])
    )

    module = AnsibleModule(
        argument_spec=argument_spec
    )


if __name__ == '__main__':
    main()
