# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPyyaml(PythonPackage):
    """PyYAML is a YAML parser and emitter for Python."""
    homepage = "http://pyyaml.org/wiki/PyYAML"
    url      = "http://pyyaml.org/download/pyyaml/PyYAML-3.11.tar.gz"

    version('5.3.1', sha256='b8eac752c5e14d3eca0e6dd9199cd627518cb5ec06add0de9d32baeee6fe645d')
    version('5.3',   sha256='e9f45bd5b92c7974e59bcd2dcc8631a6b6cc380a904725fce7bc08872e691615')
    version('5.2',   sha256='c0ee8eca2c582d29c3c2ec6e2c4f703d1b7f1fb10bc72317355a746057e7346c')
    version('5.1.2', sha256='01adf0b6c6f61bd11af6e10ca52b7d4057dd0be0343eb9283c878cf3af56aee4')
    version('5.1.1', sha256='b4bb4d3f5e232425e25dda21c070ce05168a786ac9eda43768ab7f3ac2770955')
    version('5.1',   sha256='436bc774ecf7c103814098159fbb84c2715d25980175292c648f2da143909f95')
    version('3.13',  sha256='3ef3092145e9b70e3ddd2c7ad59bdd0252a94dfe3949721633e41344de00a6bf')                        
    version('3.12', '4c129761b661d181ebf7ff4eb2d79950')
    version('3.11', 'f50e08ef0fe55178479d3a618efe21db')
