from app.Model.UserModel import User, Conversation
from app.Model.CompositionOfTheConversationModel import CompositionOfTheConversation
from flask import jsonify
from app import app
from app.Model.database import * 
from flask import request, Blueprint
from sqlalchemy import case, func
from sqlalchemy.orm import aliased

conversation_bp = Blueprint('Conversation', __name__)

@conversation_bp.route("/conversation", methods=['GET'])
def get_conversation():
    login = request.args.get('login')
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

    return jsonify(
        {
            "code": 200,
            "result": conversation_data
        }
    )

@conversation_bp.route("/conversationMember", methods=['GET'])
def get_conversation_member():
    id_conversation = request.args.get("conversationId")

    query = db.session.query(
        CompositionOfTheConversation.Login_Contacts,
        User.FIO_User,
        User.Avatar_User,
        case(
            (CompositionOfTheConversation.Login_Contacts == Conversation.Login_Creator, 1),
            else_=0
        ).label('Is_Creator')
    ).join(
        User,
        CompositionOfTheConversation.Login_Contacts == User.Login_User
    ).join(
        Conversation,
        CompositionOfTheConversation.ID_Conversation == Conversation.ID_Conversation
    ).filter(
        CompositionOfTheConversation.ID_Conversation == id_conversation
    ).group_by(
        CompositionOfTheConversation.Login_Contacts
    )

    # Выполняем запрос и получаем результат
    result = query.all()

    conversation_data = []

    for conversation in result:
        conversation_info = {
            "login": conversation[0],
            "name": conversation[1],
            "avatar": conversation[2],
            "Is_Creator": conversation[3],
        }
        conversation_data.append(conversation_info)

    return jsonify({
        "code": 200,
        "result": conversation_data
    })