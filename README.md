## Introduction

This project is an example for a python command-line application structure with a unit testing framework

## Prerequirements

* [nose](http://somethingaboutorange.com/mrl/projects/nose/1.0.0/)

### Installation on OSX

        sudo port install py26-nose

In the case of **"Error: The following dependencies were not installed: py26-distribute"** first run

        sudo port -f activate py26-distribute

## Testing

        nosetests

## Running the Application

        bin/project [arguments]
