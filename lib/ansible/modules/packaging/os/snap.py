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
    package:
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


def _get_channel_args(channel):
    if channel is None:
        return []
    if channel == 'stable':
        return ['--stable']
    if channel == 'candidate':
        return ['--candidate']
    if channel == 'beta':
        return ['--beta']
    if channel == 'edge':
        return ['--edge']
    assert 'Invalid channel {}'.format(channel)


def _get_mode_args(mode):
    if mode is None:
        return []
    if mode == 'classic':
        return ['--classic']
    if mode == 'jailmode':
        return ['--jailmode']
    if mode == 'devmode':
        return ['--devmode']
    assert 'Invalid mode {}'.format(mode)


def main():
    argument_spec = dict(
        package=dict(default=None, type='string'),
        state=dict(default='present', choices=['absent', 'present']),
        channel=dict(default=None, choices=['stable', 'candidate', 'beta', 'edge']),
        mode=dict(default=None, choices=['devmode', 'jailmode', 'classic'])
    )

    module = AnsibleModule(
        argument_spec=argument_spec
    )

    package = module.params['package']

    if package:
        state = module.params['state'] or 'present'
        if state == 'present':
            command = ['snap', 'install', package]
            command.extend(_get_channel_args(module.params['channel']))
            command.extend(_get_mode_args(module.params['mode']))
            rc, out, err = module.run_command(command)

        elif state == 'absent':
            pass

        else:
            assert 'Invalid state {}'.format(state)
    else:
        pass


if __name__ == '__main__':
    main()
