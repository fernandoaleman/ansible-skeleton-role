# Ansible Skeleton Role

The ansible skeleton role is a template for creating Ansible roles. It provides
a basic structure and common files needed to get started with an Ansible role.

## Requirements

- `ansible-galaxy` command line tool
- Python 3.x

## Usage

Clone repo

```shell
git clone git@github.com:fernandoaleman/ansible_skeleton_role.git ~/.ansible/skeleton_role
```

Create new role

```shell
ansible-galaxy init --role-skeleton=~/.ansible/skeleton_role <role_name>
```
