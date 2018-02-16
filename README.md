Boilerplate docker-compose scaffold for personal projects. Grep for "boilerplate" to match your setup.

Typically gets expanded with application servers, workers, queues and what have you.

### web

Runs a standard nginx with `/web/default.conf` as its config, serving from `/web/www`.

#### letsencrypt

The supplied `cert.pem` and `key.pem` are self-signed for localhost. The `default.conf` config shares the `certbot_challenge` directory which allows for manual-mode certbot actions, such as

 sudo certbot --manual --agree-tos -d yourdomain certonly

This will pause and ask you to place a nonce in a nonce-named file reachable as `http://yourdomain/.well-known/acme-challenge/nonce-named-file`. You can create this file in `certbot_challenge/.well-known/acme-challenge/` and continue with certbot. When it finishes, you can overwrite `cert.pem` with the resulting `fullchain.pem`, and `key.pem` with `privkey.pem`, both from whereever certbot placed them (likely `/etc/letscenrypt/live/yourdomain/`), and `docker-compose restart web`.

### db

Runs a standard MySQL as UTF-8 as possible, with:
* `/env` containing the auth credentials.
* `/db/content/` as its `/var/lib/mysql`.
* `/db/backups/` where it saved/loads its backups (see *backups* below).
* `/db/entrypoint/` where it looks for first-run SQL and shell scripts (see MySQL docker docs).
* `/env` containing the auth credentials.

#### backups

`/scripts/db_backup.sh` dumps the MySQL contents to a timestamped file in `/db/backups/`, and returns the full path to it for your cronning pleasure. **TODO** `mysql` prints a warning first, so tail the output.

`/scripts/db_restore.sh` takes a backup's filename (which you need to place in `/db/backups/` first) and reloads the database from that.