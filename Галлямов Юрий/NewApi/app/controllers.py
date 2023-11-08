from app.Model.ConversationModel import Conversation
from app.Model.MessageUserModel import MessageUser
from app.Model.CompositionOfTheConversationModel import CompositionOfTheConversation
from app.Model.UserModel import User
from app.Model.database import db
from flask import jsonify



def get_users():
    users = User.query.all()
    user_data = []

    for user in users:
        user_info = {
            "login": user.Login_User,
            "fio": user.FIO_User,
            "avatar": user.Avatar_User,
            "status": user.Status_User,
            "role": user.Role
        }
        user_data.append(user_info)

    return jsonify({"users": user_data})

def get_conversation(login):
    conversations = (
        db.session.query(
            Conversation.ID_Conversation,
            Conversation.Title_Conversation,
            Conversation.Date_Of_Creation,
            Conversation.Login_Creator,
            Conversation.Type_Conversation,
            Conversation.Avatar
        )
        .join(
            CompositionOfTheConversation,
            Conversation.ID_Conversation == CompositionOfTheConversation.ID_Conversation
        )
        .filter(CompositionOfTheConversation.Login_Contacts == login)
        .all()
    )

    conversation_data = []

    for conversation in conversations:
        conversation_info = {
            "ID_Conversation": conversation[0],
            "Title_Conversation": conversation[1],
            "Date_Of_Creation": conversation[2].strftime("%d.%m.%Y"),
            "Login_Creator": conversation[3],
            "Type_Conversation": conversation[4],
            "Avatar": conversation[5]
        }
        conversation_data.append(conversation_info)

    return jsonify({"code":200,"result": conversation_data})

def get_message(id_conversation):
    message = (
        db.session.query(
            MessageUser.IdMessage,
            MessageUser.Message_content,
            MessageUser.ID_Conversation,
            MessageUser.Login_Sender,
            MessageUser.StatusRead,
            MessageUser.DateSender,
            User.FIO_User,
            Conversation.Avatar
        )
        .join(User, MessageUser.Login_Sender == User.Login_User)
        .join(Conversation, MessageUser.ID_Conversation == Conversation.ID_Conversation)
        .filter(MessageUser.ID_Conversation == id_conversation)
        .all()
    )

    message_list = []

    for message in message:
        message_dict = {
            "IdMessage": message[0],
            "Message_content": message[1],
            "ID_Conversation": message[2],
            "Login_Sender": message[3],
            "StatusRead": message[4],
            "DateSender": message[5].strftime("%d.%m.%Y %H:%M"),
            "Name_Sender": message[6],
            "Avatar": message[7],
        }
        message_list.append(message_dict)

    return jsonify({"code": 200, "result": message_list})

def logAuth(login, password):
    user = User.query.filter(User.Login_User == login and User.Password == password)
    if user is None:
        return jsonify({"code":405, "message":"Login is error"})

    # login_user(user)
    return jsonify({"code":200, "message":"Login is succsed"})
# Пример функции для добавления пользователя
# def add_user(login, password, fio, avatar, status, role):
#     new_user = User(login=login, password=password, fio=fio, avatar=avatar, status=status, role=role)
#     db.session.add(new_user)
#     db.session.commit()


