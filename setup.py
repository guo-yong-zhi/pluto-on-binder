import setuptools

setuptools.setup(
  name="jupyter-pluto-proxy",
  # py_modules rather than packages, since we only have 1 file
  py_modules=['plutoserver'],
  entry_points={
      'jupyter_serverproxy_servers': [
          # name = packagename:function_name
          'pluto = plutoserver:setup_plutoserver',
      ]
  },
  install_requires=['jupyter-server-proxy @ git+http://github.com/fonsp/jupyter-server-proxy@3a58aa5005f942d0c208eab9a480f6ab171142ef'],
)

import os
cmd = """wget https://github.com/google/fonts/archive/main.tar.gz -O gf.tar.gz && \
  tar -xf gf.tar.gz && \
  mkdir -p ~/.fonts/truetype/google-fonts && \
  find $PWD/fonts-main/ -name "*.ttf" -exec install -m644 {} ~/.fonts/truetype/google-fonts/ \; || return 1 && \
  rm -f gf.tar.gz && \
  # Remove the extracted fonts directory
  rm -rf $PWD/fonts-main && \
  # Remove the following line if you're installing more applications after this RUN command and you have errors while installing them
  rm -rf /var/cache/* && \
  fc-cache -f"""
os.system(cmd)
