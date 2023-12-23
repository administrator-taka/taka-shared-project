import axios, { AxiosInstance } from "axios";

export const client: AxiosInstance = axios.create({
  baseURL: "/api", // プロキシで設定したパスと合わせてください
});
