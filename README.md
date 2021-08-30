# Ellipsoid ML

This repository for the logic that extracts geographically information from text, usually article titles and summaries. 
Users should invoke the functions via gRPC calls. 

## Protos

The protos are stored in the [ellipsoid_protos](https://github.com/sauleanf/ellipsoid_protos/) repository and included as a git 
submodule

## Commands

| Command | Description |
| --- | ----------- |
| `script/generate.sh` | Generates the gRPC code based on the protos |
