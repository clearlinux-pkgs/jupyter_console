#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyter_console
Version  : 6.4.0
Release  : 48
URL      : https://files.pythonhosted.org/packages/75/c7/5e585e703a2fbc56c529b982bdd4bfedd47a4737e11093c58df7e6c7216e/jupyter_console-6.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/75/c7/5e585e703a2fbc56c529b982bdd4bfedd47a4737e11093c58df7e6c7216e/jupyter_console-6.4.0.tar.gz
Summary  : Jupyter terminal console
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: jupyter_console-bin = %{version}-%{release}
Requires: jupyter_console-license = %{version}-%{release}
Requires: jupyter_console-python = %{version}-%{release}
Requires: jupyter_console-python3 = %{version}-%{release}
Requires: Pygments
Requires: ipykernel
Requires: ipython
Requires: jupyter_client
Requires: pexpect
Requires: prompt_toolkit
BuildRequires : Pygments
BuildRequires : buildreq-distutils3
BuildRequires : ipykernel
BuildRequires : ipython
BuildRequires : jupyter_client
BuildRequires : pexpect
BuildRequires : prompt_toolkit

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
Provides: pypi(jupyter_console)
Requires: pypi(ipykernel)
Requires: pypi(ipython)
Requires: pypi(jupyter_client)
Requires: pypi(prompt_toolkit)
Requires: pypi(pygments)

%description python3
python3 components for the jupyter_console package.


%prep
%setup -q -n jupyter_console-6.4.0
cd %{_builddir}/jupyter_console-6.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635745359
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jupyter_console
cp %{_builddir}/jupyter_console-6.4.0/COPYING.md %{buildroot}/usr/share/package-licenses/jupyter_console/4864371bd27fe802d84990e2a5ee0d60bb29e944
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
/usr/share/package-licenses/jupyter_console/4864371bd27fe802d84990e2a5ee0d60bb29e944

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
