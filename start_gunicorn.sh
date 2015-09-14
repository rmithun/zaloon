APPNAME=onepass
APPDIR=/home/jawahar/zaloon/zaloon_dev/
PROJDIR=/home/jawahar/zaloon/zaloon_dev/zaloon



LOGFILE=$PROJDIR'gunicorn.log'
ERRORFILE=$PROJDIR'gunicorn-error.log'
 
NUM_WORKERS=3
 
ADDRESS=127.0.0.1:8000
 
#source ~/.bashrc
#workon $APPNAME
 
#exec /home/balance/Project/bin/gunicorn $APPNAME.wsgi:application 
exec ../bin/gunicorn $APPNAME.wsgi:application \
-w $NUM_WORKERS --bind=$ADDRESS \
--log-level=debug \
--log-file=$LOGFILE
