#!/bin/bash

db_set() {
echo "$1, $2" >> database
}

db_get() {
var=$(grep "^$1, " database | tail -n 1 | sed 's/^[0-9]*, *//g')
if [ "$var" = "#Thombstone" ]
then
    echo "DELETED"
else
    echo $var
fi
}

db_delete() {
echo "$1, #Thombstone" >> database | echo 'Deleted'
}

db_compact() {
declare -A db
input="/Users/aleksandr/dev_dao/tech_sessions/20200220_bashdb/database"
while IFS= read -r line
do
  id="$(cut -d',' -f1 <<<"$line")"
  val="$(cut -d' ' -f2 <<<"$line")"
  db[$id]="$val"
done < "$input"


for x in ${!db[@]}; do
  if [ "${db[${x}]}" != "#Thombstone" ]
    then echo "${x}, ${db[${x}]}" >> database_tmp
  fi
done

mv database_tmp database
}
