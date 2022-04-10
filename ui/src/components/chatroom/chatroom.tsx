import './chatroom.scss';
import React, { useEffect, useState } from 'react';
import { ChatBubble } from '../chat-bubble/chat-bubble';
import { models } from '../../models';
import { useParams, useLocation } from 'react-router-dom';
import { getUser } from '../../utils';
import { APIService } from '../../services';

export interface ChatroomProps { }

type RouteParams = {
    id: string;
}

export const Chatroom: React.FunctionComponent<ChatroomProps> = () => {
    const location = useLocation();
    const [message, setMessage] = useState('');
    const sendingMessage = false;
    const [messages, loadMessages] = useState<models.Message[]>();
    const [loadingMessages, reloadMessages] = useState(true);
    const { id } = useParams<RouteParams>();
    const [currentUser, loadUser] = useState<models.User>();
    const [loadingUser, reloadUser] = useState(true);

    const sendMessage = () => {
        APIService.sendMessage(message, currentUser!.id, id!).then(function(){
            reloadMessages(true);
            setMessage('');
        });
    };

    useEffect(() => {
        APIService.getMessages(id!).then(function(res){
            let data = res;
            loadMessages(data);
            reloadMessages(false);
        });
    }, [loadingMessages, location]);

    useEffect(() => {
        let user = getUser();
        loadUser(user);
        reloadUser(false);
    }, [loadingUser]);

    return (
        <section className='chat'>
            <main className='chat__view'>
                {(messages || [])?.map((m, i) => {
                    const isContinued = (i + 1 < messages!.length) && messages![i + 1].sentBy.id === m.sentBy.id;
                    const isCurrentUser = m.sentBy.id === currentUser?.id;
                    return <ChatBubble key={m.id} name={m.sentBy.name} sentByUser={isCurrentUser} appearContinued={isContinued} content={m.content} />
                })}
            </main>
            <footer className='chat__input'>
                <textarea disabled={sendingMessage} value={message} onChange={(e) => setMessage(e.target.value)} />
                <button disabled={sendingMessage} onClick={() => sendMessage()}> Send </button>
            </footer>
        </section>
    )
};
