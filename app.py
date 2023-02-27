# from flask import Flask, request, session
# from twilio.twiml.messaging_response import MessagingResponse
# from GlotBot import ask, append_interaction_to_chat_log

# app = Flask(__name__)
# # if for some reason your conversation with the bot gets weird, change the secret key 
# app.config['SECRET_KEY'] = '89djhff9lhkd93'

# @app.route('/GlotBot', methods=['POST'])
# def glotbot():
#     incoming_msg = request.values['Body']

    
#     chat_log = session.get('chat_log')
#     answer = ask(incoming_msg, chat_log)
#     session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
#                                                          chat_log)
#     msg = MessagingResponse()
#     msg.message(answer)
#     return str(msg)

# if __name__ == '__main__':
#     app.run(debug=True)


# new start - updation of app.py
from flask import Flask, request, session, jsonify
from GlotBot import ask, append_interaction_to_chat_log

app = Flask(__name__)
# if for some reason your conversation with the bot gets weird, change the secret key 
app.config['SECRET_KEY'] = '89djhff9lhkd93'

@app.route('/GlotBot', methods=['POST'])
def glotbot():
    incoming_data = request.get_json()

    incoming_msg = incoming_data.get('message')
    chat_log = session.get('chat_log')

    answer = ask(incoming_msg, chat_log)

    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer, chat_log)

    return jsonify({'message': answer})

if __name__ == '__main__':
    app.run(debug=True)


# new start - updation of GlotBot.py + app.py
# from dotenv import load_dotenv
# from random import choice
# from flask import Flask, request
# import os
# import openai
# from dotenv import load_dotenv

# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")
# completion = openai.Completion()

# start_sequence = "\nPerson: "
# restart_sequence = "\nGlotBot: "
# session_prompt = ""

# app = Flask(__name__)

# @app.route('/chatbot', methods=['POST'])
# def chatbot():
#     incoming_msg = request.json['message']
#     chat_log = request.json.get('chat_log', session_prompt)

#     answer = ask(incoming_msg, chat_log)
#     updated_chat_log = append_interaction_to_chat_log(incoming_msg, answer, chat_log)

#     return {'message': answer, 'chat_log': updated_chat_log}

# def ask(question, chat_log=None):
#     prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=prompt_text,
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     story = response['choices'][0]['text']
#     return str(story)

# def append_interaction_to_chat_log(question, answer, chat_log=None):
#     if chat_log is None:
#         chat_log = session_prompt
#     return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'

# if __name__ == '__main__':
#     app.run(debug=True)
