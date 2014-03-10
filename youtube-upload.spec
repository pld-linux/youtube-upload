Summary:	Upload videos to Youtube from the command-line
Name:		youtube-upload
Version:	0.7.3
Release:	1
License:	GPL v3
Group:		Applications/System
Source0:	https://youtube-upload.googlecode.com/files/%{name}-%{version}.tgz
# Source0-md5:	e667962d4a41a936dc6dafdff5c594e9
URL:		https://code.google.com/p/youtube-upload/
BuildRequires:	python-gdata
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-gdata
Requires:	python-progressbar
Requires:	python-pycurl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Upload videos to Youtube from the command-line.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/youtube-upload
%{py_sitescriptdir}/youtube_upload
%{py_sitescriptdir}/youtube_upload-%{version}-py*.egg-info
