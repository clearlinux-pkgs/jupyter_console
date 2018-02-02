#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyter_console
Version  : 5.2.0
Release  : 13
URL      : http://pypi.debian.net/jupyter_console/jupyter_console-5.2.0.tar.gz
Source0  : http://pypi.debian.net/jupyter_console/jupyter_console-5.2.0.tar.gz
Summary  : Jupyter terminal console
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: jupyter_console-bin
Requires: jupyter_console-python3
Requires: jupyter_console-python
Requires: Sphinx
Requires: ipython
Requires: jupyter_client
Requires: jupyter_core
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
# Jupyter Console
[![Build Status](https://travis-ci.org/jupyter/jupyter_console.svg?branch=master)](https://travis-ci.org/jupyter/jupyter_console)
[![Documentation Status](http://readthedocs.org/projects/jupyter-console/badge/?version=latest)](https://jupyter-console.readthedocs.io/en/latest/?badge=latest)

%package bin
Summary: bin components for the jupyter_console package.
Group: Binaries

%description bin
bin components for the jupyter_console package.


%package python
Summary: python components for the jupyter_console package.
Group: Default
Requires: jupyter_console-python3

%description python
python components for the jupyter_console package.


%package python3
Summary: python3 components for the jupyter_console package.
Group: Default
Requires: python3-core

%description python3
python3 components for the jupyter_console package.


%prep
%setup -q -n jupyter_console-5.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507155688
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-console

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
