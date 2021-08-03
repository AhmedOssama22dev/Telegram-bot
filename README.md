# Telegram-bot
This is a simple telegram bot @sessionNotifierBot that can be used by an instructor to :
  -start sessions and let students get notified to their telegram channel https://t.me/joinchat/y7-YwLkEs7E2NzQ0
  -Get students data 
  -Search student and get his details
  
Since this is a test version:  PASSWORD: mybot

All requests are calling the API i developed and deployed to heroku : https://tele-bot-back-end.herokuapp.com/
    <h4>some useful endpoints:</h4>
    <a href="https://tele-bot-back-end.herokuapp.com/students/"
      >GET all students
    </a><br>
    <a href="https://tele-bot-back-end.herokuapp.com/students/id"
      >GET student by id
    </a><br>
    <a href="https://tele-bot-back-end.herokuapp.com/sessions/"
      >GET all sessions
    </a><br>
    <a href="https://tele-bot-back-end.herokuapp.com/create/session/"
      >POST New session
    </a>
