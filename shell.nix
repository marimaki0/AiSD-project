{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python3
    pkgs.python3Packages.numpy
    pkgs.python3Packages.matplotlib
    pkgs.python3Packages.networkx
    pkgs.zlib
  ];
}

