#!/usr/bin/env bash
createuser redcap_django --interactive
createdb -O redcap_django redcap_django
psql -d redcap_django -c "ALTER USER redcap_django WITH PASSWORD 'qwer1234'"
