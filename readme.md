###Genral instructions 

###install node and react dependencies 
\jitFin\npm i

###Django model migrations and run server 
\jitFin\jitTransaction> python manage.py makemigrations jit
\jitFin\jitTransaction> python manage.py migrate
\jitFin\jitTransaction> python manage.py runserver


reach react page on localhost:8000/

###APIS 
curl --location --request GET 'http://localhost:8000/api/trans/' \
--data-raw ''


curl --location --request POST 'http://localhost:8000/api/trans/' \
--header 'Content-Type: application/json' \
--data-raw '{
     "transactionDate" :"2019-07-09",
    "description" :"fuel",
    "category" :2,
    "amount" :10322.22

}'


