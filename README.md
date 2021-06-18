# GNU SASL Library

**GNU SASL** is an implementation of the Simple Authentication and Security Layer framework and a few common SASL mechanisms. SASL is used by network servers (e.g., IMAP, SMTP, XMPP) to request authentication from clients, and in clients to authenticate against servers.

GNU SASL consists of a C library (libgsasl), a command-line application (gsasl), and a manual. The library supports the ANONYMOUS, CRAM-MD5, DIGEST-MD5, EXTERNAL, GS2-KRB5, GSSAPI, LOGIN, NTLM, OPENID20, PLAIN, SCRAM-SHA-1, SCRAM-SHA-1-PLUS, SCRAM-SHA-256, SCRAM-SHA-256-PLUS, SAML20, and SECURID mechanisms.

The library is portable because it does not do network communication by itself, but rather leaves it up to the calling application. The library is flexible with regards to the authorization infrastructure used, as it utilizes callbacks into the application to decide whether an user is authorized or not. 

## How it works

1. Get source from [src.fedoraproject.org](https://src.fedoraproject.org/rpms/libgsasl).
2. Write last commit SHA from [src.fedoraproject.org](https://src.fedoraproject.org/rpms/libgsasl) to [CHANGELOG](CHANGELOG).
3. Modify & update source (and `*.spec`).
4. Build SRPM & RPM.
