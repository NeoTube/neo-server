# CONTRIBUTING

1. Fork the repository (https://github.com/neotube/neo-server/fork).
2. Clone the fork locally
```bash
git clone git@github.com:my_awsm_username/neo-server
cd neo-server
```

## Installing dependencies

- Using poetry
```bash
poetry install && poetry shell
```
- Using nix
```bash
nix develop
```

Note: In Nix devshell env, use `run_server` to run the server.
