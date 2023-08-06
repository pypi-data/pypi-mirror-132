"""Ansible utilities for clickable"""

__version__ = "1.4"

import itertools
import json
import locale
import logging
import os
import os.path
import pprint
import re
import shlex
import subprocess
from shlex import quote

import click
import six
import yaml

from clickable.utils import PathResolver
from clickable.virtualenv import virtualenv
import clickable.coloredlogs


clickable.coloredlogs.bootstrap()


logger = logging.getLogger('stdout.clickable')


def _configure(ctx):
    logger.info("Install ansible-galaxy roles in dependencies/galaxy-roles/")
    virtualenv(ctx.obj['path_resolver'], ctx.obj['ansible']['virtualenv'])
    virtualenv_path = ctx_get(ctx, 'virtualenv_path')
    env = dict(os.environ)
    env["ANSIBLE_COLLECTIONS_PATHS"] = "dependencies/galaxy-collections/"
    env["ANSIBLE_ROLES_PATH"] = "dependencies/galaxy-roles/"
    logger.info("Install ansible-galaxy collections in dependencies/galaxy-collections/")
    subprocess.check_call(_vcommand(virtualenv_path, 'ansible-galaxy',
                  'install',
                  '--force',
                  '-r', 'dependencies/requirements.yml'),
                  env=env)


def _vault_secure_yaml(ctx):
    import subprocess
    vault_file = 'inventory/group_vars/all/secure.yml'
    command = _ovh_vault_command(ctx, 'view', vault_file)
    yaml_content = subprocess.check_output(command)
    secure = yaml.safe_load(yaml_content)
    return secure


def _vault_action_file(ctx, action, vault_file):
    import subprocess
    command = _ovh_vault_command(ctx, action, vault_file)
    yaml_content = subprocess.check_output(command)
    print(yaml_content)


def run_playbook(ctx, playbook=None,
                 ask_become_pass=False, ask_vault_pass=False,
                 check=False, diff=False,
                 verbose=False, tags=None, limit=[],
                 extra_vars=[], extra_args=[]):
    args = [playbook]
    if ask_become_pass:
        args.append('--ask-become-pass')
    if ask_vault_pass:
        args.append('--ask-vault-pass')
    if diff:
        args.append('--diff')
    if check:
        args.append('--check')
    if verbose:
        if isinstance(verbose, six.integer_types):
            args.append('-' + ('v' * verbose))
        else:
            args.append('-v')
    if tags:
        args.extend(['--tags', tags])
    if limit:
        args.extend(['-l', ','.join(limit)])
    if extra_vars:
        for extra_var in extra_vars:
            args.extend(['-e', extra_var])
    if extra_args:
        for extra_arg in extra_args:
            args.append(extra_arg)
    command = ['ansible-playbook'] + args
    run_interactive(ctx, 'ansible-playbook', args, verbose)


def run_interactive(ctx, command, args, print_command):
    virtualenv_path = ctx_get(ctx, 'virtualenv_path')
    environ = {}
    environ['PATH'] = \
        os.path.join(virtualenv_path, 'bin') + ':' + os.environ['PATH']
    environ['ANSIBLE_CONFIG'] = 'inventory/ansible.cfg'
    if os.path.exists('.vault_pass.txt'):
        environ['ANSIBLE_VAULT_PASSWORD_FILE'] = '.vault_pass.txt'
        ask_vault_pass = False
    os.environ.update(environ)
    if print_command:
        environ = ' '.join(['{}={}'.format(key, quote(value)) for key, value in environ.items()])
        all_args = [os.path.join(virtualenv_path, 'bin', command)] + args
        all_command = ' '.join([quote(i) for i in all_args])
        logger.info('running: {} {}'.format(environ, all_command))
    subprocess.check_call(_vcommand(virtualenv_path, command, *args))


def run_ansible_module(ctx, host, module, module_args,
                       ansible_user=None, inventory=None,
                       become=False, become_user='root',
                       ask_become_pass=False, ask_vault_pass=False,
                       check=False, diff=False,
                       verbose=False, extra_vars=None, extra_args=None):
    args = []
    args.append(host)
    args.append('-m')
    args.append(module)
    if module_args:
        args.append('-a')
        args.append(module_args)
    if ansible_user:
        args.append('-U')
        args.append(ansible_user)
    if inventory:
        args.append('-i')
        args.append(','.join(inventory))
    if ask_become_pass:
        args.append('--ask-become-pass')
    if ask_vault_pass:
        args.append('--ask-vault-pass')
    if diff:
        args.append('--diff')
    if check:
        args.append('--check')
    if become:
        args.append('--become')
    if become_user:
        args.append('--become-user')
        args.append(become_user)
    if verbose:
        if isinstance(verbose, six.integer_types):
            args.append('-' + ('v' * verbose))
        else:
            args.append('-v')
    if extra_vars:
        for extra_var in extra_vars:
            args.extend(['-e', extra_var])
    if extra_args:
        for extra_arg in extra_args:
            args.append(extra_arg)
    run_interactive(ctx, 'ansible', args, verbose)


def run(ctx, playbook=None,
        ask_become_pass=False, ask_vault_pass=False,
        check=False, diff=False,
        verbose=False, tags=None, ansible_args=''):
    _configure(ctx)
    run_playbook(ctx, playbook, ask_become_pass=ask_become_pass,
                 ask_vault_pass=ask_vault_pass,
                 check=check, diff=diff, verbose=verbose,
                 tags=tags, ansible_args=ansible_args)


