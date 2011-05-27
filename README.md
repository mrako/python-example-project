## Introduction

This project is an example for a python command-line application structure with a unit testing framework

## Prerequirements

* [nose](http://somethingaboutorange.com/mrl/projects/nose/1.0.0/)

### Installation on OSX

#### Using macports
        sudo port install py26-nose

In the case of **"Error: The following dependencies were not installed: py26-distribute"** first run

        sudo port -f activate py26-distribute

### Installation on *nix platforms (including OSX)
#### Using easy_install

	sudo easy_install nose

#### Using pip
	
	sudo pip install nose 

## Running the Application

        bin/project [arguments]

## Testing

        nosetests
