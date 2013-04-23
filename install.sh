#! /bin/bash

#-----------------------------------------------------------------------
#Copyright 2013 Centrum Wiskunde & Informatica, Amsterdam
#
#Author: Daniel M. Pelt
#Contact: D.M.Pelt@cwi.nl
#Website: http://dmpelt.github.io/pyastratoolbox/
#
#
#This file is part of the Python interface to the
#All Scale Tomographic Reconstruction Antwerp Toolbox ("ASTRA Toolbox").
#
#The Python interface to the ASTRA Toolbox is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#The Python interface to the ASTRA Toolbox is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with the Python interface to the ASTRA Toolbox. If not, see <http://www.gnu.org/licenses/>.
#
#-----------------------------------------------------------------------

function printHelp {
	echo "install.sh: Installs Python interface to the ASTRA-toolbox"
	echo 
	echo "Usage: ./install.sh [-i astra_include_path] [-l astra_library_path] [-p python_executable_path] [-c cuda_path]"
	echo
	echo -e "\t-i astra_include_path:\t\tspecify path to astra header files (without trailing astra/) (Optional)"
	echo -e "\t-l astra_library_path:\t\tspecify parent path of astra library file (Optional)"
	echo -e "\t-p python_executable_path:\tspecify path to python executable (Optional)"
	echo -e "\t-c cuda_path:\t\t\tpath to CUDA (Optional)"
	echo -e "\t-h:\t\t\t\tprint this help (Optional)"
	exit 1
}


CINFLAGS=""
LINFLAGS=""
PEX=python
while getopts ":i:l:p:c:" opt; do
  case $opt in
    h)
      printHelp
      ;;
    i)
      CINFLAGS="${CINFLAGS} -I${OPTARG}"
      ;;
    l)
      LINFLAGS="${LINFLAGS} -L${OPTARG}"
      ;;
    c)
      LINFLAGS="${LINFLAGS} -DASTRA_CUDA -L${OPTARG}/lib"
      CINFLAGS="${CINFLAGS} -DASTRA_CUDA -I${OPTARG}/include"
      ;;
    p)
      PEX=${OPTARG}
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      printHelp
      ;;
  esac
done

if [ -d build ]
then
	echo "Previous build found!"
	echo "Remove it before rebuilding (recommended)?"
	pushd build > /dev/null
	BUILDPATH=`pwd`
	popd > /dev/null
	read -p "Remove $BUILDPATH (y/n/q)?" choice
	case "$choice" in 
	  q|Q ) 
		exit 1
		;;
	  y|Y ) 
		rm -r build
		;;
	  n|N ) 
		;;
	  * ) 
		echo "Invalid choice, quitting..."
		exit 1
		;;
	esac
fi

CPPFLAGS=${CINFLAGS} LDFLAGS=${LINFLAGS} $PEX builder.py install
