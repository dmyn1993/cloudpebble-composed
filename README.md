Cloudpebble Composed
====================

This repo contains the key components of CloudPebble. It also contains a `docker-compose` file
that will assemble all of them into something that runs like a real CloudPebble instance.

Getting Started
---------------

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Mac, Windows),
   or otherwise get docker and docker-compose into a working state (Linux).
2. `git clone https://github.com/dmyn1993/cloudpebble-composed.git && cd cloudpebble-composed`
3. `./dev_setup.sh` (this will take a while)
4. edit `/etc/hosts`, add `127.0.0.1 host.docker.internal`
5. `docker compose up`
6. Register a local account at http://your_ip_address/accounts/register/
7. Login with local account at http://your_ip_address/accounts/login/ (you have to login when the docker restarts)

At the end of this, you will have seven Docker containers running. The CloudPebble-specific ones
should pick up most changes without being rebuilt, although in some cases you may have to stop and
restart them (re-run `docker-compose up`).

Limitations
-----------

- Pebble SSO is not available; only local accounts work.
- Websocket installs are not available because pebble SSO is not available

Credits:
A special thanks to https://www.reddit.com/r/pebble/comments/bza6yq/how_to_get_cloudpebble_working_on_a_local_computer/
