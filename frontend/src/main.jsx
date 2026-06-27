import React from "react";
import ReactDOM from "react-dom/client";
import { VocalBridgeProvider } from "@vocalbridgeai/react";

import App from "./App";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")).render(
    <React.StrictMode>
        <VocalBridgeProvider
            options={{
                auth: {
                    tokenUrl: "http://127.0.0.1:8000/api/voice-token",
                },

                participantName: "Sifat",

                debug: true,
            }}
        >
            <App />
        </VocalBridgeProvider>
    </React.StrictMode>
);