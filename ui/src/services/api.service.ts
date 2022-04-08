import { Chatroom, Message, User } from "../models/models";

export interface APIErrorResponse {
    code: number; 
    message: string;
}

const API_URL: string = process.env.CHAT_API_ENDPOINT || 'http://localhost:5000';

export class APIService {

    static isJson(res: Response): boolean {
        return !!res.headers.get('content-type')?.includes('application/json');
    }

    static async do(route: RequestInfo, options: RequestInit) {
        const res = await fetch(route, options);
        await APIService.throwIfError(res);
        if (APIService.isJson(res)) {
            return await res.json();
        }
        return await res.text();
    }

    static async throwIfError(res: Response): Promise<void> {
        if (res.ok) {
            return;
        }
        if (APIService.isJson(res)) {
            throw await res.json();
        }
        const error: APIErrorResponse = { code: res.status, message: res.statusText };
        throw error;
    }

    static async ping(): Promise<string> {
        return APIService.do(`${API_URL}/ping`, {
            method: 'GET',
        });
    }

    static async login(username: string): Promise<{}> {
        return APIService.do(`${API_URL}/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ "username":username })
        });
    }

    static async rooms(): Promise<Chatroom[]> {
        return APIService.do(`${API_URL}/rooms`, {
            method: 'GET',
        });
    }

    static async createRoom(name: string, userid: string): Promise<Chatroom> {
        return APIService.do(`${API_URL}/room`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ "roomname":name, "userid":userid })
        });
    }

    static async getMessages(roomid: string): Promise<Message[]> {
        return APIService.do(`${API_URL}/room/${roomid}`, {
            method: 'GET'
        });
    }

    static async sendMessage(text: string, userid:string, roomid:string): Promise<Message> {
        return APIService.do(`${API_URL}/message`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ "text":text, "userid":userid, "roomid":roomid })
        });
    }

    static async createUser(username: string): Promise<User> {
        return APIService.do(`${API_URL}/user`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ "username":username })
        });
    }
}
