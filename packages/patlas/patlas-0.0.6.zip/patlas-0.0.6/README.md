[![image](https://img.shields.io/pypi/v/patlas.svg)](https://pypi.python.org/pypi/patlas)
[![Build](https://github.com/aforren1/patlas/workflows/Build/badge.svg?branch=main)](https://github.com/aforren1/patlas/actions/workflows/build.yml)

A simple, runtime-dependency-free texture atlas packer.

Basic usage:

```python
from patlas import AtlasPacker, load
from glob import glob

ap = AtlasPacker(side=2048, pad=2)
ap.pack(glob('images/*.png')) # list of images
ap.pack(['images/image.jpg']) # can call multiple times (packing quality may suffer)

ap.atlas # memoryview of RGBA texture
ap.metadata # dictionary of image locations and image format

ap.save('atlas') # serialize as custom .patlas file

atlas, metadata = load('atlas.patlas')
```

See [demo.py](https://github.com/aforren1/patlas/blob/main/demo.py) for example usage with [ModernGL](https://github.com/moderngl/moderngl).

Features/limitations:

 - Uses `stb_image`, `stb_rect_pack`, and `stb_dxt` from [stb](https://github.com/nothings/stb)
   - Can import any image format `stb_image` can (see [here](https://github.com/nothings/stb/blob/5ba0baaa269b3fd681828e0e3b3ac0f1472eaf40/stb_image.h#L23))
 - Only square RGBA textures (currently)
 - Optional DXT5/BC3(?) compression
 - Optional OpenMP support (disabled by default to reduce wheel size) can substantially reduce runtime. To enable, build from source with `OMP=1` set in the environment, e.g. `OMP=1 pip install patlas --no-binary patlas`
   - On Windows, should "just work"?
   - MacOS may need extra packages, e.g. `libomp` from brew
   - Linux may need extra packages, e.g. `libomp-dev` on Ubuntu
 - Save to a custom `.patlas` file
   - Uses [qoi](https://qoiformat.org/) image format + zlib for fast and small encoding/decoding
   - See the [save](https://github.com/aforren1/patlas/blob/main/patlas.pyx) method of `AtlasPacker` for gory details
 - Includes a command-line utility (see `patlas --help` for details)
 - Requires Cython at build time (but source distribution should have pre-generated `.c` files)