def run_playbook_task(click_group, name, playbook, static_extra_vars=[],
        static_extra_args=[], decorators=[], help=None, short_help=None,
        common_hosts=False):
    @click.pass_context
    @click.argument('extra-args', nargs=-1)
    @click.option('--ask-become-pass', '-K', default=False, is_flag=True)
    @click.option('--ask-vault-pass', default=False, is_flag=True)
    @click.option('--check', '-C', default=False, is_flag=True)
    @click.option('--diff', '-D', default=False, is_flag=True)
    @click.option('-v', '--verbose', count=True)
    @click.option('-l', '--limit', default=[], multiple=True)
    @click.option('--tags', '-t', default=[], multiple=True)
    @click.option('--extra-vars', '-e', default=[], multiple=True)
    @decorate(decorators)
    def inside_run(ctx,
                   ask_become_pass, ask_vault_pass,
                   check, diff, verbose,
                   tags, limit, extra_vars, extra_args):
        merged_vars = list(static_extra_vars)
        merged_vars.extend(extra_vars)
        _configure(ctx)
        if common_hosts:
            merged_vars.append('{}={}'.format('common_hosts', common_hosts))
        else:
            merged_vars.append('{}={}'.format('common_hosts', 'all'))
        
        # command-line or statically supplied ansible-playbook command line
        # arguments
        merged_extra_args = []
        if extra_args:
            merged_extra_args.extend(extra_args)
        if static_extra_args:
            merged_extra_args.extend(static_extra_args)
        run_playbook(ctx, playbook, ask_become_pass=ask_become_pass,
                     ask_vault_pass=ask_vault_pass, check=check,
                     diff=diff, verbose=verbose, tags=','.join(tags),
                     limit=limit,
                     extra_vars=merged_vars,
                     extra_args=extra_args)
    return click_group.command(name, help=help, short_help=short_help)(inside_run)


def run_module_task(click_group, name, static_args='',
        static_extra_vars=[], static_extra_args=[], decorators=[]):
    """
    static_args: static args for module
    static_extra_args: static args for ansible command
    """
    @click.pass_context
    @click.argument('host')
    @click.argument('extra-args', nargs=-1)
    @click.option('--module-name', '-m', help='module name')
    @click.option('--become', '-b',
                  default=False, help='use become', is_flag=True)
    @click.option('--become-user', default='root', help='become user')
    @click.option('--args', '-a', help='module arguments')
    @click.option('--user', '-u')
    @click.option('--inventory', '-i', default=[], multiple=True)
    @click.option('--ask-become-pass', '-K', default=False)
    @click.option('--ask-vault-pass', default=False)
    @click.option('--check', '-C', default=False, is_flag=True)
    @click.option('--diff', '-D', default=False, is_flag=True)
    @click.option('-v', '--verbose', count=True)
    @click.option('--extra-vars', '-e', default=[], multiple=True)
    @decorate(decorators)
    def inside_run(ctx, host, module_name, user, args, inventory,
                   become, become_user, ask_become_pass, ask_vault_pass,
                   check, diff, verbose,
                   extra_vars, extra_args):
        merged_vars = list(static_extra_vars)
        merged_vars.extend(extra_vars)
        # module args, combination of command-line supplied and statically
        # supplied arguments (mainly key=value pairs)
        merged_args = []
        if static_args:
            merged_args.append(static_args)
        if args:
            merged_args.append(args)

        # ansible command args, command-line supplied or statically-supplied
        merged_extra_args = []
        if extra_args:
            merged_extra_args.extend(extra_args)
        if static_extra_args:
            merged_extra_args.extend(static_extra_args)

        _configure(ctx)
        run_ansible_module(ctx, host, module_name,
                           ' '.join(merged_args) if merged_args else '',
                           become=become, become_user=become_user,
                           ansible_user=user, inventory=inventory,
                           ask_become_pass=ask_become_pass,
                           ask_vault_pass=ask_vault_pass, check=check,
                           diff=diff, verbose=verbose,
                           extra_vars=extra_vars, extra_args=extra_args)
    return click_group.command(name)(inside_run)


def decorate(decorators):
    """
    Decorate with a list of decorators
    """
    def decorator(f):
        if decorators:
            for decorator in reversed(decorators):
                f = decorator(f)
        return f
    return decorator


def kwargs_to_extra_vars(*names):
    """
    Handle click provided arguments by their names, and add them to
    ansible extra_vars keyword argument.
    """
    def decorator(f):
        def wrapper(*args, **kwargs):
            # get already existing extra_vars list
            # or initiate a new one
            extra_vars = kwargs['extra_vars']
            if not extra_vars:
                extra_vars = []
            if type(extra_vars) is tuple:
                extra_vars = list(extra_vars)
            kwargs['extra_vars'] = extra_vars
            new_kwargs = dict(kwargs)
            for name in names:
                value = new_kwargs.pop(name)
                if value:
                    if isinstance(value, six.string_types):
                        extra_vars.append('{}={}'.format(name, value))
                    else:
                        extra_vars.append('{}={}'.format(name, json.dumps(value)))
            return f(*args, **new_kwargs)
        return wrapper
    return decorator


def _vcommand(virtualenv_path, command, *args):
    cl = []
    cl.append(os.path.join(virtualenv_path, 'bin', command))
    cl.extend(args)
    return cl


def ctx_get(ctx, key, default=Exception):
    if key in ctx.obj:
        return ctx.obj[key]
    else:
        if default is Exception:
            raise Exception('{} not found in ctx.obj'.format(key))
        else:
            return default
