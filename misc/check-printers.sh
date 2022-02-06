#!/bin/bash
user=$(cat credentials | jq -r '.user');
pass=$(cat credentials | jq -r '.pass');
urls=$(cat credentials | jq -r '.nolop_urls[]');

for url in ${urls}; do
  if [ $# -gt 0 ]; then
    if [[ ${url} != *${1}* ]]; then
      continue
    fi
  fi
  cookie=${url#"https://"}
  cookie=${cookie%"/"}
  if [ -f "$cookie.cookie" ]; then
    continue;
  fi
  curl -H "Content-Type: application/json" "$url/api/login" -d "{\"user\":\"$user\", \"pass\":\"$pass\", \"remember\":true}" --cookie-jar "$cookie.cookie";
done;

for url in ${urls}; do
  if [ $# -gt 0 ]; then
    if [[ ${url} != *${1}* ]]; then
      continue
    fi
  fi
  cookie=${url#"https://"}
  cookie=${cookie%"/"}
  ret=$(curl -s "$url/api/job" --cookie "$cookie.cookie");
  echo $url;
  echo $ret | jq -r '.state';
  echo "$(echo $ret | jq -r '.progress.completion')%";
  left=$(echo $ret | jq -r '.progress.printTimeLeft');
  echo "$(echo "scale=2 ; $left / 60" | bc) minutes left.";
  echo;
done;