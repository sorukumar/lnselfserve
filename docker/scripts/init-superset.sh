#!/bin/bash
superset db upgrade
superset init
superset run -h 0.0.0.0 -p 8088 --with-threads --reload --debugger
