# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Rsync(AutotoolsPackage):
    """An open source utility that provides fast incremental file transfer."""
    homepage = "https://rsync.samba.org"
    url      = "https://download.samba.org/pub/rsync/src/rsync-3.1.2.tar.gz"

    version('3.2.3', sha256='becc3c504ceea499f4167a260040ccf4d9f2ef9499ad5683c179a697146ce50e')
    version('3.2.2', sha256='644bd3841779507665211fd7db8359c8a10670c57e305b4aab61b4e40037afa8')
    version('3.1.3', '1581a588fde9d89f6bc6201e8129afaf')
    version('3.1.2', '0f758d7e000c0f7f7d3792610fad70cb')
    version('3.1.1', '43bd6676f0b404326eee2d63be3cdcfe')

    depends_on('zlib')
    depends_on('popt')
    depends_on('openssl', when='@3.2:')
    depends_on('xxhash', when='@3.2:')
    depends_on('zstd', when='@3.2:')
    depends_on('lz4', when='@3.2:')

    
    def configure_args(self):
        return ['--with-included-zlib=no']
                                            
