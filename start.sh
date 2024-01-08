. colors.sh
jobName=app_sport.py
echo "${YELLOW}check $jobName pid ${NOCOLOR}"
echo "ps aux | grep "$jobName" | grep -v grep | awk '{print $2}'"
TAILPID=`ps aux | grep "$jobName" | grep -v grep | awk '{print $2}'`
if [[ "0$TAILPID" != "0" ]]; then
    echo "${RED}kill process $TAILPID${NOCOLOR}"
    sudo kill -9 $TAILPID
fi

echo "${RED}python $jobName ${NOCOLOR}"

nohup python $jobName > /dev/null 2>&1 &
