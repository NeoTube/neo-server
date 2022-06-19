{
  description = "Dev Shell For NeoTube Server";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-22.05";
    flake-utils.url = "github:numtide/flake-utils/master";
    devshell.url = "github:numtide/devshell/master";
  };
  outputs = { self, nixpkgs, flake-utils, devshell }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          overlays = [ devshell.overlay ];
        };

      in {
        devShell = pkgs.devshell.mkShell {
          name = "neotube-server-dev-shell";
          packages = with pkgs; [ python310 poetry nodePackages.pyright alejandra rnix-lsp ];
	  devshell.startup.setup_poetry_dependencies.text = "${pkgs.poetry}/bin/poetry install";
	  devshell.startup.setup_poetry_python_version.text = "${pkgs.poetry}/bin/poetry env use ${pkgs.python310}/bin/python";
	  commands = [
            {
              name = "run_server";
              category = "server";
              command =
                "${pkgs.poetry}/bin/poetry run python -m  neo_server";
            }
	];
        };
      });
}
