%global release_prefix          102

Name:                           libgsasl
Version:                        1.10.0
Release:                        %{release_prefix}%{?dist}
Summary:                        GNU SASL library
License:                        LGPLv2+
URL:                            https://www.gnu.org/software/gsasl/
Vendor:                         Package Store <https://pkgstore.github.io>
Packager:                       Kitsune Solar <kitsune.solar@gmail.com>

Source0:                        https://ftp.gnu.org/gnu/gsasl/%{name}-%{version}.tar.gz
Source1:                        https://ftp.gnu.org/gnu/gsasl/%{name}-%{version}.tar.gz.sig

BuildRequires:                  gcc
BuildRequires:                  krb5-devel
BuildRequires:                  libgcrypt-devel
BuildRequires:                  libidn-devel
BuildRequires:                  libntlm-devel
BuildRequires:                  pkgconfig
BuildRequires:                  make

%description
The library includes support for the SASL framework
and at least partial support for the CRAM-MD5, EXTERNAL,
GSSAPI, ANONYMOUS, PLAIN, SECURID, DIGEST-MD5, LOGIN,
and NTLM mechanisms.

# -------------------------------------------------------------------------------------------------------------------- #
# Package: devel
# -------------------------------------------------------------------------------------------------------------------- #

%package devel
Summary:                        Development files for %{name}
Requires:                       %{name}%{?_isa} = %{version}-%{release}
Requires:                       pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%prep
%autosetup


%build
%configure --disable-static --disable-rpath --with-gssapi-impl=mit
%{make_build}


%install
%{make_install}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%{find_lang} %{name}

%ldconfig_scriptlets


%files -f %{name}.lang
%doc AUTHORS NEWS README THANKS
%license COPYING COPYING.LIB
%{_libdir}/libgsasl.so.*


%files devel
%license COPYING COPYING.LIB
%{_includedir}/gsasl*
%{_libdir}/libgsasl.so
%{_libdir}/pkgconfig/libgsasl.pc


%changelog
* Fri Jun 18 2021 Package Store <kitsune.solar@gmail.com> - 1:1.10.0-102
- UPD: Add "Vendor" & "Packager" fields.

* Fri Jun 18 2021 Package Store <kitsune.solar@gmail.com> - 1:1.10.0-101
- UPD: New build for latest changes.

* Thu Jun 17 2021 Package Store <kitsune.solar@gmail.com> - 1:1.10.0-100
- UPD: Move to GitHub.
- UPD: License.

* Sat Apr  3 2021 Peter Lemenkov <lemenkov@gmail.com> - 1.10.0-1
- Ver. 1.10.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 13 2020 Package Store <kitsune.solar@gmail.com> - 1.8.1-100
- NEW: v1.8.1.

* Wed Oct 16 2019 Package Store <kitsune.solar@gmail.com> - 1.8.0-100
- UPD: MARKETPLACE.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Kevin Fenzi <kevin@scrye.com> - 1.8.0 -13
- Rebuilt for new libidn.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 23 2016 Paul Belanger <pabelanger@redhat.com> - 1.8.0-7
- Re-enable GSSAPI support (#1134957, #1246177)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Aug 19 2012 Tom Callaway <spot@fedoraproject.org> - 1.8.0-1
- update to 1.8.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 28 2012 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.6.1-1
- New upstream release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Apr 16 2011 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.6.0-2
- Remove clean section, since it's no longer required
- Use '{buildroot}' instead of 'RPM_BUILD_ROOT'

* Fri Apr 15 2011 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.6.0-1
- New upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 12 2010 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.4.0-6
- Just bump the release to avoid an E-V-R bug

* Tue Jan 12 2010 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.4.0-1
- New upstream

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 1 2009 Nikolay Vladimirov <nikolay@vladimiroff.com> - 0.2.29-1
- Rewrite to use poll instead of select.
- Don't use poll with POLLOUT to avoid busy-waiting.

* Tue Jul 29 2008 Nikolay Vladimirov <nikolay@vladimiroff.com> - 0.2.27-1
- new upstream release 0.2.27

* Tue Jun 3 2008 Nikolay Vladimirov <nikolay@vladimiroff.com> - 0.2.26-1
- new upstream release 0.2.26

* Sat Mar 29 2008 Nikolay Vladimirov <nikolay@vladimiroff.com> - 0.2.25-1
- new upstream release

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.18-6
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Nikolay Vladimirov <nikolat@vladimiroff.com> - 0.2.18-5
- rebuild for ppc32 selinux fix

* Thu Aug 2 2007 Nikolay Vladimirov <nikolat@vladimiroff.com> - 0.2.18-4
- License tag changed

* Tue Jun 26 2007 Nikolay Vladimirov <nikolay@vladimiroff.com> - 0.2.18-3
- added NTLM support

* Fri Jun 22 2007 Nikolay Vladimirov <nikolay@vladimiroff.com> - 0.2.18-2
- fixed mixed-use-of-spaces-and-tabs
- fixed timestamps for header files
- edited summary

* Thu Jun 21 2007 Nikolay Vladimirov <nikolay@vladimiroff.com> - 0.2.18-1
- initial release
