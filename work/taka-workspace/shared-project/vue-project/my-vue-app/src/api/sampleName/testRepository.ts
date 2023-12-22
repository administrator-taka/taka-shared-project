import { client } from "@/api/sampleName/index";
import { testRequest } from "@/api/interface/request/testRequest";
import { testResponse } from "@/api/interface/response/testResponse";
import { AxiosResponse } from "axios";

export default {
  async testApi(params: testRequest): Promise<testResponse> {
    return await client
      .post("/test/db", params, {
        headers: { "Content-Type": "application/json" },
      })
      .then((res: AxiosResponse<testResponse>) => {
        return res.data;
      });
  },
};
