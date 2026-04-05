#!/bin/sh

BASEDIR=$(dirname "$0")
cd $BASEDIR
echo "Running init.sh"
find $BASEDIR -type f \( -not -name 'db.sqlite3'  -not -name '*.pyc' -not -name '*.tmp' -not -name '*.html' -not -name 0001_initial.py -o -name 'models.py' \)  -exec md5sum {} \; > /tmp/sum
sum=`cat /tmp/sum`

cd $BASEDIR
pip install -U pip
pip install -r requirements.txt

# rm -f db.sqlite3 */migrations/0*
./manage.py makemigrations
./manage.py migrate
# ./manage.py shell -c "from django.contrib.auth.models import User;user=User.objects.create_user('targuan', password='monster');user.is_superuser=True;user.is_staff=True;user.save()"
# echo "loading data"
# ./manage.py loaddata initdata.json
echo "running server"
./manage.py runserver 0.0.0.0:5000 &
echo "watching for change"
while true
do  
    find $BASEDIR -type f \( -not -name 'db.sqlite3' -not -name '*.pyc' -not -name '*.tmp' -not -name '*.html' -not -name 0001_initial.py -o -name 'models.py' \)  -exec md5sum {} \; > /tmp/current_sum
    current_sum=`cat /tmp/current_sum`
    if [ "$sum" = "$current_sum" ]
    then
        sleep 5
    else
        echo "Change detected, restarting:"
        diff /tmp/sum /tmp/current_sum
        kill $!
        dt=$(date '+%Y-%m-%d-%H:%M:%S');
        ./manage.py dumpdata > initdata-${dt}.json
        exec $BASEDIR/init.sh
    fi
done;