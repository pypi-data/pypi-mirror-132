# certbot-dns-innovativity

An Authenticator plugin for Certbot DNS-01 ACME that uses Innovativity's DNS Manager module.

## Overview

[Innovativity](https://innovativity.io) is a cloud/devops consulting company based in Italy. We offer many
IT-related services to our customers, including a centralized panel for ACME DNS authentication for multiple
providers (CloudFlare, DigitalOcean, Hetzner, and more).

This package is currently meant for Innovativity customers, although plans are on the way to opensource the whole
project.

The API called by this authenticator provides a way to create/delete DNS ACME challenges. The API verifies the
credentials and their permission on the requested domain/subdomain and creates a TXT record on success for a
DNS-01 challenge. The cleanup allows deletion of that record only.
This provides more granularity of most providers' API tokens, such as CloudFlare's Zone Token or DigitalOcean's API Key.


## Installation

Install using pip:

```
pip install certbot-dns-innovativity
```


## Usage

Create a credentials file with strict permissions:

```
touch ~/.secrets/certbot/innovativity.ini
chmod 600 ~/.secrets/certbot/innovativity.ini
```

Configure API url and token:

```ini
# DNS Manager credentials used by Certbot
dns_innovativity_dashboard_url = http://localhost:8000/
dns_innovativity_api_token = 1234567890asdfghjkl1234567890asdfghjkl
```

The path to this file can be provided interactively or using the `--dns-innovativity-credentials` command-line argument.

This file will be used again by Certbot during renewal, so it shouldn't be deleted nor moved without changing renew configurations.

To acquire a new certificate, run:

```
certbot certonly \
   --authenticator dns-innovativity \
   --dns-innovativity-credentials ~/.secrets/certbot/innovativity.ini \
   -d domain.example.com
```
