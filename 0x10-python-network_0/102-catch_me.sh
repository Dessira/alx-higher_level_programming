#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me rcieves response You got me!
curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
