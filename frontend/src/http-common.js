import axios from "axios";

export default axios.create({
    baseURL: "http://192.168.1.223:5050/api",
    headers: {
        "Content-type": "application/json"
    }
});