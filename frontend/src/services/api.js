import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000",
    headers: {
        "Content-Type": "application/json",
    },
});

export async function requestHumanApproval(requestData) {

    try {

        const response = await api.post(
            "/decision",
            requestData
        );

        return response.data;

    } catch (error) {

        console.error(
            "Decision API Error:",
            error
        );

        if (error.response) {

            console.error(
                error.response.data
            );

        }

        throw error;

    }

}

export async function getVoiceToken() {

    try {

        const response = await api.post(
            "/api/voice-token"
        );

        return response.data;

    } catch (error) {

        console.error(
            "Voice Token Error:",
            error
        );

        throw error;

    }

}

export default api;