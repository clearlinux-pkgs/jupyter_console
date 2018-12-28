#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyter_console
Version  : 6.0.0
Release  : 24
URL      : https://files.pythonhosted.org/packages/92/c8/b7e768a3dec19b09d8ad5296a479e03c19a741a1bb4abab27c09236b8562/jupyter_console-6.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/92/c8/b7e768a3dec19b09d8ad5296a479e03c19a741a1bb4abab27c09236b8562/jupyter_console-6.0.0.tar.gz
Summary  : Jupyter terminal console
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: jupyter_console-bin = %{version}-%{release}
Requires: jupyter_console-license = %{version}-%{release}
Requires: jupyter_console-python = %{version}-%{release}
Requires: jupyter_console-python3 = %{version}-%{release}
Requires: Sphinx
Requires: ipython
Requires: jupyter_client
Requires: jupyter_core
BuildRequires : buildreq-distutils3

%description
# Jupyter Console
[![Build Status](https://travis-ci.org/jupyter/jupyter_console.svg?branch=master)](https://travis-ci.org/jupyter/jupyter_console)
[![Documentation Status](http://readthedocs.org/projects/jupyter-console/badge/?version=latest)](https://jupyter-console.readthedocs.io/en/latest/?badge=latest)

%package bin
Summary: bin components for the jupyter_console package.
Group: Binaries
Requires: jupyter_console-license = %{version}-%{release}

%description bin
bin components for the jupyter_console package.


%package license
Summary: license components for the jupyter_console package.
Group: Default

%description license
license components for the jupyter_console package.


%package python
Summary: python components for the jupyter_console package.
Group: Default
Requires: jupyter_console-python3 = %{version}-%{release}

%description python
python components for the jupyter_console package.


%package python3
Summary: python3 components for the jupyter_console package.
Group: Default
Requires: python3-core

%description python3
python3 components for the jupyter_console package.


%prep
%setup -q -n jupyter_console-6.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541267162
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jupyter_console
cp COPYING.md %{buildroot}/usr/share/package-licenses/jupyter_console/COPYING.md
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-console

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jupyter_console/COPYING.md

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
