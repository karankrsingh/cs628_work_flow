## Running Locally

```bash
git clone https://github.com/sibtc/simple-file-upload.git
```

```bash
pip install -r requirements.txt
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

For home page http://127.0.0.1:8000/
there are two veiw:

1.. Teacher's view:
Here will be list of all students under him. Just click on roll number or name to move to respective students detail.

In every page there are 5 components:

a. Techer can see past meetings details which contains when meeting scheduled and what work expected, then student report in that meeting and what grades were given on basis of report

b. Next scheduled meeting which tells only the schedule and work expected

c. For evaluation which contains reports which are ready to be evaluated

d. Schedule next meeting

e. See graphical view of students progress by week vs marks graph

2.. Students' view: 
Here will be list of weeks for each student on clicking he can see whether meeting is scheduled. He can see previous history's as well and upload report for next meeting.

Please see the mysqlite database to see the table and populate accordingly.

Note: Since javascript is fetched online so please keep internet running.